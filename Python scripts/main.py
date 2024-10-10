import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import matplotlib.pyplot as plt

# Load images and labels
def load_images_from_folder(folder):
    images = []
    labels = []
    if not os.path.exists(folder):
        raise FileNotFoundError(f"The folder {folder} does not exist.")
    for subfolder in os.listdir(folder):
        subfolder_path = os.path.join(folder, subfolder)
        if os.path.isdir(subfolder_path):
            # Skip the 'val' folder
            if subfolder == 'val':
                continue
            # Extract the label from the subfolder name (e.g., "Dag0" -> 0)
            label = int(subfolder.replace('Dag', ''))
            for filename in os.listdir(subfolder_path):
                img_path = os.path.join(subfolder_path, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    # Resize the image to a fixed size (e.g., 128x128)
                    img = cv2.resize(img, (128, 128))
                    images.append(img)
                    labels.append(label)
    return np.array(images), np.array(labels)

# Path to your folder containing images
folder_path = os.path.join(os.path.dirname(__file__), 'Images', 'Images')

# Load the dataset
X, y = load_images_from_folder(folder_path)

# Normalize the image data (scale pixel values to [0, 1])
X = X / 255.0

# Split the dataset into training and testing sets (e.g., 80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Data augmentation
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
])

# Build the CNN model
model = models.Sequential([
    data_augmentation,
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),  # Add dropout for regularization
    layers.Dense(1, activation='linear')  # Output layer for regression (age prediction)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Callbacks for early stopping and learning rate reduction
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
reduce_lr = callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=0.0001)

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test),
                    callbacks=[early_stopping, reduce_lr])

# Plot the training and validation loss over epochs
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Evaluate the model on the test data
test_loss, test_mae = model.evaluate(X_test, y_test)
print(f"Test Mean Absolute Error: {test_mae}")

# Extract features using the trained model (excluding the final layer)
feature_extractor = models.Model(inputs=model.input, outputs=model.layers[-3].output)
features = feature_extractor.predict(X)

# Apply t-SNE to reduce the dimensionality of the features to 2D
tsne = TSNE(n_components=2, random_state=42)
features_2d = tsne.fit_transform(features)

# Plot the 2D features with different colors for each day
plt.figure(figsize=(10, 8))
for day in np.unique(y):
    indices = np.where(y == day)
    plt.scatter(features_2d[indices, 0], features_2d[indices, 1], label=f'Day {day}')
plt.title('t-SNE Visualization of Image Features')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend()
plt.show()

# Predict the age of a new watercress image
def predict_image_age(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"The image file {image_path} does not exist or cannot be opened.")
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    predicted_age = model.predict(img)[0][0]
    return predicted_age

# Example predictions
image_paths = [
    os.path.join(folder_path, 'Dag4', 'PXL_20240930_141852018.jpg'),
    os.path.join(folder_path, 'Dag4', 'PXL_20241003_045221202.jpg'),
    os.path.join(folder_path, 'Dag10', 'PXL_20241009_173052717.jpg'),
    os.path.join(folder_path, 'Dag13', 'PXL_20241009_173146411.jpg'),
    os.path.join(folder_path, 'val', '1.jpg'),
    os.path.join(folder_path, 'val', '7.jpg'),
    os.path.join(folder_path, 'val', '13.jpg')
]

for image_path in image_paths:
    predicted_age = predict_image_age(image_path)
    print(f"Predicted Age: {predicted_age} days")