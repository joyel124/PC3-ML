from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Cargar modelo
modelo = joblib.load("modelo_diabetes_v2.pkl")

# Lista de columnas esperadas (según tu dataset)
columnas = [
    "gender", "age", "hypertension", "heart_disease",
    "smoking_history", "bmi", "HbA1c_level", "blood_glucose_level"
]

# One-hot encoding necesario para "gender" y "smoking_history"
categoricas = ["gender", "smoking_history"]

app = Flask(__name__)

@app.route("/predecir", methods=["POST"])
def predecir():
    datos = request.json
    entrada = pd.DataFrame([datos])

    # 🔧 Convertir columnas categóricas explícitamente a string
    for col in ["gender", "smoking_history"]:
        entrada[col] = entrada[col].astype(str)

    # Hacer la predicción
    prob = modelo.predict_proba(entrada)[0][1]
    resultado = int(prob >= 0.4)

    return jsonify({
        "resultado": resultado,
        "probabilidad": round(prob, 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
