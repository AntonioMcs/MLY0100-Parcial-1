# 📘 Proyecto Parcial — MLY0100  
## Predicción y Evaluación de Riesgo de Diabetes usando Kedro, Docker y Airflow  
**Autor:** Antonio Sepúlveda  
**Fecha:** 2025  

---

# 🩺 1. Entendimiento del Negocio

El objetivo del proyecto es desarrollar un **pipeline automatizado de Machine Learning** para:

### ✔️ Clasificar pacientes según la probabilidad de tener diabetes  
Usando la variable objetivo **Outcome**:  
- **0 = No diabetes**  
- **1 = Diabetes**

### ✔️ Implementar un flujo completo usando Kedro:
- Limpieza y validación de datos  
- División Train/Test  
- Entrenamiento de modelos  
- Evaluación automática  
- Reportes y visualizaciones  
- Ejecución modular, escalable y reproducible  

### 🔍 Beneficios del sistema:
- Apoyar diagnósticos tempranos  
- Priorizar pacientes de mayor riesgo  
- Identificar factores clínicos relevantes  
- Automatizar experimentación y retraining  

---

# 📊 2. Entendimiento de los Datos

Se utiliza el **PIMA Diabetes Dataset**, ubicado en:

data/01_raw/diabetes.csv


### 🔢 Variables principales:
- Pregnancies  
- Glucose  
- BloodPressure  
- SkinThickness  
- Insulin  
- BMI  
- DiabetesPedigreeFunction  
- Age  
- Outcome (objetivo)

### ✔️ Resultados generados por el pipeline:
- Datos limpios → `diabetes_cleaned`
- Split → `X_train`, `X_test`, `y_train`, `y_test`
- Modelo entrenado → `diabetes_trained_model`
- Métricas CSV → `diabetes_evaluation_results`
- Visualizaciones → `data/08_reporting/`

---

## 🔁 Pipelines disponibles

- `diabetes`: limpieza, split, entrenamiento y evaluación principal.
- `clustering`: escalado + KMeans para segmentación clínica.
- `reporting`: genera gráficos y visualizaciones a partir de las métricas.
- `unsupervised_learning`: PCA + clustering + detección de anomalías inspirado en el proyecto FIFA pero enfocado en diabetes.

---

## ⚙️ 3. Instalación y Configuración
##
## 1. Clonar repositorio
```sh
git clone https://github.com/AntonioMcs/MLY0100-Parcial-1.git
cd MLY0100-Parcial-1/mly0100parcial-kedro
