# Watercress AI project | [Projectfiche](./projectfiche.pdf)

## Overview
1. The project
2. Materials and software
3. Proces
4. Architecture
5. Guide
6. Difficulties
7. Final product

## The project
The WaterCress AI project has the main goal of creating a working AI model, which is then deployed on an embedded device. The challenges in this project lay in the gathering of our own data to create a labeled dataset. Following that, the model has to be chosen and trained to guarantee the best possible result. Ultimately, the model has to run on an embedded device. The project is deemed successful when we can make an accurate prediction using a camera on the chosen embedded device and then display this in a way (display).
We use watercress as it grows quickly, but it should be possible to use the same way of working to get the same result for a different type of plant. 

### Goals
Here you find a small list of the main goals we set for ourselves with deadlines that we would like to hit.
- 26/09 Planting the watercress, Order materials
- 03/10 Testing with sample data (as watercress was not visible on pictures yet)
- 17/10 Full dataset from day 1 till day 20
- 24/10 Trained model 
- 07/11 Dashboard to display model
- 22/11 Deployment on edge devices (perhabs with casing)

## Materials and software

## Proces
In this section, you can find a step-by-step analysis of the steps we took to get to the final project.
### Week 1
When brainstorming, we quickly had a plan. The main thing we thought about was the software we would want to use. As some of us had a bit of experience with Kerras and TensorFlow, this was our first option. Another option was using pytorch as it should become the standard for AI projects in the foreseen future. Lastly, we talked about the option of using Edge Impulse (https://edgeimpulse.com/). It's an online webpage that specializes in neural networking solutions. At first we chose this option as it's a faster way to create and train models and analyze all of your data. It also has some built-in tools to split data (if you've not done so). Of course we need to deploy our model, which we chose the Raspberry Pi 5 for as it has a lot of calculation power to run a model. We also ended up ordering a camera and display for the Raspberry to be able to make pictures and display the age on the display.

### Week 2
We started off with a small amount of data, which wasn't of great help because only on the last day the watercress became visible. We did use this to train a model that could see if there was watercress in the image. We had some issues getting a good result on this as the data with watercress was very limited. This week we finalized the [project canvas](./project-canvas.pdf) and started making the [architecture document](./ArchitectureDocuments/ArchitectureDoc.pdf). After receiving our materials, we also initialized the raspberry (first it was a raspberry pi 4) and tested the camera and display by writing some Python script. These worked correctly, and we created some more specific script for our project (displaying a number on the screen after making a picture). Of course this didn't use any AI yet. 

### Week 3 
With some more data, we expected better results from our model, but the results were not as good as expected. This week we tested some models with TensorFlow and pytorch and got some 'ok' results. We also started using a different tool to label our data, called Labelbox (https://labelbox.com/). We chose to use this as we already had close to 250 images, and this kept growing day by day. Even though our edge impulse model wasn't performing to our expectations, we experimented with deploying that (bad) model on the raspberry. We ran into a few issues with the files but found another way to deploy the model (described in the guide). We still experienced some issues with the camera and tried another one, which worked.

### Week 4
As we now gained a sufficient amount of data, we first labeled everything to then try to train a new model on edge impulse. We had low expectations, but our model performed rather well. We fine-tuned it a bit and left out the last day of data (as we only had 6 images for that day at the time). And that's why we've got our best result yet.
![image](https://github.com/user-attachments/assets/c04771c4-8510-4177-904a-4b14dc07b3b8)
The accuracy on itself was already good, but for this project we didn't mind predictions that we're one to three days away from the actual age. With this in mind, our accuracy is more like 95%.

We then proceeded to get the new model on the Raspberry and test it. While working on a script to test it without edge impulse, we also worked on our documentation. 

## Architecture
Below you find the [architecture document] (./ArchitectureDocuments/ArchitectureDoc.pdf) with some explanation.
![image](https://github.com/user-attachments/assets/0e066311-f14f-4c5c-9857-6393a01e0a65)
### Software
To train our model, we use different libraries, software, and hardware devices. To capture images from the watercress, we used the camera of our phone and saved them on a hard drive. Later, we also used Labelbox to label the images (and save them). This is how we created our dataset, which exists only of folders with the days. This is because edge impulse can automatically split between validation, training, and test data. To evaluate, display, and proof our model, we will create a small and basic dashboard using streamlit (which is a Python library used for dashboard representations).

### Hardware
As an embedded device to run our model, we chose the Raspberry Pi 5. It's a single-board computer that we can use to deploy our AI model. We use the Raspberry Pi camera V2 (connected with 4-lane MIPI camera display transceivers) and the sense hat, which uses an LED matrix to represent, for example, the predicted age (which contains a joystick button).

### Deployment | [Edge Impulse documentation](https://docs.edgeimpulse.com/docs)
There are multiple options to go on and deploy the model. We can transfer the files by downloading the model from Edge Impulse and putting them on the SD card. We also have the possibility to connect via the Raspberry Pi 5 to the edge impulse directly. 

## Guide
This section describes the exact steps to take to make this project yourself!
### Dataset creation

### Edge Impulse | [Edge Impulse](https://studio.edgeimpulse.com/) 
1) After signing up, you can create and name a project, which will lead you to the dashboard screen. Scroll down till you find the area about **project info** on the right side. For this project, set the labeling method to "one label per data item." This setting is used for classification. The other one is used for object detection, which we don't need for this specific project.
2) For now we can skip the device section as we will upload images and not get the data ourselves. If you want to make the images with your embedded device, connect using the edge impulse documentation (or follow the steps later in this guide for Raspberry Pi 5 only).
3) Proceed to the **Data Acquisition** section and press upload data. For upload mode, you can press "select a folder," as we've labeled all data in folders. Under select files, press the button and navigate to your data folder. Now select the correct folder (iterate over all of the folders). Under upload into category, we chose to let Edge Impulse split the data itself, but if you have performed the split, you can select "training" or "test" data accordingly. Under "label," choose the bottom option and fill in the label, matching the folder name (so "0" for day 0, etc.). At the top, you will now find the amount of items and the split. Aim for a split of around 80%/20% for training/test data.
    - Training data: This is the dataset used to teach the machine learning model. The model learns the relationships between input features and the target variable by adjusting its parameters to minimize the error or loss.
    - Validation data: This dataset is used to fine-tune the model’s hyperparameters (like learning rate, number of layers, etc.) and assess its performance while training. It helps prevent the model from overfitting the training data.
    - Test data: This dataset evaluates the final model's performance after training and validation are complete. It provides an unbiased estimate of how the model will perform on new, unseen data.
4) Now navigate to **create impulse**; you can play with the options here, but we chose the following impulse (don't forget to press save!)
   
![image](https://github.com/user-attachments/assets/52ae42f6-1292-48fc-8ddc-b1ba327a93bb)

5) Next, go to the **image** section and press "save parameters." Now press "generate parameters" and wait till the feature explorer is shown. Like this (the part with the graph)
![image](https://github.com/user-attachments/assets/d0fde320-7646-4a9f-9381-a7e095e55af1)

6) Following that, press "transfer learning" in our case. You have a lot of options that you can play with to fine-tune and experiment. We recommend starting by keeping the default settings and pressing the "save & train" button. Now wait till you get the model result (this can take a bit of time, depending on the amount of images and epochs).
![image](https://github.com/user-attachments/assets/eb8357e3-7369-42f5-80bc-cfd21bff3d9b)

The left top to right bottom diagonal (green squares) is very important in this truth table. These are the correctly classified images by the model (on validation data). For this project, the ones that are within 3 squares (right and left) of the correct prediction are also considered "good" (146/154, so 95%).

7) Now go to **Retrain model** and press "train model." Wait till it's done (takes a bit longer than the previous step). Look for green text saying it is done in the mini terminal at the right top.
8) Now you have access to **live classification** and **model testing**. Model testing will give you an overview of all test data, which you can have a look at. In classification, you can test on each individual image and, most importantly, test on data collected with your embedded device (with a camera, of course).
   
**--! EXPLANATION ON HOW TO CONNECT TO DEVICE!--**
The first step is installing Edge Impulse on your device, in our case a Raspberry Pi 5. There is a very simple [guide] (https://docs.edgeimpulse.com/docs/edge-ai-hardware/cpu/raspberry-pi-5) made by Edge Impulse themselves. After having installed it, you need to follow the on-screen prompts and set up Edge Impulse on the device. It is a very simple process of logging in, selecting your input devices, and what project you're working on.
      

### Deployment
To deploy the model on your device, there are 2 ways. The first is with the SDK's. Simply go to your Edge Impulse dashboard and navigate to the "Deployment" tab. 
![image](./ArchitectureDocuments/Deploy.png)
After having selected the right deployment (in our case, Linux AARCH64), you need to run `edge-impulse-linux-runner` on your device, and it should connect if you set it up right.
The second way involves placing the downloaded model file onto the device itself. This can be done through various means; we used WinSCP to place the file onto our Raspberry Pi 5. After that, you can use the model freely in your project.
### Dashboard




## Difficulties

## Final Product








This project was made by Lynn Delaere, Lennart Fonteyne, and Esteban Desmedt for Vives project experience 2024-2025.
