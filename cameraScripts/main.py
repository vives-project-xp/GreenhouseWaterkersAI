#!/usr/bin/env python

import cv2
import os
import sys
import getopt
import signal
import time
from sense_hat import SenseHat
from edge_impulse_linux.image import ImageImpulseRunner

runner = None
show_camera = True
if (sys.platform == 'linux' and not os.environ.get('DISPLAY')):
    show_camera = False

sense = SenseHat()

def now():
    return round(time.time() * 1000)

def get_webcams():
    port_ids = []
    for port in range(5):
        print("Looking for a camera in port %s:" % port)
        camera = cv2.VideoCapture(port)
        if camera.isOpened():
            ret = camera.read()[0]
            if ret:
                backendName = camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                print("Camera %s (%s x %s) found in port %s " % (backendName, h, w, port))
                port_ids.append(port)
            camera.release()
    return port_ids

def sigint_handler(sig, frame):
    print('Interrupted')
    if (runner):
        runner.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def help():
    print('python classify.py <path_to_model.eim> <Camera port ID, only required when more than 1 camera is present>')

def take_picture(camera):
    """ Capture an image from the camera and save it to disk. """
    ret, frame = camera.read()
    if ret:
        filename = "captured_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image captured and saved as {filename}")
        return filename
    else:
        print("Failed to capture image.")
        return None

def display_on_sensehat(text):
    """ Display the text on the Sense HAT LED display. 
    If it's a single letter, show it permanently. If it's more than one letter, scroll the text continuously. """
    sense.clear()

    if len(text) == 1:
        sense.show_letter(text, text_colour=[0, 255, 0], back_colour=[0, 0, 0])
    else:
        while True:
            sense.show_message(text, text_colour=[0, 255, 0], back_colour=[0, 0, 0], scroll_speed=0.1)

def run_model_on_image(runner, image_file):
    """ Run the model on the captured image and display the highest confidence label. """
    for res, img in runner.classifier(image_file):
        if "classification" in res["result"].keys():
            # Get the highest confidence label
            highest_label = max(res['result']['classification'], key=res['result']['classification'].get)
            print(f"Classified as: {highest_label}")
            
            # Display the label on the Sense HAT display
            display_on_sensehat(highest_label)

def joystick_pressed(event, runner, camera):
    """ Callback function to capture and classify image when joystick is pressed. """
    if event.action == "pressed" and event.direction == "middle":
        print("Joystick pressed, taking picture...")
        filename = take_picture(camera)
        if filename:
            run_model_on_image(runner, filename)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["--help"])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit()

    if len(args) == 0:
        help()
        sys.exit(2)

    model = args[0]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    modelfile = os.path.join(dir_path, model)

    print('MODEL: ' + modelfile)

    with ImageImpulseRunner(modelfile) as runner:
        try:
            model_info = runner.init()
            print('Loaded runner for "' + model_info['project']['owner'] + ' / ' + model_info['project']['name'] + '"')
            labels = model_info['model_parameters']['labels']

            if len(args) >= 2:
                videoCaptureDeviceId = int(args[1])
            else:
                port_ids = get_webcams()
                if len(port_ids) == 0:
                    raise Exception('Cannot find any webcams')
                if len(args) <= 1 and len(port_ids) > 1:
                    raise Exception("Multiple cameras found. Add the camera port ID as a second argument to use this script")
                videoCaptureDeviceId = int(port_ids[0])

            # Open the selected camera
            global camera
            camera = cv2.VideoCapture(videoCaptureDeviceId)
            ret = camera.read()[0]
            if ret:
                backendName = camera.getBackendName()
                w = camera.get(3)
                h = camera.get(4)
                print("Camera %s (%s x %s) in port %s selected." % (backendName, h, w, videoCaptureDeviceId))
            else:
                raise Exception("Couldn't initialize selected camera.")

            # Register joystick event and pass runner and camera to the callback
            sense.stick.direction_any = lambda event: joystick_pressed(event, runner, camera)
            print("Press the joystick to take a picture...")

            # Keep the program running to listen for joystick presses
            while True:
                time.sleep(1)

        finally:
            if runner:
                runner.stop()
            camera.release()

if __name__ == "__main__":
    main(sys.argv[1:])
