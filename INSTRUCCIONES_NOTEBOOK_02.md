# 📝 Instrucciones para Notebook 02 - Modelado

## 🎯 Objetivo
Usar el nuevo dataset procesado (traducido al inglés y completamente limpio) para entrenar modelos de regresión y clasificación.

---

## 📥 PASO 1: Cargar el Dataset

### Opción A: Carga Directa (Recomendada)
```python
import pandas as pd

# Cargar dataset ya procesado
df = pd.read_csv('data/03_processed/df_processed_final.csv')

# Verificar
print(f"Dimensiones: {df.shape}")
print(f"Valores faltantes: {df.isnull().sum().sum()}")
print(f"Primeras columnas: {df.columns[:10].tolist()}")

# Output esperado:
# Dimensiones: (119143, 134)
# Valores faltantes: 0
```

### Opción B: Con Utility Script (Más Segura)
```python
# En la celda de imports
import sys
sys.path.insert(0, 'src')

from cargar_dataset_procesado import cargar_dataset_procesado, mostrar_estadisticas

# Cargar con validación automática
df = cargar_dataset_procesado()

# Ver estadísticas detalladas
mostrar_estadisticas(df)
```

---

## 🔍 PASO 2: Explorar Variables

### Columnas Disponibles
```python
# Ver todas las columnas
print(df.columns.tolist())

# Agrupar por tipo
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
bool_cols = df.select_dtypes(include=['bool']).columns.tolist()
object_cols = df.select_dtypes(include=['object']).columns.tolist()

print(f"Numéricas: {len(numeric_cols)}")
print(f"Booleanas: {len(bool_cols)}")
print(f"Objetos: {len(object_cols)}")
```

### Variable Target
```python
# La variable target es 'review_score'
print(df['review_score'].describe())

# Visualizar distribución
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.hist(df['review_score'], bins=30, edgecolor='black')
plt.xlabel('Review Score')
plt.ylabel('Frecuencia')
plt.title('Distribución de Review Scores')
plt.show()

# Estadísticas
print(f"Min: {df['review_score'].min()}")
print(f"Max: {df['review_score'].max()}")
print(f"Mean: {df['review_score'].mean():.2f}")
print(f"Median: {df['review_score'].median():.2f}")
print(f"Std: {df['review_score'].std():.2f}")
```

---

## 🔧 PASO 3: Preparar Features y Target

### Separación Básica
```python
# Separar features y target
X = df.drop(columns=['review_score'])
y = df['review_score']

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"Tipo target: {y.dtype}")
```

### Remover Identificadores (Opcional)
```python
# Si desea remover columnas que son solo IDs
id_columns = ['order_id', 'customer_id', 'customer_unique_id', 
              'order_item_id', 'product_id', 'seller_id', 'review_id']

id_cols_present = [col for col in id_columns if col in X.columns]

if id_cols_present:
    X = X.drop(columns=id_cols_present)
    print(f"Columnas ID removidas: {len(id_cols_present)}")
    print(f"X shape después: {X.shape}")
```

### Remover Timestamps (Opcional)
```python
# Si desea remover columnas de fecha/hora
timestamp_columns = [col for col in X.columns 
                    if 'timestamp' in col.lower() or 'date' in col.lower()]

if timestamp_columns:
    X = X.drop(columns=timestamp_columns)
    print(f"Columnas timestamp removidas: {len(timestamp_columns)}")
    print(f"X shape después: {X.shape}")
```

---

## 📊 PASO 4: Dividir en Train/Test

### Split Estándar
```python
from sklearn.model_selection import train_test_split

# Dividir 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Train size: {X_train.shape}")
print(f"Test size: {X_test.shape}")
```

### Split Estratificado (Si es Clasificación)
```python
# Si convierte review_score a categorías
y_categories = pd.cut(y, bins=5)  # 5 categorías

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y_categories
)

print(f"Train: {X_train.shape}")
print(f"Test: {X_test.shape}")
```

---

## ⚙️ PASO 5: Validación Cruzada

### Setup Recomendado
```python
from sklearn.model_selection import cross_val_score, KFold

# Definir k-fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Ejemplo con regresión
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(model, X_train, y_train, 
                        cv=kfold, scoring='r2')

print(f"CV R² Scores: {scores}")
print(f"Mean R²: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

---

## 🎯 PASO 6: Entrenar Modelos de Regresión

### Ejemplo: Regresión Lineal
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Entrenar
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluar
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))

print(f"Train R²: {train_r2:.4f}")
print(f"Test R²: {test_r2:.4f}")
print(f"Test RMSE: {test_rmse:.4f}")
```

### Ejemplo: Random Forest
```python
from sklearn.ensemble import RandomForestRegressor

# Entrenar
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Predecir y evaluar
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R²: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# Feature importance
importances = pd.DataFrame({
    'feature': X_train.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(importances.head(10))
```

---

## 🏆 PASO 7: Entrenar Modelos de Clasificación

### Preparar Variable Target
```python
# Convertir review_score (1-5) a categorías
y_class = pd.cut(y, bins=[0, 2, 4, 5], labels=['Bad', 'Good', 'Excellent'])

# O usar el score directo como clase
y_class = y.astype(int)  # 1, 2, 3, 4, 5

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_class, test_size=0.2, random_state=42, stratify=y_class
)

print(f"Clases: {y_train_c.unique()}")
print(f"Distribución train:\n{y_train_c.value_counts()}")
```

