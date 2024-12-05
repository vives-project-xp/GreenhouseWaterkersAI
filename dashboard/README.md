# Watercress Age Prediction with Streamlit and TensorFlow Lite

This project is a web application for predicting the age of Watercress plants using a pre-trained TensorFlow Lite model. The app is built with Streamlit and provides an interactive interface for uploading images or selecting example images, running the model, and visualizing predictions.

## Features

- **Interactive Image Upload:** Upload custom images of Watercress for prediction.
- **Example Image Selection:** Choose from a set of example images included in the `example_images` folder.
- **Model Output Visualization:**
  - Displays the predicted age of Watercress along with confidence scores.
  - Provides a bar chart visualization of model confidence across all age classes using Plotly.
- **Easy-to-Use Interface:** Built with Streamlit, the app is intuitive and works in any browser.

## Prerequisites

### Environment Setup

To run the app, you will need to set up a Python environment with the required dependencies. It is recommended to use a virtual environment.

1. **Create a virtual environment:**

    ```bash
    python -m venv myenv
    ```

2. **Activate the virtual environment:**

    On Windows:

    ```bash
    myenv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash
    source myenv/bin/activate
    ```

3. **Install Required Libraries**

    Install the dependencies from:

    ```bash
    pip install streamlit tensorflow pillow plotly
    ```

## Folder Structure

```plaintext
project/
│
├── model.lite              # Pre-trained TensorFlow Lite model
├── example_images/             # Folder containing example images
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ... (more example images)
├── main.py                      # Main Streamlit app script
└── README.md                   # Project documentation
```
## Running the Application
1. **Start the streamlit app:**
```bash
streamlit run main.py
```
2. **Access the app in your browser on the link that is provided**

## How to Use

Using the app is fairly straightforward. You can either upload an image yourself or use one of the provided example images that are conveniently provided for you on the left. 
