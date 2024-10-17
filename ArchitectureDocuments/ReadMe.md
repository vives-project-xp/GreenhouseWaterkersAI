# Architecture documents

This section contains the architecture documentens that are used in this project.

## Flowchart
In the [ArchitectureDoc](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/ArchitectureDoc.pdf) you can find a flowcart
overview with all the block components that are used. Devided in a software block and a hardwareblock.

## Hardware
The hardwareblock contains a Raspberry Pi 5, a Sense Hat that is connected to the headerpins of the Raspberry Pi and a cameramodule for the Raspberry Pi.

A Raspberry Pi is a single-board computer from the Raspberry Pi Foundation. It has a quad-core ARM Cortex-A76 processor, improved GPU (VideoCore VII), up to 8GB of RAM, and support for PCIe 2.0, allowing for faster data transfer and more expansion options. It has dual 4K HDMI output, improved USB 3.0 connectivity, Gigabit Ethernet, and a redesigned power management system for better performance and energy efficiency. It is an ideal device for more demanding applications like AI.
The Raspberry Pi Sense HAT is an add-on board for the Raspberry Pi that includes a variety of sensors and an LED matrix. It features sensors for temperature, humidity, pressure, orientation, and motion. The 8x8 RGB LED matrix can display data, images, and patterns, while the onboard joystick allows for simple user interaction.
The datasheets of the Raspberry Pi 5 can be found under the [RaspberryPi5Datasheet](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/RaspberryPi5Datasheet.pdf) file and the drawing can be found under the [RaspberryPi5Drawing](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/RaspberryPi5Drawing.pdf). A lot of additional information can be found on the website of [Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-5) documentation. The datasheet of the Sense HAT can be found under the [SenseHatDatasheet](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/SenseHatDatasheet.pdf) file and the schematics can be found under the [SenseHatDrawing](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/SenseHatDrawing.pdf).
Additional information can be found on the website of [Raspberry Pi](https://www.raspberrypi.com/documentation/accessories/sense-hat.html). From more information about the camera go to the website of [raspberry Pi](https://www.raspberrypi.com/documentation/accessories/camera.html).

## Software
The softwareblock contains the software that has been used during this project. 
[Labelbox](https://labelbox.com/) is a data-labeling platform designed to help users create, manage, and improve training data for machine learning models. It provides tools to annotate and label various types of data, including images, video, text, and sensor data, using techniques like bounding boxes, segmentation, classification, and more. It also supports APIs and SDKs for automating data management tasks. Via this [link](https://docs.labelbox.com/reference/quick-start) you can find a quick start guide to start a labelbox project.
[Edge Impulse]((https://edgeimpulse.com/)) is a machine leaning development platform focused on building and deploying models for edge devices, such as microcontrollers, IoT devices, and embedded systems. It provides tools for data collection, model training and deployment designed for low-power devices. This allows developers to easily deploy trained models directly onto edge devices for real-time, on-device inference.
Via this [link](https://docs.edgeimpulse.com/docs) you can find a quick start guide to start your own AI project.
[PyTorch](https://pytorch.org/docs/stable/index.html) is an open-source python machine learning framework. It is widely used for building and training neural networks, espacially in deep learning. PyTorch provides a flexible and intuitive interface with dynamic computational graphs, making it easy to experiment with different model architectures and debug code. 
You can use PyTorch to create and train machine learning models for tasks like computer vision, natural language processing, and reinforcement learning.
[Stramlit](https://docs.streamlit.io/) is an open-source Python framework for building interactive web applications for data science and machine learning projects.With Streamlit, you can create interactive dashboards, visualize data, and deploy machine learning models with just a few lines of code. It supports various widgets for user input, like sliders, buttons, and text inputs, which makes it easy to create dynamic and responsive interfaces.
