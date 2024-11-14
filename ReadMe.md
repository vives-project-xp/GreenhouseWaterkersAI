# Watercress AI project | [Projectfiche](./projectfiche.pdf)

## Overview
1. The project
2. Materials and software
3. Process
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
- 22/11 Deployment on edge devices (perhaps with casing)

## Materials and software

## Process
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

### Week 5
We tried to make a link between labelbox and edge impulse by writing a script that would download the images from labelbox with the bounding boxes and all the information we needed to upload them to edge impulse. First we tried a script that downloaded the images and put the info of the images into a CSV file. But that didn't seem to work quite well with edge impulse. Then we tried an other script that would download the images and put the info of the images into a COCO dataset format file. We had to tweak the script a bit to get it to work with edge impulse but in the end, we got it to work. You can find the scripts in [this folder](./LabelboxScripts/).

We adjusted the deployment of the model on the Raspberry Pi 5 and tested it. So that a picture could be taken and the model would predict the age of the watercress. The prediction was then displayed on the LED matrix of the Sense Hat. 

### Week 6
We continued by trying to get a working dashboard using the [streamlit library] (https://docs.streamlit.io/). We ran into a lot of issues when trying to get this to work. We tried different methods like using the edge impulse API as well as building the model and trying to run the code that way. Resolving one error kept leading to a different error.

### Week 7
This week we saw a breakthrough in the dashboard, as we got a working dashboard which makes predictions based on an uploaded image. We build a different model then the weeks before and with some changes to the code, we created a succesfull dashboard. With that same model we created a script to analyse the model and images. We got a graph for the amount of images in each class, a confusion matrix, etc.. We also added some more images (for the day 19 and 20 classes, because they were not represented enough) and raised our accuracy to 88%. ![image](https://github.com/user-attachments/assets/35a7e844-a36d-441a-9a4a-59232430ec8b)


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
To build a dataset for watercress growth, you'll need to start by planting the watercress! Here’s a step-by-step guide to set up your experiment and capture high-quality data:
1) Planting the watercress
   - **Materials**: Watercress seeds, a small container, soil, water, and a spray bottle.
   - **Planting**: Fill the container with soil and sprinkle the seeds on top. Cover the seeds with a thin layer of soil and mist them with water. Keep the soil moist by misting it daily.
   - **Light & Temperature**: Place the container in indirect sunlight at a temperature between 10-20°C.
2) Capturing the data
    - **Materials**: A camera (phone or camera), a tripod, and a notebook.
    - **Setup**: Place the camera on a tripod to ensure consistent framing and lighting conditions. Position the camera so that the watercress is in the center of the frame. Take pictures from multiple angles to capture the growth of the watercress.
    - **Capture**: Take pictures of the watercress every day at the same time to ensure consistency.
    - **Notes**: Keep a notebook to record the date and time of each picture to track the growth of the watercress.
3) Data organization
    - **Folders**: Create a folder for each day of the experiment (e.g., day 0, day 1, day 2, etc.). Save the images from each day in the corresponding folder.
    - **Naming**: Name the images with a unique identifier to track the growth of the watercress (e.g., day0_001.jpg, day1_001.jpg, etc.).
4) Duration
    - **Timeline**: Capture images of the watercress every day for 20 days to track its growth over time.

By following these steps, you can create a dataset of watercress growth that can be used to train a machine learning model to predict the age of the watercress based on its appearance.

### Labeling | [Labelbox](https://labelbox.com/)
After creating a dataset of watercress, you need to label the images. We used Labelbox to label the images.
1) Go to the Labelbox website (https://labelbox.com/) and create an account. This will lead you to the dashboard screen where you can create a new project. 
2) After creating a new project, you will need to add data to the project. To do this go to the catalog tab and click on the "New" button. This will add a new dataset to the project.
3) Go to annotate, click the "Add data" button, and add the dataset of the watercress to the project. After that you will have to set up the ontology for this project. The ontology is a list of labels that you can use to label the images. We used bounding boxes for labeling the days from "day 0" to "day 20" because edge impulse requires bounding boxes for object detection.
4) After setting up the ontology, you can start labeling the images. To label an image, click on the image and draw a bounding box around the whole picture.
5) After labeling all the images, you need to review all the labels to make sure they are correct. You can do this by clicking on the "Review" tab and reviewing the labels one by one. If you find any mistakes, you can correct them by clicking on the label and editing it.
6) After reviewing all the labels, you can export the labels by clicking on the "Export" button on the "Done" tab. This will export the labels in a JSON format. You can use this JSON file to write a python script that downloads the images with the bounding boxes and all the information you need to upload them to edge impulse. You can download the images into one folder so it's easier to upload them to edge impulse.

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
To prove our model works, we want to create a very simple dashboard that shows the prediction (from our model) when an image is pressed. For this we will use a virtual environment.
1) Get the .lite file from the dashboard. Place it in your project folder
2) We use windows, but it's recommended to use Linux (WSL) for this part. Follow the [Installation guide ](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) if you don't have it installed already.
3) With your WSL(ubuntu) terminal opened we will first create a virtual environment.
Ensure you have installed Python version 3.x. If this is not the case, run:
```
python3 --version
```
Ensure you have installed Python version 3.x. Check this by running the following command:
```
python3 --version
```

If you have not installed it yet, you can do so by running:
```
sudo apt update
sudo apt install python3 python3-pip
```

Let's create the virtual environment now!
```
python3 -m venv envname
```

Activate the environment like this:
```
source myenv/bin/activate
```

Now you can install the packages.
```
pip install streamlit tensorflow
```
4) Download [this](). Replace the model name with the name and path of your model.
5) To run, type `streamlit run {fileName}`

STILL WORKING ON THE REST


## Difficulties
1) We experienced how important the right amount of data is. Early in the project we had few images which made the model really bad of course. Later we had a lot of images but for some classes (days) we had way more or less images then for others. This meant the model overfit on those with more images. By balancing this out we created a fairly good model rather quick.

## Final Product








This project was made by Lynn Delaere, Lennart Fonteyne, and Esteban Desmedt for Vives project experience 2024-2025.
