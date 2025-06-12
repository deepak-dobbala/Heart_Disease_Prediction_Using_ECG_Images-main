## ECG Image-Based Heartbeat Classification for Arrhythmia Detection

**Live Demo:** [heart-disease-app.onrender.com](https://heart-disease-app.onrender.com)
**GitHub Repository:** [github.com/your-username/heart-disease-prediction-ecg](https://github.com/your-username/heart-disease-prediction-ecg)

---

### Introduction

Cardiovascular diseases (CVDs) are the leading cause of death worldwide, accounting for over 17.7 million deaths (31% of all deaths) in 2017, with more than 75% occurring in low- and middle-income countries. Arrhythmia—irregular heart rhythm—is a significant CVD subtype that can range from benign skipped beats to life-threatening ventricular fibrillation.

In this project, we developed a web application that classifies ECG images into seven categories (normal and six arrhythmia types) using a deep Convolutional Neural Network (CNN). Users can upload an ECG image via the Flask-based interface, and receive an instant prediction and detailed information about the diagnosed condition.

---

### Key Features

* **High Accuracy:** Achieves \~96% classification accuracy across seven categories.
* **Real-Time Inference:** Users upload an image and get instant predictions.
* **Detailed Insights:** For each detected condition, the app provides descriptions, symptoms, risk factors, and lifestyle advice.
* **Containerized Deployment:** Dockerized and deployed on Render for seamless scaling.

---

### Architecture

1. **Data Preprocessing:** Grayscale ECG images are augmented using Keras's `ImageDataGenerator` (rotations, shifts, flips, zooms).
2. **Model:** A sequential 2D CNN with multiple convolutional, pooling, dropout, and dense layers, compiled with the Adam optimizer and categorical cross-entropy loss.
3. **Backend:** Flask serves the web UI and handles file uploads, model loading, and prediction.
4. **Containerization:** Docker builds the app into an image, exposing port 5000.
5. **Deployment:** Render pulls the Docker Hub image and hosts the service at a public URL.

---

### Getting Started

#### Prerequisites

* Docker
* Docker Hub account (image: `deepakdobbal28/heart-disease-pred-app:1.0`)

#### Local Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/heart-disease-prediction-ecg.git
   cd heart-disease-prediction-ecg
   ```
2. **Build the Docker image**

   ```bash
   docker build -t heart-disease-app:local .
   ```
3. **Run the container**

   ```bash
   docker run -p 5000:5000 heart-disease-app:local
   ```
4. **Visit** `http://localhost:5000` in your browser.

#### Using the Live Demo

* Navigate to the [live app](https://heart-disease-app.onrender.com).
* Upload an ECG image on the **Predict** page.
* View diagnosis and condition details.

---

### Future Work

* Integrate hyperparameter optimization for improved accuracy.
* Expand to detect additional cardiac conditions and multi-lead ECG signals.
* Implement user authentication and result history tracking.

---

### License

This project is released under the MIT License.
