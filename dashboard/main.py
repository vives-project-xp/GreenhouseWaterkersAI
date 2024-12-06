import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import plotly.graph_objects as go
import os
from typing import List, Tuple, Dict, Optional
import io

class WatercressModel:
    def __init__(self, model_path: str):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    def preprocess_image(self, image: Image.Image) -> np.ndarray:
        """Preprocess image for model input."""
        input_shape = self.input_details[0]['shape']
        image = image.resize((input_shape[1], input_shape[2]))
        image_array = np.array(image, dtype=np.float32) / 255.0
        return np.expand_dims(image_array, axis=0)
    
    def predict(self, image: Image.Image) -> Tuple[int, float, List[Tuple[str, float]], Dict[str, float]]:
        """Run inference on an image."""
        processed_image = self.preprocess_image(image)
        self.interpreter.set_tensor(self.input_details[0]['index'], processed_image)
        self.interpreter.invoke()
        output = self.interpreter.get_tensor(self.output_details[0]['index'])[0]
        
        predicted_age = np.argmax(output)
        confidence = output[predicted_age]
        
        age_labels = [str(i) for i in range(21)]
        age_probabilities = {label: output[i] for i, label in enumerate(age_labels)}
        sorted_ages = sorted(age_probabilities.items(), key=lambda x: x[1], reverse=True)
        
        return predicted_age, confidence, sorted_ages, age_probabilities

class Dashboard:
    def __init__(self):
        st.set_page_config(layout="wide")
        self.model = WatercressModel("model.lite")
        
    def load_image(self, image_path: str) -> Image.Image:
        """Load and convert image to RGB."""
        return Image.open(image_path).convert("RGB")
    
    def create_prediction_plot(self, age_probabilities: Dict[str, float]) -> go.Figure:
        """Create confidence plot."""
        age_labels = [str(i) for i in range(21)]
        prob_values = [age_probabilities[label] for label in age_labels]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=age_labels,
            y=prob_values,
            marker=dict(color='skyblue'),
            name="Confidence"
        ))
        fig.update_layout(
            title="Age Prediction Confidence",
            xaxis_title="Age",
            yaxis_title="Confidence",
            xaxis=dict(tickmode="linear"),
            template="plotly_white",
            height=300
        )
        return fig
    
    def sidebar(self) -> List[Image.Image]:
        """Create sidebar with image selection options."""
        st.sidebar.title("Image Selection")
        
        # File upload section
        uploaded_file = st.sidebar.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        
        # Example images section
        st.sidebar.markdown("---")
        st.sidebar.subheader("Select Images")
        
        selected_images = []
        example_folder = "example_images"
        image_files = [
            f for f in os.listdir(example_folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
        
        # Create a container for the image grid
        image_container = st.sidebar.container()
        col1, col2 = image_container.columns(2)
        
        # Display images in a grid with checkboxes
        for idx, image_file in enumerate(image_files):
            image_path = os.path.join(example_folder, image_file)
            image = self.load_image(image_path)
            
            current_col = col1 if idx % 2 == 0 else col2
            with current_col:
                st.image(image, use_container_width=True)
                if st.checkbox("Select", key=f"img_{idx}"):
                    selected_images.append(image)
        
        # Add uploaded file if present
        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            selected_images.append(image)
            
        return selected_images
    
    def display_predictions(self, images: List[Image.Image]):
        """Display images and their predictions."""
        for idx, image in enumerate(images):
            st.markdown(f"### Image {idx + 1}")
            
            img_col, plot_col = st.columns(2)
            
            with img_col:
                st.image(image, use_container_width=True)
                predicted_age, confidence, _, age_probabilities = self.model.predict(image)
                
                met_col1, met_col2 = st.columns(2)
                with met_col1:
                    st.metric("Predicted Age", predicted_age)
                with met_col2:
                    st.metric("Confidence", f"{confidence:.1%}")
            
            with plot_col:
                fig = self.create_prediction_plot(age_probabilities)
                st.plotly_chart(fig, use_container_width=True)
            
            st.markdown("---")
    
    def run(self):
        """Run the dashboard."""
        st.title("Watercress Age Prediction")
        
        # Get selected images from sidebar
        selected_images = self.sidebar()
        
        # Display predictions if images are selected
        if selected_images:
            self.display_predictions(selected_images)
        else:
            st.info("Please select one or more images from the sidebar to begin.")

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()