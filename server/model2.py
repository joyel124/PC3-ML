import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Cargar dataset
df = pd.read_csv("dataset/diabetes_prediction_dataset.csv")  # Asegúrate de renombrar correctamente tu CSV

# Separar features (X) y target (y)
X = df.drop("diabetes", axis=1)
y = df["diabetes"]

# Columnas categóricas y numéricas
columnas_cat = ["gender", "smoking_history"]
columnas_num = ["age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]

# Preprocesamiento
preprocesamiento = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), columnas_cat),
    ("num", StandardScaler(), columnas_num)
])

# Pipeline completo
modelo = Pipeline([
    ("preprocesado", preprocesamiento),
    ("clasificador", GradientBoostingClassifier(random_state=42))
])

# División entrenamiento / prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print("✅ Precisión:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Exportar modelo entrenado
joblib.dump(modelo, "modelo_diabetes_v2.pkl")
print("✅ Modelo exportado como modelo_diabetes_v2.pkl")