# Ink2Code 

Ink2Code is an AI-powered tool that converts **hand-drawn UI sketches into working frontend code**.

Users can upload a sketch of a user interface, and the system automatically detects UI components and generates **HTML, React, and Flutter code**, along with a **live preview of the generated UI**.

---

##  Features

* Upload hand-drawn UI sketches
* Detect UI components using OpenCV
* Draw bounding boxes around detected elements
* Classify UI elements (Input Field, Button, Container)
* Generate code in multiple frameworks:

  * HTML
  * React
  * Flutter
* Live UI preview inside the application
* Download generated code

---

##  How It Works

The system follows this pipeline:

Sketch → UI Detection → Code Generation → Live UI Preview

1. The user uploads a hand-drawn UI sketch.
2. OpenCV detects UI components using contour detection.
3. The system classifies detected components.
4. Code is generated automatically.
5. A live preview renders the generated UI.

---

##  Tech Stack

Frontend

* HTML
* TailwindCSS

Backend

* Python
* Flask

AI / Computer Vision

* OpenCV

---

##  Project Structure

```
Ink2Code
│
├── app.py
├── detector.py
├── generator.py
│
├── templates
│   └── index.html
│
├── static
│
├── uploads
│
└── README.md
```

---

##  Future Improvements

* Train a deep learning model for better UI recognition
* Export full React or Flutter projects
* Integrate with design tools like Figma
* Support more UI components

---

## Setup Instructions

git clone <repo link>

cd Ink2Code

pip install -r requirements.txt

python app.py

---

##  Author

Team : SketchStack
Arpan Manna
A Shivamani
A Abhiram

HackFusion 2K26 Project

## Point of contact:

arpanmanna822@gmail.com

