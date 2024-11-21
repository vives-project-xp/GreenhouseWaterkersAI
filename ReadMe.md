# Watercress AI project | [Projectfiche](./projectfiche.pdf)

## Overview
1. The project
2. Materials and software
3. Process
4. Architecture
5. [Guide](./TechnicalDoc/guide.md)
6. Difficulties
7. Final product

## The project
The WaterCress AI project has the main goal of creating a working AI model, which is then deployed on an embedded device. The challenges in this project lay in the gathering of our own data to create a labeled dataset. Following that, the model has to be chosen and trained to guarantee the best possible result. Ultimately, the model has to run on an embedded device. The project is deemed successful when we can make an accurate prediction using a camera on the chosen embedded device and then display this in a way (display).
We use watercress as it grows quickly, but it should be possible to use the same way of working to get the same result for a different type of plant. 

### Goals
Here you find a small list of the main goals we set for ourselves with deadlines that we would like to hit.
- 26/09 Planting the watercress, Order materials [x]
- 03/10 Testing with sample data (as watercress was not visible on pictures yet) [x]
- 17/10 Full dataset from day 1 till day 20 [x]
- 24/10 Trained model [x]
- 07/11 Dashboard to display model [x]
- 22/11 Deployment on edge devices (perhaps with casing) [ ] note: to do stand alone deployment, and casing.
- 05/12 Stand alone deployment, and casing [ ]

## Materials and software
## Process
In this section, you can find a step-by-step analysis of the steps we took to get to the final project.
### Week 1
When brainstorming, we quickly had a plan. The main thing we thought about was the software we would want to use. As some of us had a bit of experience with Keras and TensorFlow, this was our first option. Another option was using pytorch as it should become the standard for AI projects in the foreseen future. Lastly, we talked about the option of using Edge Impulse (https://edgeimpulse.com/). It's an online webpage that specializes in neural networking solutions. At first we chose this option because it offers a faster way to create, train models, and analyze data. It also has some built-in tools to split data (if you've not done so). Of course we need to deploy our model, which we chose the Raspberry Pi 5 for as it has a lot of calculation power to run a model. We also ended up ordering a camera and display for the Raspberry to be able to make pictures and display the age on the display.

### Week 2
We started off with a small amount of data, which wasn't very helpful since watercress only became visible in the images on the final day. We did use this to train a model that could see if there was watercress in the image. We had some issues getting a good result on this as the data with watercress was very limited. This week we finalized the [project canvas](./project-canvas.pdf) and started making the [architecture document](./ArchitectureDocuments/ArchitectureDoc.pdf). After receiving our materials, we also initialized the raspberry (first it was a raspberry pi 4) and tested the camera and display by writing some Python script. These worked correctly, and we created some more specific script for our project (displaying a number on the screen after making a picture). Of course this didn't use any AI yet. 

### Week 3 
With some more data, we expected better results from our model, but the results were not as good as expected. This week we tested some models with TensorFlow and pytorch and got some 'ok' results. We also started using a different tool to label our data, called Labelbox (https://labelbox.com/). We chose to use this as we already had close to 250 images, and this kept growing day by day. Even though our edge impulse model wasn't performing to our expectations, we experimented with deploying that (bad) model on the raspberry. We ran into a few issues with the files but found another way to deploy the model (described in the guide). We still experienced some issues with the camera and tried another one, which worked.

### Week 4
As we now gained a sufficient amount of data, we first labeled everything to then try to train a new model on edge impulse. We had low expectations, but our model performed rather well. We fine-tuned it a bit and left out the last day of data (as we only had 6 images for that day at the time). And that's why we've got our best result yet.
![image](https://github.com/user-attachments/assets/c04771c4-8510-4177-904a-4b14dc07b3b8)
The accuracy on itself was already good, but for this project we didn't mind predictions that were one to three days away. from the actual age. Considering this tolerance, our effective accuracy is approximately 95%.

We then proceeded to get the new model on the Raspberry and test it. While working on a script to test it without edge impulse, we also worked on our documentation. 

### Week 5
We tried to make a link between labelbox and edge impulse by writing a script that would download the images from labelbox with the bounding boxes and all the information we needed to upload them to edge impulse. First we tried a script that downloaded the images and put the info of the images into a CSV file. But that didn't seem to work quite well with edge impulse. Then we tried an other script that would download the images and put the info of the images into a COCO dataset format file. We had to tweak the script a bit to get it to work with edge impulse but in the end, we got it to work. You can find the scripts in [this folder](./LabelboxScripts/).

We adjusted the deployment of the model on the Raspberry Pi 5 and tested it. So that a picture could be taken and the model would predict the age of the watercress. The prediction was then displayed on the LED matrix of the Sense Hat. 

### Week 6
We continued by trying to get a working dashboard using the [streamlit library] (https://docs.streamlit.io/). We ran into a lot of issues when trying to get this to work. We tried different methods like using the edge impulse API as well as building the model and trying to run the code that way. Resolving one error kept leading to a different error.

### Week 7
This week we saw a breakthrough in the dashboard, as we got a working dashboard which makes predictions based on an uploaded image. We build a different model then the weeks before and with some changes to the code, we created a succesful dashboard. With that same model we created a script to analyse the model and images. We got a graph for the amount of images in each class, a confusion matrix, etc.. We also added some more images (for the day 19 and 20 classes, because they were not represented enough) and raised our accuracy to 88%. 
![image](https://github.com/user-attachments/assets/35a7e844-a36d-441a-9a4a-59232430ec8b)


## Architecture
Below you find the [architecture document] (./ArchitectureDocuments/ArchitectureDoc.pdf) with some explanation.
![image](https://github.com/user-attachments/assets/0e066311-f14f-4c5c-9857-6393a01e0a65)
### Software
To train our model, we use different libraries, software, and hardware devices. To capture images from the watercress, we used the camera of our phone and saved them on a hard drive. Later, we also used Labelbox to label the images (and save them). This is how we created our dataset, which exists only of folders with the days. This is because edge impulse can automatically split between validation, training, and test data. To evaluate, display, and proof our model, we will create a small and basic dashboard using streamlit (which is a Python library used for dashboard representations).

### Hardware
As an embedded device to run our model, we chose the Raspberry Pi 5. It's a single-board computer that we can use to deploy our AI model. We use the Raspberry Pi camera V2 (connected with 4-lane MIPI camera display transceivers) and the sense hat, which uses an LED matrix to represent, for example, the predicted age (which contains a joystick button).

### Deployment | [Edge Impulse documentation](https://docs.edgeimpulse.com/docs)
There are multiple options to go on and deploy the model. We can transfer the files by downloading the model from Edge Impulse and putting them on the SD card. We also have the possibility to connect via the Raspberry Pi 5 to the edge impulse directly. 



## Difficulties
1) We experienced how important the right amount of data is. Early in the project, we had few images, which naturally led to poor model performance. Later we had a lot of images but for some classes (days) we had way more or fewer images than for others. This meant the model overfit on those with more images. By balancing this out we quickly created a fairly accurate model.

## Final Product








This project was made by Lynn Delaere, Lennart Fonteyne, and Esteban Desmedt for Vives project experience 2024-2025.
