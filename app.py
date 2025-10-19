import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename

# Import Keras utilities
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Initialize the Flask application
app = Flask(__name__)

# Define the path for uploaded images
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
# Ensure 'model.h5' is in the same directory as app.py
try:
    model = load_model('model.h5')
    print("* Model loaded successfully")
except Exception as e:
    print(f"* Error loading model: {e}")
    model = None

# Set your class names in alphabetical order to match Keras's default behavior
# 0 = NORMAL, 1 = PNEUMONIA
CLASS_NAMES = ['NORMAL', 'PNEUMONIA'] 


def preprocess_image(image_path, target_size=(150, 150)):
    """
    Preprocesses the image for the model.
    1. Loads the image
    2. Resizes it to (150, 150)
    3. Converts it to a NumPy array
    4. Adds a batch dimension (1, 150, 150, 3)
    5. Normalizes pixel values to [0, 1]
    """
    try:
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize
        return img_array
    except Exception as e:
        print(f"* Error in preprocessing image: {e}")
        return None

# Define the main route ('/')
@app.route('/', methods=['GET'])
def index():
    # Render the main page
    return render_template('index.html')

# Define the predict route ('/predict')
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', error="Model is not loaded. Please check server logs.")

    if 'file' not in request.files:
        return render_template('index.html', error="No file part")
        
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error="No selected file")

    if file:
        try:
            # Secure the filename
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure the uploads directory exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            # Save the file
            file.save(file_path)
            print(f"* File saved to: {file_path}")

            # Preprocess the image
            processed_image = preprocess_image(file_path)
            
            if processed_image is None:
                return render_template('index.html', error="Error processing image.")

            # Make a prediction
            prediction = model.predict(processed_image)
            print(f"* Raw prediction output: {prediction}")
            
            # For a binary classifier with a sigmoid activation, the output is a single value.
            # We use a threshold (0.5) to decide the class.
            score = prediction[0][0]
            if score > 0.5:
                # If score is high, it's class 1 (PNEUMONIA)
                predicted_class_name = CLASS_NAMES[1] 
            else:
                # If score is low, it's class 0 (NORMAL)
                predicted_class_name = CLASS_NAMES[0]
            
            print(f"* Prediction Score: {score}, Predicted Class: {predicted_class_name}")

            # Pass the prediction and image name to the template
            return render_template('index.html', 
                                   prediction=predicted_class_name,
                                   uploaded_image=filename)
                                   
        except Exception as e:
            print(f"* An error occurred during prediction: {e}")
            return render_template('index.html', error=f"An error occurred: {e}")

    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)