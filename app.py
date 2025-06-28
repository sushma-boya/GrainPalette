from flask import Flask, render_template, request
import numpy as np
import cv2
import os
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model("rice_model.keras")  # Make sure this file is in root folder

# Class label mapping
class_labels = {
    0: 'Arborio',
    1: 'Basmati',
    2: 'Ipsala',
    3: 'Jasmine',
    4: 'Karacadag'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/result', methods=['POST'])
def result():
    if 'image' not in request.files:
        return "No image uploaded", 400

    f = request.files['image']
    if f.filename == '':
        return "No file selected", 400

    filepath = os.path.join('static', f.filename)
    f.save(filepath)

    # Image preprocessing
    img = cv2.imread(filepath)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    pred = model.predict(img)
    pred_class = np.argmax(pred)
    prediction = class_labels[pred_class]

    return render_template('results.html', prediction_text=f"Predicted Rice Type: {prediction}", img_path=filepath)

if __name__ == "__main__":
    app.run(debug=True)
