import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

app = Flask(__name__)  # Create Flask app
app.config['TEMPLATES_AUTO_RELOAD'] = True
model = load_model('C:/Users/deepa/Downloads/Heart_Disease_Prediction_Using_ECG_Images-main/Heart_Disease_Prediction_Using_ECG_Images-main/flask/ECG.h5')

heart_conditions = {
    "Normal": {
        "description": "No abnormalities detected in heart function.",
        "symptoms": "None; heart functions are within normal ranges.",
        "risk_factors": "Maintain a healthy lifestyle to prevent potential heart issues.",
        "lifestyle_advice": "Continue regular exercise, balanced diet, and routine checkups."
    },
    "Left Bundle Branch Block": {
        "description": "A blockage in the left bundle branch of the heart’s electrical conduction system.",
        "symptoms": "Often asymptomatic, but can include fainting, dizziness, or palpitations in some cases.",
        "risk_factors": "High blood pressure, heart disease, or congenital heart defects.",
        "lifestyle_advice": "Manage blood pressure, avoid smoking, and maintain regular exercise."
    },
    "Right Bundle Branch Block": {
        "description": "A blockage in the right bundle branch of the heart’s conduction system.",
        "symptoms": "Typically asymptomatic, but may cause fatigue or fainting in some cases.",
        "risk_factors": "Can be present in healthy individuals or due to underlying heart conditions.",
        "lifestyle_advice": "Stay active, avoid smoking, and manage heart health under medical supervision."
    },
    "Premature Atrial Contraction": {
        "description": "Early heartbeats originating in the atria.",
        "symptoms": "Palpitations, skipped heartbeats, or fluttering sensation in the chest.",
        "risk_factors": "Stress, caffeine, tobacco, alcohol, or electrolyte imbalance.",
        "lifestyle_advice": "Reduce caffeine and alcohol intake, manage stress, and stay hydrated."
    },
    "Premature Ventricular Contraction": {
        "description": "Extra heartbeats that start in the ventricles and disrupt regular heart rhythm.",
        "symptoms": "Fluttering, skipped beats, or a pounding sensation in the chest.",
        "risk_factors": "High blood pressure, heart disease, stress, caffeine, or electrolyte imbalance.",
        "lifestyle_advice": "Monitor stress levels, reduce caffeine intake, and maintain heart health."
    },
    "Ventricular Fibrillation": {
        "description": "A severe arrhythmia where ventricles quiver instead of pumping effectively.",
        "symptoms": "Sudden collapse, loss of consciousness, and lack of pulse; life-threatening emergency.",
        "risk_factors": "Heart attack, electrolyte imbalance, or severe heart disease.",
        "lifestyle_advice": "This is a critical condition requiring immediate medical attention and possibly lifestyle adjustments under medical supervision."
    }
}

@app.route("/")
def about():
    return render_template("home.html")

@app.route("/about")
def home():
    return render_template("home.html")

@app.route("/info")
def information():
    return render_template("information.html")

@app.route("/upload")
def test():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def upload():
    if request.method == 'POST':
        f = request.files['file']  # Get uploaded file
        basepath = os.path.dirname('__file__')  # Get directory of the file
        upload_path = os.path.join(basepath, "uploads")
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        filepath = os.path.join(upload_path, f.filename)
        f.save(filepath)
        
        img = image.load_img(filepath, target_size=(64, 64))  # Load image
        x = image.img_to_array(img)  # Convert image to array
        x = np.expand_dims(x, axis=0)  # Expand dimensions
        
        pred = model.predict(x)  # Predict the class
        y_pred = np.argmax(pred)
        index = ['Left Bundle Branch Block', 'Normal', 'Premature Atrial Contraction',
                 'Premature Ventricular Contractions', 'Right Bundle Branch Block', 'Ventricular Fibrillation']
        result = str(index[y_pred])

        # Get heart condition details
        condition_details = heart_conditions.get(result, heart_conditions["Normal"])


        # Return condition type along with other details
        return jsonify({
            'condition_type': result,
            'description': condition_details["description"],
            'symptoms': condition_details["symptoms"],
            'risk_factors': condition_details["risk_factors"],
            'lifestyle_advice': condition_details["lifestyle_advice"]
        })

if __name__ == "__main__":
    app.run(debug=True)
