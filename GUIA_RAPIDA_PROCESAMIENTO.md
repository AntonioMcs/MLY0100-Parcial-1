# 🚀 Pipeline de Procesamiento - MLY0100 Parcial 1

## 📌 Inicio Rápido

### 1. Dataset ya está procesado ✅
```bash
# Dataset final LISTO PARA MODELADO
data/03_processed/df_processed_final.csv  (119,143 × 134 columnas)
```

### 2. Cargarlo en Python
```python
import pandas as pd

# Cargar dataset procesado (EN INGLÉS)
df = pd.read_csv('data/03_processed/df_processed_final.csv')

# Verificar
print(f"Dimensiones: {df.shape}")
print(f"Valores faltantes: {df.isnull().sum().sum()}")

# Usar en modelado
X = df.drop(columns=['review_score'])
y = df['review_score']
```

### 3. O usar el utility script
```python
from src.cargar_dataset_procesado import cargar_dataset_procesado

# Cargar con validación automática
df = cargar_dataset_procesado()

# Ya está listo
print(df.shape)  # (119143, 134)
```

---

## 📊 ¿Qué pasó?

Se reescribió todo el pipeline de procesamiento para que **funcione con el nuevo dataset traducido al inglés** en lugar del dataset original en portugués.

### Flujo Original → Nuevo Flujo

| Fase | Original | Nuevo |
|------|----------|-------|
| 1️⃣ Union | 9 CSV raw | 9 CSV raw |
| 2️⃣ Limpieza | Caracteres especiales | Caracteres especiales |
| 3️⃣ Traducción | ❌ NO EXISTÍA | ✅ Traducir a inglés |
| 4️⃣ Procesamiento | Script/Notebook | Script maestro |
| **Output** | Dataset portugués | **Dataset inglés** |

---

## 🎯 Estado Actual

### ✅ Completado
- [x] Dataset unido: 119,143 filas × 44 columnas
- [x] Caracteres especiales limpiados (ã, é, ç → a, e, c)
- [x] **TODO traducido a inglés**
- [x] Valores faltantes: 208,702 → 0 (100% completo)
- [x] Outliers tratados: 17 variables
- [x] Features creadas: 9 variables derivadas
- [x] Encoding: 6 One-Hot + 8 Label (→ 134 columnas)
- [x] Escalado: StandardScaler + MinMaxScaler
- [x] Dataset final guardado: `data/03_processed/df_processed_final.csv`

### 🚀 Listo Para
- ✅ Modelado en Notebook 02
- ✅ Validación cruzada
- ✅ Predicción con nuevos datos

---

## 📂 Estructura de Archivos

### Output Principal
```
data/03_processed/
└── df_processed_final.csv  ⭐ DATASET FINAL (119,143 × 134)
```

### Archivos Intermedios (para debugging)
```
data/02_intermediate/
├── df_unido_y_limpio.csv              (Paso 1: Union)
├── df_translated_to_english.csv       (Paso 2: Traducción)
├── df_cleaned.csv                     (Paso 3: Missing values)
├── df_cleaned_no_outliers.csv         (Paso 4: Outliers)
├── df_cleaned_categorical.csv         (Paso 5: Categorías)
├── df_with_features.csv               (Paso 6: Features)
└── df_encoded.csv                     (Paso 7: Encoding)
```

### Modelos Guardados (para predicción)
```
data/06_models/
├── scaler_standard.pkl   (StandardScaler para 19 variables)
└── scaler_minmax.pkl     (MinMaxScaler para 12 variables)
```

---

## 🔧 Scripts Disponibles

### 1. `union_y_limpieza.py`
Une 9 archivos CSV + limpia caracteres especiales

```bash
python src/union_y_limpieza.py
# Output: data/02_intermediate/df_unido_y_limpio.csv
```

### 2. `traduccion_a_ingles.py`
Traduce dataset completo a inglés

```bash
python src/traduccion_a_ingles.py
# Output: data/02_intermediate/df_translated_to_english.csv
```

### 3. `procesar_dataset_maestro.py` ⭐
Ejecuta los 9 pasos de procesamiento (RECOMENDADO)

```bash
python src/procesar_dataset_maestro.py
# Output: data/03_processed/df_processed_final.csv
```

### 4. `cargar_dataset_procesado.py`
Utility para cargar dataset en Python

```python
from src.cargar_dataset_procesado import cargar_dataset_procesado
df = cargar_dataset_procesado()
```

---

## 📋 Los 9 Pasos del Procesamiento

```
PASO 1: Cargar dataset traducido
        Input:  119,143 × 44
        Output: Dataset en memoria

PASO 2: Analizar estado inicial
        Detecta: 208,702 valores faltantes
        Análisis: Tipos de datos, duplicados

PASO 3: Tratar valores faltantes
        Método: Mediana (numéricas), Moda (categóricas)
        Resultado: 208,702 → 0 ✅

PASO 4: Tratar outliers
        Método: IQR con k=1.5 (capping, no eliminación)
        Variables: 17 numéricas

PASO 5: Limpiar categóricas
        Normalización: lowercase, strip, group raras (<1%)
        Variables: 18 categóricas

PASO 6: Feature Engineering
        Nuevas variables: 9 derivadas (order_total_value, delivery_days, etc.)
        Columnas: 44 → 53

PASO 7: Encoding
        One-Hot (≤50 cats): 6 variables
        Label (>50 cats): 8 variables
        Columnas: 53 → 134

PASO 8: Normalización/Escalado
        StandardScaler: 19 variables (|skewness| < 1)
        MinMaxScaler: 12 variables (|skewness| ≥ 1)
        Scalers guardados: .pkl files

PASO 9: Guardar dataset final
        Output: data/03_processed/df_processed_final.csv
        Status: ✅ LISTO PARA MODELADO
```

