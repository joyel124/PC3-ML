<div align="center">
  <a href="https://github.com/EduardoPuglisevich/Aplicaciones-de-Data-Science.git">
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/UPC_logo_transparente.png" alt="Logo UPC" width="80" height="80">
  </a>

  <h3 align="center"> Machine-Learning-CC57</h3>

  <p align="center">
    Practica Califica 3
    <br/>
    <br/>
    <strong>Docente</strong>
    <br/>
    Jairo Pinedo Taquia
  </p>
</div>

# 🤖 Detección de Riesgo de Diabetes con NAO y Machine Learning

## 🎯 Objetivo del Proyecto

Este proyecto tiene como finalidad integrar un modelo de Machine Learning que predice el riesgo de diabetes tipo 2, con un robot humanoide NAO, que interpreta los resultados y brinda una respuesta verbal al usuario. La solución demuestra cómo la inteligencia artificial puede ser usada en aplicaciones biomédicas interactivas.

---

## 🧠 Modelo de Inteligencia Artificial

El modelo fue entrenado usando un conjunto de datos médicos con las siguientes características:

- `gender`: Sexo del paciente
- `age`: Edad
- `hypertension`: Presencia de hipertensión (0/1)
- `heart_disease`: Presencia de enfermedad cardíaca (0/1)
- `smoking_history`: Historial de tabaquismo
- `bmi`: Índice de masa corporal
- `HbA1c_level`: Nivel de hemoglobina glicosilada
- `blood_glucose_level`: Nivel de glucosa en sangre

Se utilizó un **Gradient Boosting Classifier** integrado con un `ColumnTransformer` para el preprocesamiento de datos. El modelo alcanza una **precisión del 97.2%**.

---

## 📁 Arquitectura del Proyecto

---

## 📁 Estructura del Carpetas

```plaintext
project-root/
├── client/
│   └── nao.py                    # Script que ejecuta el robot NAO (cliente)
│
├── server/
│   ├── dataset/
│   │   └── diabetes_prediction_dataset.csv   # Dataset usado para entrenar
│   ├── main.py                  # Servidor Flask que expone el endpoint /predecir
│   ├── model2.py                # Script de entrenamiento del modelo de IA
│   └── modelo_diabetes_v2.pkl   # Modelo entrenado exportado con joblib

```
---
# ⚙️ Instrucciones de instalación del modelo de IA en el Robot NAO

## 🧪 1. Requisitos previos
- **Python 2.7** (para NAOqi SDK, si se usa en PC)
- **Python 3.x** (para el servidor Flask/API)
- **NAOqi SDK instalado** (opcional si solo usas simulador)
- **Robot NAO encendido** o uso del simulador NAO en Choregraphe/Chrome
- **IP del robot o simulador conocida** (`127.0.0.1` para local)

## 🛠️ 2. Instalar dependencias del servidor (API)
Crea y activa un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Asegúrate de tener en el directorio server/:

* modelo_diabetes_v2.pkl
* main.py
* dataset/diabetes_prediction_dataset.csv

## 🚀 3. Ejecutar el servidor Flask (API)

```bash
cd server
python main.py
```

Esto abrirá el endpoint en http://localhost:5000/predecir.

| ⚠️ Asegúrate de que el firewall permita conexiones si trabajas desde otra red/local.

## 🤖 4. Ejecutar el cliente (robot físico o simulador)

✅ Opción A: Robot NAO físico

* IP del robot NAO conocida (ej: 192.168.1.5)
* En client/nao.py, actualiza:

```
python
ROBOT_IP = "192.168.1.5"
API_URL = "http://TU_IP_LOCAL:5000/predecir"
```

Luego ejecuta:

```bash
python nao.py
```

El robot hablará según la predicción.

🧪 Opción B: Simulador (Choregraphe o Web)

* Inicia el simulador NAO (Chrome/Choregraphe)
* Usa esta configuración en el script nao.py:

```
python
ROBOT_IP = "127.0.0.1"
API_URL = "http://127.0.0.1:5000/predecir"
```

* Corre el script:

```bash
python nao.py
```

El mensaje será mostrado como un globo sobre la cabeza del NAO.

🧪 Ejemplo de uso (NAO)

```bash
python client/nao.py
```
Primero, NAO empezará a hacer preguntas y el usuario las responderá por la consola (En el caso de usar el simulador).

Luego de procesar las respuestas del usuario, NAO les dirá:
* ¡Tienes un alto riesgo de diabetes!" si el modelo predice riesgo (1)
* No se detecta riesgo de diabetes." si el modelo predice (0)

## 📺 Video Explicativo
📽️ Enlace al video de demostración (no listado en YouTube):
👉 https://youtu.be/ENLACE-DEMO-AQUI

El video muestra:

* Objetivo del proyecto y del modelo de ML.
* Arquitectura del sistema.
* Funcionamiento en tiempo real con el robot NAO.

## 👨‍💻 Integrantes

* u202013066 Christian Joel Cutipa Cañapataña 
* u202112986 José Giovanni Laura Silvera
* u202116752 Cesar Rafael Sanchez Garay
* u20191b823 Nicola Rovegno Chavez


