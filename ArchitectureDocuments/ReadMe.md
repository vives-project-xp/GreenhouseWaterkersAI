# Architecture documents

This section contains the architecture documentens that are used in this project.

In the [ArchitectureDoc](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/ArchitectureDoc.pdf) you can find a flowcart
overview with all the block components that are used. Devided in a software block and a hardwareblock.

The hardwareblock contains a Raspberry Pi 5, a Sense Hat that is connected to the headerpins of the Raspberry Pi and a cameramodule for the Raspberry Pi.
The datasheets of the Raspberry Pi 5 can be found under the [RaspberryPi5Datasheet](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/RaspberryPi5Datasheet.pdf) file and the drawing can be found under the [RaspberryPi5Drawing](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/RaspberryPi5Drawing.pdf). A lot of additional information can be found on the website of [Raspberry Pi](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#raspberry-pi-5) documentation. The datasheet of the Sense HAT can be found under the [SenseHatDatasheet](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/SenseHatDatasheet.pdf) file and the schematics can be found under the [SenseHatDrawing](https://github.com/vives-project-xp/GreenhouseWaterkersAI/blob/main/ArchitectureDocuments/SenseHatDrawing.pdf).
Additional information can be found on the website of [Raspberry Pi](https://www.raspberrypi.com/documentation/accessories/sense-hat.html). From more information about the camera go to the website of [raspberry Pi](https://www.raspberrypi.com/documentation/accessories/camera.html).

The softwareblock contains the software that has been used during this project. 
[Labelbox](https://labelbox.com/) is used to label all the photo's with annotations. Via this [link](https://docs.labelbox.com/reference/quick-start) you can find a quick start guide to start a labelbox project.
[Edge Impulse]((https://edgeimpulse.com/)) is used to build the AI model and to train the model. It also supports deployment on the Raspberry Pi. Via this [link](https://docs.edgeimpulse.com/docs) you can find a quick start guide to start your own AI project.
The [library PyTorch](https://pytorch.org/docs/stable/index.html) is used to build an AI model using python programming. 
The [Stramlit library](https://docs.streamlit.io/) is used to make a dashboard.
