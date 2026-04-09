from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 🤖 ML-LIKE SYMPTOM SCORING MODEL
def analyze_input(user_input, age):
    user_input = user_input.lower()

    symptoms = user_input.split()

    # Disease scoring
    scores = {
        "Diabetes": 0,
        "Hypertension": 0,
        "Gastritis": 0,
        "Migraine": 0,
        "Skin Infection": 0,
        "Heart Issue": 0
    }

    # 🧠 Keyword mapping (ML-like)
    for word in symptoms:
        if word in ["sugar", "diabetes", "urination"]:
            scores["Diabetes"] += 2

        if word in ["bp", "pressure", "stress"]:
            scores["Hypertension"] += 2

        if word in ["stomach", "pain", "gas"]:
            scores["Gastritis"] += 2

        if word in ["headache", "migraine"]:
            scores["Migraine"] += 2

        if word in ["skin", "rash", "itching"]:
            scores["Skin Infection"] += 2

        if word in ["chest", "pain"]:
            scores["Heart Issue"] += 3

    # Get best disease
    disease = max(scores, key=scores.get)

    # 🎯 Default values
    precautions = ""
    medication = ""
    ayurvedic = ""
    doctor = ""
    risk = "Low"
    diet = ""

    # 🧠 Assign details
    if disease == "Diabetes":
        precautions = "Monitor sugar levels, exercise"
        medication = "Metformin / Insulin"
        ayurvedic = "Karela juice"
        doctor = "Endocrinologist"
        diet = "Low sugar diet"
        risk = "High" if age > 50 else "Moderate"

    elif disease == "Hypertension":
        precautions = "Reduce salt, avoid stress"
        medication = "BP tablets"
        ayurvedic = "Garlic"
        doctor = "Cardiologist"
        diet = "Low salt diet"
        risk = "High" if age > 45 else "Moderate"

    elif disease == "Gastritis":
        precautions = "Avoid spicy food"
        medication = "Antacids"
        ayurvedic = "Jeera water"
        doctor = "Gastroenterologist"
        diet = "Light food"
        risk = "Low"

    elif disease == "Migraine":
        precautions = "Rest, avoid screens"
        medication = "Paracetamol"
        ayurvedic = "Peppermint oil"
        doctor = "Neurologist"
        diet = "Hydration"
        risk = "Low"

    elif disease == "Skin Infection":
        precautions = "Maintain hygiene"
        medication = "Antifungal"
        ayurvedic = "Neem"
        doctor = "Dermatologist"
        diet = "Fruits, water"
        risk = "Low"

    elif disease == "Heart Issue":
        precautions = "Emergency care"
        medication = "Immediate hospital visit"
        ayurvedic = "Not recommended"
        doctor = "Cardiologist"
        diet = "Low fat diet"
        risk = "High"

    # 🎯 Age advice
    if age < 18:
        advice = "👶 Child: Consult pediatrician"
    elif age < 60:
        advice = "🧑 Adult: Maintain healthy lifestyle"
    else:
        advice = "👴 Senior: High risk, regular checkups needed"

    return {
        "disease": disease,
        "precautions": precautions,
        "medication": medication,
        "ayurvedic": ayurvedic,
        "doctor": doctor,
        "risk": risk,
        "diet": diet,
        "advice": advice
    }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['symptoms']
    age = int(request.form['age'])

    result = analyze_input(user_input, age)

    return render_template("result.html",
                           user_input=user_input,
                           age=age,
                           result=result)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)