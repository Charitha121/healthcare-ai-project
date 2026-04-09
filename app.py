from flask import Flask, render_template, request
import os

app = Flask(__name__)


def analyze_input(user_input, age):
    user_input = user_input.lower()

    # Default values
    disease = "Unknown"
    precautions = "Consult doctor"
    medication = "Not specified"
    ayurvedic = "Not specified"
    doctor = "General Physician"
    risk = "Low"
    diet = "Maintain balanced diet"

    # 🧠 DIABETES
    if "diabetes" in user_input or "sugar" in user_input:
        disease = "Diabetes"
        precautions = "Monitor sugar levels, regular exercise"
        medication = "Metformin / Insulin (doctor prescribed)"
        ayurvedic = "Karela juice, Fenugreek seeds"
        doctor = "Endocrinologist"
        diet = "Low sugar diet, whole grains, leafy vegetables"
        risk = "High" if age > 50 else "Moderate"

    # 🧠 BLOOD PRESSURE
    elif "bp" in user_input or "blood pressure" in user_input:
        disease = "Hypertension"
        precautions = "Reduce salt, avoid stress"
        medication = "Amlodipine / BP tablets"
        ayurvedic = "Garlic, Ashwagandha"
        doctor = "Cardiologist"
        diet = "Low salt diet, fruits, oats"
        risk = "High" if age > 45 else "Moderate"

    # 🧠 WEIGHT LOSS
    elif "weight loss" in user_input:
        disease = "Unintentional Weight Loss"
        precautions = "Check nutrition, regular meals"
        medication = "Vitamin supplements"
        ayurvedic = "Ashwagandha, Shatavari"
        doctor = "Nutritionist"
        diet = "High protein diet, nuts, milk, eggs"
        risk = "High" if age > 50 else "Moderate"

    # 🧠 SKIN
    elif "skin" in user_input or "rash" in user_input:
        disease = "Skin Infection / Allergy"
        precautions = "Maintain hygiene, avoid allergens"
        medication = "Antifungal / Anti-allergy meds"
        ayurvedic = "Neem, Aloe vera"
        doctor = "Dermatologist"
        diet = "Vitamin C foods, fruits, water"
        risk = "Low"

    # 🧠 FEVER
    elif "fever" in user_input:
        disease = "Viral Fever"
        precautions = "Rest, hydration"
        medication = "Paracetamol"
        ayurvedic = "Tulsi, Ginger tea"
        doctor = "General Physician"
        diet = "Soups, fruits, light food"
        risk = "Moderate" if age > 50 else "Low"

    # 🧠 CHEST PAIN
    elif "chest pain" in user_input:
        disease = "Possible Heart Issue"
        precautions = "Emergency attention required"
        medication = "Immediate hospital visit"
        ayurvedic = "Not recommended"
        doctor = "Cardiologist"
        diet = "Low fat diet"
        risk = "High"

    # 🧠 STOMACH
    elif "stomach" in user_input:
        disease = "Gastritis / Digestive Issue"
        precautions = "Avoid spicy food"
        medication = "Antacids"
        ayurvedic = "Jeera water"
        doctor = "Gastroenterologist"
        diet = "Curd, rice, light food"
        risk = "Low"

    # 🧠 HEADACHE
    elif "headache" in user_input:
        if age > 60:
            disease = "BP-related Headache"
            precautions = "Monitor BP, avoid stress"
            medication = "Doctor prescribed medication"
            ayurvedic = "Brahmi"
            doctor = "Neurologist / Cardiologist"
            diet = "Low salt diet"
            risk = "High"
        else:
            disease = "Migraine / Stress"
            precautions = "Rest, avoid screens"
            medication = "Paracetamol / Ibuprofen"
            ayurvedic = "Peppermint oil"
            doctor = "Neurologist"
            diet = "Hydration, fruits"
            risk = "Low"

    # 🎯 AGE BASED ADVICE
    if age < 18:
        advice = "👶 Child: Extra care and proper nutrition needed."
    elif age < 60:
        advice = "🧑 Adult: Maintain healthy lifestyle."
    else:
        advice = "👴 Senior: High risk, regular checkups needed."

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