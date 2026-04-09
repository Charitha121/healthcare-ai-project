from flask import Flask, render_template, request

app = Flask(__name__)

def analyze_input(user_input):
    user_input = user_input.lower()

    # Fever + Cough
    if "fever" in user_input and "cough" in user_input:
        return {
            "disease": "Flu / Viral Infection",
            "precautions": "Take rest, drink warm fluids, avoid cold items",
            "medication": "Paracetamol, Cough Syrup",
            "ayurvedic": "Tulsi tea, Ginger tea, Honey"
        }

    # Fever + Body Pain
    elif "fever" in user_input and "body pain" in user_input:
        return {
            "disease": "Dengue / Viral Fever",
            "precautions": "Drink fluids, take rest, monitor temperature",
            "medication": "Paracetamol (avoid self-medication)",
            "ayurvedic": "Papaya leaf juice, Giloy"
        }

    # Headache
    elif "headache" in user_input:
        return {
            "disease": "Migraine / Stress",
            "precautions": "Avoid screen, rest in dark room, hydrate",
            "medication": "Paracetamol",
            "ayurvedic": "Peppermint oil, Brahmi, Ashwagandha"
        }

    # Stomach Pain
    elif "stomach pain" in user_input:
        return {
            "disease": "Gastritis / Food Poisoning",
            "precautions": "Eat light food, avoid spicy/oily items",
            "medication": "Antacids, ORS",
            "ayurvedic": "Jeera water, Ajwain, Ginger"
        }

    # Leg Pain
    elif "leg pain" in user_input:
        return {
            "disease": "Muscle Strain / Calcium Deficiency",
            "precautions": "Take rest, apply hot/cold compress",
            "medication": "Pain relief gel, Calcium tablets",
            "ayurvedic": "Turmeric milk, Ashwagandha"
        }

    # Chest Pain
    elif "chest pain" in user_input:
        return {
            "disease": "Possible Heart Issue",
            "precautions": "Seek immediate medical help",
            "medication": "Emergency consultation required",
            "ayurvedic": "Not recommended in emergency"
        }

    # Breathing Problem
    elif "breathing problem" in user_input:
        return {
            "disease": "Asthma / Lung Issue",
            "precautions": "Avoid dust, take fresh air",
            "medication": "Inhaler (as prescribed)",
            "ayurvedic": "Tulsi, Steam inhalation"
        }

    # Vomiting + Fever
    elif "vomiting" in user_input and "fever" in user_input:
        return {
            "disease": "Food Infection / Viral Fever",
            "precautions": "Stay hydrated, take rest",
            "medication": "ORS, Anti-vomiting tablets",
            "ayurvedic": "Ginger tea, Lemon water"
        }

    # Default
    else:
        return {
            "disease": "Unknown",
            "precautions": "Consult a doctor",
            "medication": "Not specified",
            "ayurvedic": "Not specified"
        }


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['symptoms']
    result = analyze_input(user_input)

    return f"""
    <html>
    <body style="text-align:center;font-family:Arial;background:#f4f6f9;">
        <h1>🧠 AI Healthcare Diagnosis</h1>

        <p><b>Entered Symptoms:</b> {user_input}</p>

        <h3>🔍 Disease:</h3>
        <p>{result['disease']}</p>

        <h3>🛡️ Precautions:</h3>
        <p>{result['precautions']}</p>

        <h3>💊 Medication:</h3>
        <p>{result['medication']}</p>

        <h3>🌿 Ayurvedic Remedies:</h3>
        <p>{result['ayurvedic']}</p>

        <br><br>
        <a href="/" style="text-decoration:none;color:blue;">🔙 Go Back</a>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)