---

## 🎨 Cambios en Columnas

### Ejemplos de Traducción

| Portugués | Inglés |
|-----------|--------|
| order_id | order_id |
| cliente_id | customer_id |
| data_compra | order_purchase_timestamp |
| preço | price |
| peso_produto_kg | product_weight_g |
| avaliação_cliente | review_score |
| estado_uf | state_code |
| cidade_cliente | customer_city |

### Ejemplos de One-Hot Encoding

**payment_type** (4 categorías):
- payment_type_credit_card → 0 or 1
- payment_type_boleto → 0 or 1
- payment_type_debit_card → 0 or 1
- payment_type_voucher → 0 or 1

**order_status** (8 categorías):
- order_status_delivered → 0 or 1
- order_status_canceled → 0 or 1
- order_status_pending → 0 or 1
- etc.

---

## 📊 Estadísticas del Dataset Final

```
Dimensiones:        119,143 filas × 134 columnas
Tamaño:             162.19 MB
Valores faltantes:  0 (100% completo)
Duplicados:         11,320 (retenidos)

Tipos de datos:
  - Booleanas:      87 (del One-Hot encoding)
  - Float64:        33 (variables numéricas escaladas)
  - Object:         13 (identificadores sin procesar)
  - Int64:          1

Variables:
  - Numéricas:      34 (escaladas)
  - Categóricas:    13 (no procesadas, IDs)
  - Booleanas:      87 (del encoding)
```

---

## 🔄 ¿Cómo Actualizar?

### Si cambió datos raw:
```bash
# Reejecutar todo el pipeline
python src/procesar_dataset_maestro.py

# O fase por fase
python src/union_y_limpieza.py
python src/traduccion_a_ingles.py
python src/procesar_dataset_maestro.py
```

### Si necesita regenerar desde cero:
```bash
# Limpiar archivos intermedios
rm data/02_intermediate/df_*.csv

# Regenerar
python src/procesar_dataset_maestro.py
```

---

## ✅ Validación

### Verificar integridad:
```python
import pandas as pd

df = pd.read_csv('data/03_processed/df_processed_final.csv')

# Validaciones
assert df.shape == (119_143, 134), "Dimensiones incorrectas"
assert df.isnull().sum().sum() == 0, "Hay valores faltantes"
assert df['review_score'].notna().all(), "review_score tiene NaN"

print("✅ Dataset validado correctamente")
```

### O usar el utility:
```python
from src.cargar_dataset_procesado import cargar_dataset_procesado, mostrar_estadisticas

df = cargar_dataset_procesado()
mostrar_estadisticas(df)
```

---

## 🎯 Próximo Paso: Notebook 02

### Cargar datos:
```python
import pandas as pd
from src.cargar_dataset_procesado import cargar_dataset_procesado

# Opción 1: Directo
df = pd.read_csv('data/03_processed/df_processed_final.csv')

# Opción 2: Con utility (recomendado)
df = cargar_dataset_procesado()

# Separar features y target
X = df.drop(columns=['review_score'])
y = df['review_score']

# Proceder con modelado
print(f"Features: {X.shape}")
print(f"Target: {y.shape}")
```

### Mantener escalers para inferencia:
```python
import joblib

# Cargar scalers si necesita predecir sobre nuevos datos
scaler_std = joblib.load('data/06_models/scaler_standard.pkl')
scaler_minmax = joblib.load('data/06_models/scaler_minmax.pkl')

# Usar en predicción
X_new_scaled = scaler_std.transform(X_new_subset)
```

---

## 📖 Documentación Completa

Ver archivos:
- **[PROCESAMIENTO_PIPELINE.md](PROCESAMIENTO_PIPELINE.md)** - Documentación técnica completa
- **[RESUMEN_PROCESAMIENTO.md](RESUMEN_PROCESAMIENTO.md)** - Resumen ejecutivo

---

## ⚠️ Notas Importantes

1. **Valores faltantes:** Se imputaron (no se eliminaron) para preservar el tamaño
2. **Duplicados:** Se retuvieron (pueden ser órdenes múltiples válidas)
3. **Outliers:** Se aplicó capping (no eliminación) para preservar datos extremos
4. **IDs:** No fueron escalados (son identificadores, no features)
5. **Scalers:** Se guardaron para aplicar a datos de prueba/predicción

---

## 🎊 ¡COMPLETADO!

✅ Pipeline de procesamiento ejecutado exitosamente  
✅ Dataset traducido al inglés y procesado  
✅ 119,143 filas × 134 columnas listo para modelado  
✅ 0 valores faltantes (100% completo)  
✅ Documentación completa incluida  

**Estado: PRODUCCIÓN** 🚀

---

*MLY0100 - Parcial 1 - 2024*  
*Última actualización: 2024*  
*Versión: 3.0*
