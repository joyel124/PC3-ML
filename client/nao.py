# coding=utf-8
from naoqi import ALProxy
import json
import urllib2
import time

ROBOT_IP = "127.0.0.1"
API_URL = "http://192.168.1.4:5000/predecir"
PORT = 9559

# Datos de entrada nuevos según el nuevo dataset
entrada = {
  "gender": "Male",
  "age": 76.0,
  "hypertension": 1,
  "heart_disease": 1,
  "smoking_history": "current",
  "bmi": 20.14,
  "HbA1c_level": 4.8,
  "blood_glucose_level": 155
}

try:
    req = urllib2.Request(API_URL)
    req.add_header("Content-Type", "application/json")
    response = urllib2.urlopen(req, json.dumps(entrada))
    response_json = json.loads(response.read())

    resultado = response_json["resultado"]
    probabilidad = response_json["probabilidad"]

    print("Predicción:", resultado, "| Probabilidad:", probabilidad)

    # NAO responde
    motion = ALProxy("ALMotion", ROBOT_IP, PORT)
    tts = ALProxy("ALTextToSpeech", ROBOT_IP, PORT)
    posture = ALProxy("ALRobotPosture", ROBOT_IP, PORT)

    motion.wakeUp()
    posture.goToPosture("StandInit", 0.5)

    if resultado == 1:
        tts.say("¡Tienes un alto riesgo de diabetes!")
    else:
        # tts.say("No se detecta riesgo de diabetes. Probabilidad: %.0f por ciento." % (probabilidad * 100))
        tts.say("No se detecta riesgo de diabetes")

    motion.rest()

except Exception as e:
    print("❌ Error:", e)