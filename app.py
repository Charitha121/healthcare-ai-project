from flask import Flask, render_template, request
import os

app = Flask(__name__)

def analyze_input(user_input, age):
    user_input = user_input.lower()

    advice = ""

    # Age-based advice
    if age < 12:
        advice = "👶 Child: Consult pediatrician for safe treatment."
    elif age > 60:
        advice = "👴 Senior: Take extra care and consult doctor early."
    else:
        advice = "🧑 Adult: Follow precautions and monitor symptoms."

    # Symptoms logic
    if "fever" in user_input and "cough" in user_input:
        return {
            "disease": "Flu / Viral Infection",
            "precautions": "Rest, warm fluids",
            "medication": "Paracetamol, Cough Syrup",
            "ayurvedic": "Tulsi tea, Ginger",
            "doctor": "General Physician",
            "advice": advice
        }

    elif "headache" in user_input:
        return {
            "disease": "Migraine / Stress",
            "precautions": "Rest, avoid screens",
            "medication": "Paracetamol",
            "ayurvedic": "Peppermint oil",
            "doctor": "Neurologist",
            "advice": advice
        }

    elif "stomach pain" in user_input:
        return {
            "disease": "Gastritis",
            "precautions": "Avoid spicy food",
            "medication": "Antacids",
            "ayurvedic": "Jeera water",
            "doctor": "Gastroenterologist",
            "advice": advice
        }

    elif "chest pain" in user_input:
        return {
            "disease": "Heart Issue",
            "precautions": "Emergency care",
            "medication": "Immediate hospital visit",
            "ayurvedic": "Not recommended",
            "doctor": "Cardiologist",
            "advice": advice
        }

    else:
        return {
            "disease": "Unknown",
            "precautions": "Consult doctor",
            "medication": "Not specified",
            "ayurvedic": "Not specified",
            "doctor": "General Physician",
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