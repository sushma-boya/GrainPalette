
# 🌾 GrainPalette: A Deep Learning Odyssey in Rice Type Classification

![Rice Fields](static/rice_fields.jpg)

GrainPalette is a deep learning-powered web app that classifies rice grain images into 5 unique types using Transfer Learning and TensorFlow. Just upload a picture and get an instant prediction of the rice type. Clean UI. High accuracy. 

---
#Demo video link
https://drive.google.com/file/d/1Kq8apZpv0F30F-kIhxNCm5KnhcoWCtfr/view?usp=drive_link
## Demo

➡️ Upload an image of rice grain  
✅ Model classifies it into one of the following types:

- Arborio
- Basmati
- Ipsala
- Jasmine
- Karacadag

---

##  Features

- 🔥 Transfer learning with MobileNetV2
- 📈 Achieves 97%+ accuracy on test data
- 🌐 Web app powered by Flask
- ⚡ Clean responsive UI (HTML5 + Bootstrap)
- 📷 Image upload and live prediction

---

## Tech Stack

| Layer             | Tech Used              |
|------------------|------------------------|
| Deep Learning    | TensorFlow, Keras      |
| Transfer Learning| MobileNetV2 (TF Hub)   |
| Web Framework    | Flask                  |
| Image Processing | OpenCV, NumPy          |
| Frontend         | HTML, CSS, Bootstrap   |

---

#Project Structure
Rice_type_detection/
├── app.py
├── rice_model.keras
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── details.html
│   └── results.html
├── static/
│   ├── rice_banner.jpg
│   ├── arborio_sample.jpg
│   └── basmati_sacks.jpg
├── .gitignore
└── README.md

##  Run This Project Locally

1. Clone this repo:git clone https://github.com/sushma-boya/GrainPalette.git
cd GrainPalette

2. Create virtual environment and activate:
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
python app.py

5. Open browser and go to: " http://127.0.0.1:5000 "

#Contact
📧 info@grainpalette.ai
📞 +91 98765 43210

Made by Sushma Naidu

# License
This project is licensed under the MIT License — see the LICENSE file for details.

# GrainPalette
 5d21522952b132dc0c6c008e79a4285362e528a0
