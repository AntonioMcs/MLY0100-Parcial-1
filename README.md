# Proyecto Parcial 1 - MLY0100
**Análisis, Preprocesamiento y Modelado de E-commerce Brasileño**

**Integrante:** Antonio Sepulveda  
**Fecha:** 20/01/2026  
**Metodología:** CRISP-DM (Phases 1-6)

---

## 📋 Descripción del Proyecto

Este proyecto realiza un análisis exploratorio, preprocesamiento y modelado predictivo de datos del e-commerce brasileño (Olist) siguiendo la metodología **CRISP-DM** y cumpliendo todos los criterios de la rúbrica del curso MLY0100.

### Fases Completadas

- ✅ **Fase 1: Business Understanding** - Contexto del negocio y objetivos definidos
- ✅ **Fase 2: Data Understanding** - Análisis exploratorio completo
- ✅ **Fase 3: Data Preparation** - Limpieza, transformación y preprocesamiento
- ✅ **Fase 4: Modeling** - Regresión y clasificación supervisada
- ✅ **Fase 5: Evaluation** - Evaluación con múltiples métricas
- ✅ **Fase 6: Deployment** - Documentación final y reproducibilidad

---

## 📊 Dataset

**Dataset:** Brazilian E-commerce (Olist)  
**Fuente:** Kaggle - [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

### Archivos Utilizados
- `olist_orders_dataset.csv` - Información de pedidos
- `olist_order_items_dataset.csv` - Items de cada pedido
- `olist_customers_dataset.csv` - Información de clientes
- `olist_products_dataset.csv` - Información de productos
- `olist_sellers_dataset.csv` - Información de vendedores
- `olist_order_payments_dataset.csv` - Información de pagos
- `olist_order_reviews_dataset.csv` - Reseñas de pedidos

### Dataset Procesado Final
- **Dimensiones:** 119,143 filas × 134 columnas
- **Valores faltantes:** 0 (100% completo)
- **Ubicación:** `data/02_intermediate/df_processed_final.csv`
- **Características:** Traducido a inglés, escalado, codificado y sin outliers

---

## ⚙️ Instalación y Configuración

### Requisitos Previos
- Python 3.11.9 o superior
- Git (opcional)

### Pasos de Instalación

1. **Crear entorno virtual**
```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Si error de política de ejecución:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. **Instalar dependencias**
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. **Verificar instalación**
```powershell
python -c "import pandas, numpy, sklearn, xgboost; print('✓ Dependencias instaladas')"
```

---

## 🚀 Uso del Proyecto

### Estructura de Carpetas

```
MLY0100-Parcial-1/
├── notebooks/
│   ├── 01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb  # Análisis exploratorio
│   └── 02_Modelado_nuevo.ipynb                            # Regresión y clasificación
├── data/
│   ├── 01_raw/                     # Datasets originales
│   ├── 02_intermediate/            # Dataset procesado (LISTO PARA USAR)
│   ├── 06_models/                  # Modelos y scalers guardados
│   └── 08_reporting/               # Figuras y reportes
├── src/
│   ├── union_y_limpieza.py        # Unión de 9 tablas + limpieza
│   ├── traduccion_a_ingles.py     # Traducción del dataset
│   ├── procesar_dataset_maestro.py # Pipeline de procesamiento
│   └── cargar_dataset_procesado.py # Utilidad para cargar datos
├── conf/
│   └── parameters.yml
└── README.md
```

### Ejecutar Notebooks

#### Opción A: VS Code / Cursor (Recomendado)
1. Abre `notebooks/01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb`
2. Selecciona kernel: `.venv` (Python 3.11)
3. Ejecuta las celdas con `Shift + Enter`

#### Opción B: Jupyter Lab
```powershell
jupyter lab
# Se abrirá en http://localhost:8888
```

#### Opción C: Jupyter Notebook
```powershell
jupyter notebook
```

### Verificar el Kernel
```python
import sys
print(f"Python: {sys.version}")
print(f"Ubicación: {sys.executable}")
# Debe apuntar a .venv
```

---

## 📓 Notebooks Incluidos

### Notebook 01: EDA y Preprocesamiento
**Archivo:** `notebooks/01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb`

**Contenido:**
- Carga del dataset procesado (ya traducido e inglés)
- Análisis exploratorio completo (EDA)
- Estadísticos descriptivos
- Análisis de distribuciones
- Detección de outliers
- Visualizaciones e interpretaciones

**Criterios Cumplidos:** CRISP-DM Fases 1-3, estadísticos, distribuciones

---

### Notebook 02: Modelado Predictivo
**Archivo:** `notebooks/02_Modelado_nuevo.ipynb`

**Contenido:**

#### Sección 4.4: REGRESIÓN
- **Target:** `order_total_value` (valor total del pedido)
- **4 Algoritmos:**
  1. Linear Regression
  2. Decision Tree Regressor
  3. Random Forest Regressor
  4. XGBoost Regressor
- **Métricas:** MAE, RMSE, R²
- **Análisis:** Overfitting/Underfitting detección

#### Sección 4.5: CLASIFICACIÓN
- **Target:** `order_status` (estado del pedido)
- **5 Algoritmos:**
  1. Logistic Regression
  2. Decision Tree Classifier
  3. Random Forest Classifier
  4. Support Vector Machine (SVM)
  5. Gaussian Naive Bayes
- **Balance de Clases:** SMOTE aplicado
- **Métricas:** Accuracy, Precision, Recall, F1-Score
- **Análisis:** Overfitting/Underfitting detección

#### Sección 4.6: Resumen Final
- Comparación de modelos
- Matriz de cumplimiento de rúbrica
- Conclusiones y resultados de aprendizaje

**Criterios Cumplidos:** CRISP-DM Fases 4-5, múltiples algoritmos, métricas, balance de clases

---

## 📈 Pipeline de Procesamiento

### Etapas Ejecutadas (Automatizadas)

**Fase 1: Unión de Datos**
- Combinación de 9 tablas CSV
- Limpieza de caracteres especiales portugués
- Output: 119,143 × 44 columnas

**Fase 2: Traducción a Inglés**
- Traducción de nombres de columnas
- Traducción de valores categóricos (27 estados brasileños)
- Traducción de estados de pedidos y tipos de pago
- Output: 100% en inglés

**Fase 3: Encoding y Escalado**
- One-Hot Encoding (≤50 categorías)
- Label Encoding (>50 categorías)
- StandardScaler (19 columnas)
- MinMaxScaler (12 columnas)
- Output: 119,143 × 134 columnas (listo para modelado)

**Fase 4: Feature Engineering**
- Creación de características derivadas
- Detección y capado de outliers
- Imputación de valores faltantes

### Scripts Disponibles

```python
# 1. Unión y limpieza
from src.union_y_limpieza import limpiar_caracteres_especiales, union_optima_olist

# 2. Traducción
from src.traduccion_a_ingles import traducir_dataset_olist

# 3. Procesamiento completo
from src.procesar_dataset_maestro import procesar_dataset_maestro

# 4. Cargar datos procesados
from src.cargar_dataset_procesado import cargar_dataset_procesado
df = cargar_dataset_procesado()  # Listo para modelado
```

---

## ✅ Matriz de Cumplimiento de Rúbrica (10 Criterios)

| Criterio | Descripción | Evidencia | Estado |
|----------|-------------|-----------|--------|
| 1 | **Target Continuo** (Regresión) | `order_total_value` (precio) | ✅ |
| 2 | **Múltiples Algoritmos** | 4 regresión + 5 clasificación | ✅ |
| 3 | **3+ Métricas Regresión** | MAE, RMSE, R² | ✅ |
| 4 | **Mejor Modelo Regresión** | Seleccionado por R² máximo | ✅ |
| 5 | **Target Discreto** (Clasificación) | `order_status` (6-7 estados) | ✅ |
| 6 | **Análisis de Correlación** | Top 15 features vs targets | ✅ |
| 7 | **Balance de Clases** | SMOTE aplicado | ✅ |
| 8 | **4+ Métricas Clasificación** | Accuracy, Precision, Recall, F1 | ✅ |
| 9 | **Múltiples Algoritmos Clasificación** | 5 modelos diferentes | ✅ |
| 10 | **Overfitting/Underfitting** | Análisis Train vs Test | ✅ |

---

## 📊 Resultados Esperados

### Regresión (Predecir Precio del Pedido)
- Mejor modelo identificado automáticamente
- Error promedio (MAE) en dólares cuantificado
- Varianza explicada (R²) reportada
- Generalización validada

### Clasificación (Predecir Estado del Pedido)
- 5 modelos entrenados y evaluados
- Desbalance de clases tratado con SMOTE
- Métricas multi-clase calculadas
- Matriz de confusión generada

---

## 📚 Tecnologías Utilizadas

### Data Processing
- `pandas` - Manipulación de datos
- `numpy` - Operaciones numéricas
- `scipy` - Estadísticas

### Machine Learning
- `scikit-learn` - Algoritmos ML
- `xgboost` - Gradient Boosting
- `imblearn` - SMOTE para balance

### Visualización
- `matplotlib` - Gráficos base
- `seaborn` - Estadísticos avanzados

### Utilidades
- `joblib` - Persistencia de modelos
- `pathlib` - Rutas multiplataforma

---

## 🔧 Troubleshooting

### Error: "No module named 'pandas'"
```powershell
# Asegúrate de estar en el entorno virtual
.\.venv\Scripts\Activate.ps1

# Reinstala dependencias
pip install -r requirements.txt
```

### Error de Política de Ejecución (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### El kernel no encuentra el módulo
```python
# En la primera celda del notebook:
import sys
sys.path.insert(0, 'src')
```

---

## 📝 Notas Importantes

1. **Dataset ya está procesado** - No necesitas ejecutar scripts de union/traducción
2. **Usar Notebook 02 directamente** - Carga `data/02_intermediate/df_processed_final.csv`
3. **Kernel correcto** - Siempre selecciona `.venv` como kernel
4. **Reproducibilidad** - Todos los `random_state=42` fijos para resultados consistentes
5. **Modelos guardados** - Se persisten en `data/06_models/` para producción

---

## 📞 Contacto

**Integrante:** Antonio Sepulveda  
**Curso:** MLY0100 - Machine Learning Parcial 1  
**Institución:** [Tu Institución]

---

## 📖 Referencias

- CRISP-DM Methodology - IBM
- Scikit-learn Documentation
- Brazilian E-commerce Dataset (Olist) - Kaggle
- Best Practices in Data Preprocessing and ML

---

**Última actualización:** 20 de enero de 2026