### Entrenar Clasificador
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Entrenar
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_c, y_train_c)

# Predecir
y_pred_c = model.predict(X_test_c)

# Evaluar
print(classification_report(y_test_c, y_pred_c))

# Matriz de confusión
cm = confusion_matrix(y_test_c, y_pred_c)
print(f"Confusion Matrix:\n{cm}")
```

### Manejar Desbalance (si aplica)
```python
from imblearn.over_sampling import SMOTE

# Aplicar SMOTE
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train_c, y_train_c)

# Entrenar con datos balanceados
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_smote, y_train_smote)

y_pred_c = model.predict(X_test_c)
print(classification_report(y_test_c, y_pred_c))
```

---

## 💾 PASO 8: Guardar Modelos

### Guardar con Joblib
```python
import joblib

# Guardar modelo entrenado
joblib.dump(model, 'data/06_models/model_final.pkl')

# Cargar después
model_loaded = joblib.load('data/06_models/model_final.pkl')

# Hacer predicción
y_pred = model_loaded.predict(X_test)
```

### Guardar Información del Modelo
```python
import json

# Guardar metadata
metadata = {
    'model_type': 'RandomForestRegressor',
    'train_size': len(X_train),
    'test_size': len(X_test),
    'features_used': X_train.columns.tolist(),
    'train_r2': float(train_r2),
    'test_r2': float(test_r2),
    'test_rmse': float(test_rmse),
}

with open('data/06_models/model_metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)
```

---

## 🔄 PASO 9: Hacer Predicciones en Nuevos Datos

### Cargar Scalers
```python
import joblib

# Cargar scalers utilizados en el procesamiento
scaler_std = joblib.load('data/06_models/scaler_standard.pkl')
scaler_minmax = joblib.load('data/06_models/scaler_minmax.pkl')
```

### Procesar Nuevos Datos
```python
# Nuevos datos (debe tener la misma estructura)
df_new = pd.read_csv('nuevos_datos.csv')

# Aplicar transformaciones idénticas
# 1. Rellenar valores faltantes
df_new = df_new.fillna(df_new.median(numeric_only=True))

# 2. Remover columnas no usadas
cols_to_use = [col for col in X_train.columns if col in df_new.columns]
X_new = df_new[cols_to_use]

# 3. Aplicar escalado
X_new_scaled = X_new.copy()
# (aplicar scalers correctamente a las columnas correspondientes)

# Predecir
y_pred_new = model.predict(X_new_scaled)
```

---

## 🎨 PASO 10: Visualizaciones

### Regresión
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Predicción vs Real
axes[0].scatter(y_test, y_pred_test, alpha=0.5)
axes[0].plot([y_test.min(), y_test.max()], 
            [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0].set_xlabel('Actual')
axes[0].set_ylabel('Predicción')
axes[0].set_title(f'Predicción vs Real (R²={test_r2:.4f})')
axes[0].grid(True, alpha=0.3)

# Residuos
residuals = y_test - y_pred_test
axes[1].scatter(y_pred_test, residuals, alpha=0.5)
axes[1].axhline(y=0, color='r', linestyle='--', lw=2)
axes[1].set_xlabel('Predicción')
axes[1].set_ylabel('Residuo')
axes[1].set_title('Gráfico de Residuos')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Clasificación
```python
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test_c, y_pred_c)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=np.unique(y_train_c),
            yticklabels=np.unique(y_train_c))
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.title('Matriz de Confusión')
plt.show()
```

---

## ⚠️ NOTAS IMPORTANTES

### 1. Dataset ya está completo
✅ 119,143 filas × 134 columnas  
✅ 0 valores faltantes  
✅ Variables ya escaladas  
✅ Variables categóricas ya encodificadas  

### 2. NO necesita repetir procesamiento
❌ No ejecute `procesar_dataset_maestro.py` nuevamente (ya está hecho)  
❌ No aplique `StandardScaler` de nuevo (ya está aplicado)  
❌ No haga One-Hot encoding (ya está hecho)  

### 3. Si necesita hacer predicción en datos nuevos
Debe aplicar **exactamente el mismo preprocesamiento** que se hizo al conjunto de entrenamiento.  
Use los scalers guardados en `data/06_models/`

### 4. Columnas importantes
- **IDs:** order_id, customer_id, product_id, seller_id
- **Fechas:** order_purchase_timestamp, order_delivered_customer_date (formato objeto)
- **Target:** review_score (0-5, float)
- **Features:** Resto de columnas

---

## 🚀 RESUMEN RÁPIDO

```python
# 1. Cargar
df = pd.read_csv('data/03_processed/df_processed_final.csv')

# 2. Separar
X = df.drop(columns=['review_score'])
y = df['review_score']

# 3. Dividir
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Entrenar
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

# 5. Evaluar
from sklearn.metrics import r2_score
y_pred = model.predict(X_test)
print(f"R²: {r2_score(y_test, y_pred):.4f}")

# 6. Guardar
import joblib
joblib.dump(model, 'data/06_models/my_model.pkl')
```

---

## 📚 Referencias

- [pandas Documentation](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [matplotlib](https://matplotlib.org/)
- [Dataset Brazilian E-commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

**Última actualización:** 2024  
**Estado:** ✅ LISTO PARA USAR  
**Dataset:** df_processed_final.csv (119,143 × 134)
