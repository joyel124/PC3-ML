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

## 🧱 Arquitectura del Proyecto

```mermaid
graph TD
    A[Usuario] -->|Envía datos médicos| B[API Flask]
    B --> C[Modelo ML .pkl]
    C --> D[Predicción]
    D -->|Probabilidad| E[NAO Robot]
    E -->|Voz / Respuesta| F[Usuario]
