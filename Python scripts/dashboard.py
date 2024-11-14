import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load Edge Impulse model (TensorFlow Lite)
MODEL_PATH = "jeffrey.lite"
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

# Debug: Print output details to understand the structure
st.write("Output details:")
st.write(output_details)

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
        predicted_age = np.argmax(output)   # Adding 1 because the class indices start from 0
        confidence = output[np.argmax(output)]  # The confidence of the prediction

        # Map the output to human-readable age values (1-19)
        age_labels = [str(i) for i in range(0, 21)]  # Age labels from 1 to 19
        age_probabilities = {age_labels[i]: output[i] for i in range(len(output))}

        # Sort age probabilities in descending order (optional, to display the top prediction)
        sorted_ages = sorted(age_probabilities.items(), key=lambda x: x[1], reverse=True)

        return predicted_age, confidence, sorted_ages
    except IndexError as e:
        st.error(f"Index error in retrieving model outputs: {e}")
        return None, None, None
    except Exception as e:
        st.error(f"Unexpected error during inference: {e}")
        return None, None, None

# Streamlit App Layout
st.title("Watercress Age Prediction")

st.write("Upload an image of Watercress, and the model will predict its age (1-19).")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the uploaded image
    image = load_image(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    st.write("Running model...")
    
    # Run inference
    try:
        predicted_age, confidence, sorted_ages = run_inference(image)
        
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
