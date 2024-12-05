import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import plotly.graph_objects as go
import os

# Load Edge Impulse model (TensorFlow Lite)
MODEL_PATH = "model.lite"
try:
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()
    st.write("Model loaded successfully!")
except ValueError as e:
    st.error(f"Error loading model: {e}")
except Exception as e:
    st.error(f"Unexpected error loading model: {e}")

# Get input and output details of the model
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Define folder with example images
EXAMPLE_IMAGES_FOLDER = "example_images"

def load_image(image_file):
    """Load an image from file and convert it to RGB."""
    img = Image.open(image_file)
    return img.convert("RGB")

def preprocess_image(image, input_shape):
    """Resize image to model's input shape and normalize pixel values."""
    image = image.resize((input_shape[1], input_shape[2]))
    image_array = np.array(image, dtype=np.float32)
    # Normalize the image to match the input range of the model
    image_array = image_array / 255.0
    return np.expand_dims(image_array, axis=0)

def run_inference(image):
    """Run classification on the input image using the TFLite model."""
    try:
        input_shape = input_details[0]['shape']
        processed_image = preprocess_image(image, input_shape)
        
        # Set the model input
        interpreter.set_tensor(input_details[0]['index'], processed_image)
        interpreter.invoke()
        
        # Retrieve the output (the model predicts the age of the Watercress from 1 to 19)
        output = interpreter.get_tensor(output_details[0]['index'])[0]

        # Get the predicted age (the index of the highest probability)
        predicted_age = np.argmax(output)  # Adding 1 because the class indices start from 0
        confidence = output[np.argmax(output)]  # The confidence of the prediction

        # Map the output to human-readable age values (1-19)
        age_labels = [str(i) for i in range(0, 21)]  # Age labels from 1 to 19
        age_probabilities = {age_labels[i]: output[i] for i in range(len(output))}

        # Sort age probabilities in descending order (optional, to display the top prediction)
        sorted_ages = sorted(age_probabilities.items(), key=lambda x: x[1], reverse=True)

        return predicted_age, confidence, sorted_ages, age_probabilities
    except IndexError as e:
        st.error(f"Index error in retrieving model outputs: {e}")
        return None, None, None, None
    except Exception as e:
        st.error(f"Unexpected error during inference: {e}")
        return None, None, None, None

# Streamlit App Layout
st.title("Watercress Age Prediction")

st.write("Upload an image of Watercress, or select one of the example images to predict its age (0-20).")

# Sidebar for chart and example images
st.sidebar.title("Prediction Details")

# Placeholder for the chart
chart_placeholder = st.sidebar.empty()

# Example Images Section
st.sidebar.title("Example Images")
selected_image = None

# Get the list of example images
example_images = [
    os.path.join(EXAMPLE_IMAGES_FOLDER, f)
    for f in os.listdir(EXAMPLE_IMAGES_FOLDER)
    if f.endswith((".jpg", ".jpeg", ".png"))
]

if example_images:
    for example_path in example_images:
        # Display image preview in the sidebar
        img_preview = load_image(example_path)
        if st.sidebar.button(f"Select", key=example_path):
            selected_image = example_path
        st.sidebar.image(img_preview, use_container_width=True)

# File uploader for user images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Determine which image to process: uploaded or selected from examples
if selected_image:
    image = load_image(selected_image)
    st.sidebar.write(f"Using example image: {os.path.basename(selected_image)}")
elif uploaded_file:
    image = load_image(uploaded_file)
else:
    image = None

if image:
    # Create three sections: one for the image, one for the output
    col1, col2 = st.columns([3, 3])  # Two main columns for the app layout
    
    with col1:
        st.image(image, caption="Selected Image", use_container_width=True)

    with col2:
        st.write("Running model...")
        try:
            predicted_age, confidence, sorted_ages, age_probabilities = run_inference(image)

            if predicted_age is not None:
                st.write(f"Predicted Age: {predicted_age}")
                st.write(f"Confidence: {confidence * 100:.2f}%")
                st.write(f"Sorted Age Probabilities:")

                # Display sorted age probabilities (optional)
                for age, prob in sorted_ages:
                    st.write(f"Age {age}: {prob * 100:.2f}%")
            else:
                st.error("Model did not return valid outputs.")
        except Exception as e:
            st.error(f"Error in processing image: {e}")

        # Update the chart in the sidebar
        with chart_placeholder.container():
            st.title("Prediction Confidence Chart:")
            age_labels = [str(i) for i in range(0, 21)]
            prob_values = [age_probabilities[label] for label in age_labels]

            # Create Plotly bar chart
            fig = go.Figure()
            fig.add_trace(
                go.Bar(
                    x=age_labels, 
                    y=prob_values, 
                    marker=dict(color='skyblue'), 
                    name="Confidence"
                )
            )
            fig.update_layout(
                title="Model Confidence for Each Age (0-20)",
                xaxis_title="Age",
                yaxis_title="Confidence",
                xaxis=dict(tickmode="linear"),
                template="plotly_white",
            )

            st.plotly_chart(fig, use_container_width=True)
