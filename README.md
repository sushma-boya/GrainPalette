# 🌾 GrainPalette: A Deep Learning Odyssey in Rice Type Classification

GrainPalette is a deep learning-powered web application designed to classify rice grain images into five distinct varieties. Using transfer learning, the system delivers high-accuracy predictions from user-uploaded images through an intuitive and responsive web interface.

## 🎥 Demo

▶️ **Demo Video:**  
https://drive.google.com/file/d/1Kq8apZpv0F30F-kIhxNCm5KnhcoWCtfr/view?usp=drive_link

### How It Works

1. Upload an image of a rice grain.
2. The trained deep learning model processes the image.
3. The application predicts one of the following rice types:

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

---

## ✨ Features

- 🎯 **High Accuracy** – Achieved approximately 99% accuracy using transfer learning.
- 🌾 **Five Rice Types** – Supports classification of five distinct rice varieties.
- ⚡ **Real-Time Prediction** – Upload an image and receive predictions within seconds.
- 🌐 **Web-Based Interface** – Built using Flask with an interactive user interface.
- 📱 **Responsive Design** – Designed to work across desktop and mobile devices.
- 🧠 **Deep Learning Powered** – Uses a pretrained CNN model for image classification.

---

## 🧠 Supported Rice Classes

| Rice Type | Classification |
|-----------|----------------|
| Arborio | Supported |
| Basmati | Supported |
| Ipsala | Supported |
| Jasmine | Supported |
| Karacadag | Supported |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Deep Learning | TensorFlow, Keras |
| Transfer Learning | Pretrained CNN Model |
| Web Framework | Flask |
| Image Processing | OpenCV, NumPy |
| Frontend | HTML, CSS, Bootstrap |

---

## 📁 Project Structure

```text
GrainPalette/
│
├── app.py
├── rice_model.h5
├── requirements.txt
├── README.md
│
├── static/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── results.html
│   └── details.html
│
└── demo_video/
```
## ⚙️ Installation

Prerequisites
Python 3.8 or above
Git
4GB+ RAM recommended
GPU optional for model training

## ▶️ Run the Project Locally

1. Clone the Repository
git clone https://github.com/sushma-boya/GrainPalette.git
2. Navigate to the Project Directory
cd GrainPalette
3. Create a Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Run the Flask Application
python app.py
6. Open the Application

Visit:
http://127.0.0.1:5000

## 🧠 Model Architecture
Base Model: VGG16 pretrained on ImageNet
Input Size: 224 × 224 RGB
Transfer Learning: Pretrained convolutional layers with custom classification layers
Loss Function: Categorical Crossentropy
Optimizer: Adam
Output Classes: 5

The model classifies uploaded rice grain images into one of the five supported categories.

## 📈 Model Performance

Metric	Performance
Training Accuracy	99.2%
Validation Accuracy	98.5%
Inference Time	< 200ms
🚀 Future Enhancements
🎥 Live camera feed support
📱 Mobile application interface
🧠 Advanced rice quality detection
🌾 Broken grain detection
🌐 Multi-language support
📊 Prediction confidence visualization

## 🤝 Contributing
Contributions are welcome!

Fork the repository.
Create a new branch.
Make your changes.
Commit your changes with a clear message.
Push the branch.
Open a Pull Request.

## 👩‍💻 Author

Sushma Boya

Developer of GrainPalette, a deep learning application for rice grain image classification.

🔗 GitHub: https://github.com/sushma-boya

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for more information.

⭐ If you found this project useful, consider giving the repository a star!

Thank you for exploring GrainPalette! 🌾
