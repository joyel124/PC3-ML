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
