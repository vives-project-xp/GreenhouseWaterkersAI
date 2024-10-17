# Watercress AI project
## Overview
1. The project
2. Materials and software
3. Proces
4. Guide
5. Difficulties
6. Final product

## The project
The watercress AI project has the main goal of creating a working AI model which is then deployed on an embedded device. The challanges in this project lay in the gathering of our own data to create a labeled dataset. Following that, the model has to be chosen and trained to garantee the best possible result. Ultimately the model has to run on an embedded device. The project is deemed succesfull when we can make accurate prediction using a camera on the chosen embedded device and then display this in a way (display).
We use watercress as it grows quickly, but it should be possible to use the same way of working to get the same result for a different type of plant. 

### Goals
Here you find a small list of the main goals we set for ourself with deadlines that we would like to hit.
- 26/09 Planting the watercress, Order materials
- 03/10 Testing with sample data (as watercress was not visible on pictures yet)
- 17/10 Full dataset from day 1 till day 20
- 24/10 Trained model 
- 07/11 Dashboard to display model
- 22/11 Deployment on edge device (perhabs with casing)

## Materials and software

## Proces
At this section you can find a step by step analysis of the steps we took to get to the final project
### Week 1
When brainstorming we quickly had a plan. The main thing we thought about was the software we would want to use. As some of us had a bit of experience with kerras and tensorflow, this was our first option. Another option was using pytorch as it should become the standard for AI projects in the foreseen future. Lastly we talked about the option of using edge impulse (https://edgeimpulse.com/). It's an online webpage that specializes in neural networking solutions. At first we chose this option as it's a faster way to create and train models and analyse all of your data. It also has some build in tools to split data (if you've not done so). Of course we need to deploy our model, which we chose the raspberry pi 5 for as it has a lot of calculation power to run a model. We also ended up ordering a camera and display for the raspberry to be able to make pictures and display the age on the display.

### Week 2
We started of with a small amount of data which wasn't of great help because only on the last day the watercress became visible. We did use this to train a model that could see if there was watercress in the image. We had some issues to get a good result on this as the data with watercress was very limited. This week we finalized the project canvas and started making the architecture document.

## Guide
This section describes the exact steps to take to make this project yourself!


![image](https://github.com/user-attachments/assets/c04771c4-8510-4177-904a-4b14dc07b3b8)

## Difficulties

## Final Product








This project was made by Lynn Delaere, Lennart Fonteyne and Esteban Desmedt for Vives project experience 2024-2025
