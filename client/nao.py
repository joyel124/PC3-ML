# coding=utf-8
from naoqi import ALProxy
import json
import urllib2
import time

ROBOT_IP = "127.0.0.1"
API_URL = "http://192.168.1.4:5000/predecir"
PORT = 9559

# Inicializar proxies
tts = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
motion = ALProxy("ALMotion", ROBOT_IP, PORT)
posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

# Despierta al robot
motion.wakeUp()
posture.goToPosture("StandInit", 0.5)

def ask_and_validate(prompt_text, opciones_validas=None, tipo="str", conversion=None):
    while True:
        tts.say(prompt_text)
        print(prompt_text)
        respuesta = raw_input("> ").strip().lower()

        if opciones_validas:
            if respuesta in opciones_validas:
                return conversion[respuesta] if conversion else respuesta
            else:
                print("❌ Respuesta inválida. Intenta de nuevo.")
        else:
            try:
                if tipo == "float":
                    valor = float(respuesta)
                    if valor < 0:
                        raise ValueError
                    return valor
                elif tipo == "int":
                    valor = int(respuesta)
                    if valor < 0:
                        raise ValueError
                    return valor
            except ValueError:
                print("❌ Valor no válido. Intenta de nuevo.")

# Saludo
tts.say("Hola. Vamos a evaluar tu riesgo de diabetes.")
time.sleep(1)

# Preguntas con validación
gender = ask_and_validate(
    "¿Eres hombre o mujer? (hombre/mujer)",
    opciones_validas=["hombre", "mujer"],
    conversion={"hombre": "Male", "mujer": "Female"}
)

age = ask_and_validate("¿Cuál es tu edad?", tipo="float")

hypertension = ask_and_validate(
    "¿Tienes hipertensión? (sí/no)",
    opciones_validas=["si", "sí", "no"],
    conversion={"si": 1, "sí": 1, "no": 0}
)

heart_disease = ask_and_validate(
    "¿Tienes alguna enfermedad del corazón? (sí/no)",
    opciones_validas=["si", "sí", "no"],
    conversion={"si": 1, "sí": 1, "no": 0}
)

smoking_history = ask_and_validate(
    "¿Cuál es tu historial de tabaquismo? (nunca/actual/anterior/no sé)",
    opciones_validas=["nunca", "actual", "anterior", "no se", "no sé"],
    conversion={
        "nunca": "never",
        "actual": "current",
        "anterior": "former",
        "no se": "No Info",
        "no sé": "No Info"
    }
)

bmi = ask_and_validate("¿Cuál es tu índice de masa corporal (BMI)?", tipo="float")
hba1c = ask_and_validate("¿Cuál es tu nivel de hemoglobina glicosilada (HbA1c)?", tipo="float")
glucosa = ask_and_validate("¿Cuál es tu nivel de glucosa en sangre?", tipo="float")

# Construir entrada
entrada = {
    "gender": gender,
    "age": age,
    "hypertension": hypertension,
    "heart_disease": heart_disease,
    "smoking_history": smoking_history,
    "bmi": bmi,
    "HbA1c_level": hba1c,
    "blood_glucose_level": glucosa
}

# Enviar a la API
try:
    req = urllib2.Request(API_URL)
    req.add_header("Content-Type", "application/json")
    response = urllib2.urlopen(req, json.dumps(entrada))
    response_json = json.loads(response.read())

    resultado = response_json["resultado"]
    probabilidad = response_json["probabilidad"]

    print("Predicción:", resultado, "| Probabilidad:", probabilidad)

    if resultado == 1:
        mensaje = "¡Tienes un alto riesgo de diabetes!"
    else:
        mensaje = "No se detecta riesgo de diabetes."

    tts.say(mensaje)
    print(mensaje)
    time.sleep(5)

    motion.rest()

except Exception as e:
    print("❌ Error:", e)
