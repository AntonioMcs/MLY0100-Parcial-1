# Proyecto Parcial 1 - MLY0100
**Tema:** Análisis y Preprocesamiento de Datos de E-commerce Brasileño  
**Integrantes:** Antonio Sepulveda  
**Fecha:** 13/01/2026

---

## 📋 Descripción del Proyecto

Este proyecto realiza un análisis exploratorio y preprocesamiento de datos del e-commerce brasileño (Olist) siguiendo la metodología **CRISP-DM** y cumpliendo con todos los criterios de la rúbrica del curso MLY0100.

### Objetivos

1. **Análisis Exploratorio**: Comprender la estructura, calidad y características de los datos
2. **Preprocesamiento**: Limpiar, transformar y preparar los datos para modelado
3. **Identificación de Targets**: Definir variables objetivo para regresión y clasificación
4. **Documentación**: Documentar todo el proceso con justificaciones técnicas


## 📊 Dataset

**Dataset:** Brazilian E-commerce (Olist)  
**Fuente:** Kaggle - [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

### Archivos del Dataset (típicamente incluye):

- `olist_orders_dataset.csv` - Información de pedidos
- `olist_order_items_dataset.csv` - Items de cada pedido
- `olist_customers_dataset.csv` - Información de clientes
- `olist_products_dataset.csv` - Información de productos
- `olist_sellers_dataset.csv` - Información de vendedores
- `olist_order_payments_dataset.csv` - Información de pagos
- `olist_order_reviews_dataset.csv` - Reseñas de pedidos

**Nota:** Coloca los archivos CSV en la carpeta `mly0100parcial-kedro/data/01_raw/` antes de ejecutar el notebook.

---

## ⚙️ Instalación y Configuración

### Requisitos Previos

- Python 3.11.9 o superior
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio** (si aplica):
```bash
git clone https://github.com/AntonioMcs/MLY0100-Parcial-1/tree/modificacion-para-brazil
cd MLY0100-Parcial-1
```

2. **Crear entorno virtual de Python**:
```bash
python -m venv .venv
```
   
   Si tienes Python 3.11 específicamente:
   ```bash
   python3.11 -m venv .venv
   ```

3. **Activar entorno virtual**:
   - **Windows (PowerShell)**:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   
   Si obtienes un error de política de ejecución:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Luego intenta activar de nuevo.
   
   - **Windows (CMD)**:
   ```cmd
   .venv\Scripts\activate.bat
   ```
   
   - **Linux/Mac**:
   ```bash
   source .venv/bin/activate
   ```

4. **Verifica que estás en el entorno virtual**:
   Deberías ver `(.venv)` al inicio de tu prompt:
   ```
   (.venv) PS C:\Users\...>
   ```

5. **Instalar dependencias**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

6. **Verificar la instalación**:
```bash
python -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('Todas las librerías instaladas correctamente')"
```

---

## 🚀 Uso del Proyecto

### Ejecutar el Notebook Principal

1. **Asegúrate de tener los datasets** en `mly0100parcial-kedro/data/01_raw/`

2. **Asegúrate de estar en el entorno virtual activado**

3. **Ejecutar el notebook** (elige una opción):

   **Opción A: Desde VS Code / Cursor (Recomendado)**
   - Abre el notebook `notebooks/01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb`
   - Selecciona el kernel: haz clic en el selector de kernel (arriba a la derecha) → "Select Another Kernel" → elige el intérprete de Python de tu entorno virtual (`.venv`)
   - Ejecuta las celdas con `Shift + Enter`

   **Opción B: Desde Jupyter Lab**
   ```bash
   jupyter lab
   ```
   - Se abrirá en tu navegador
   - Navega al notebook y selecciona el kernel correcto (`.venv`)

   **Opción C: Desde Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

4. **Verificar que el kernel correcto está seleccionado**:
   Ejecuta esta celda en el notebook:
   ```python
   import sys
   print(f"Python: {sys.version}")
   print(f"Ubicación: {sys.executable}")
   ```
   Deberías ver la ruta de `.venv`, no la de Python del sistema.

5. **Ejecutar las celdas** en orden:
   - El notebook está estructurado siguiendo CRISP-DM
   - Cada sección está documentada con Markdown
   - Las celdas de código incluyen comentarios explicativos

### Estructura del Notebook

El notebook sigue las **primeras 3 fases de CRISP-DM**:

1. **Fase 1: Business Understanding**
   - Contexto del negocio
   - Objetivos y preguntas de negocio
   - Definición de targets

2. **Fase 2: Data Understanding**
   - Carga y combinación de datos
   - Análisis de estructura
   - Estadísticos descriptivos
   - Análisis de distribuciones
   - Análisis de missing values
   - Análisis de outliers
   - Análisis de variables categóricas
   - Análisis de correlaciones

3. **Fase 3: Data Preparation**
   - Tratamiento de missing values
   - Tratamiento de outliers
   - Limpieza de variables categóricas
   - Creación de variables derivadas
   - Encoding de variables categóricas
   - Normalización/estandarización
   - Comparación antes/después

---

## 🛠️ Framework y Herramientas

- **Lenguaje**: Python 3.11.9
- **IDE**: VS Code / Jupyter Lab
- **Control de versiones**: Git
- **Notebooks**: Jupyter
- **Metodología**: CRISP-DM
- **Configuración**: Parámetros en `conf/parameters.yml`

---

## 📚 Librerías Utilizadas

Instalar en el entorno virtual con `pip install -r requirements.txt`:

- **pandas** → Manipulación y análisis de datos
- **numpy** → Cálculos numéricos y operaciones matemáticas
- **matplotlib** → Visualización básica de datos
- **seaborn** → Visualización estadística avanzada
- **scikit-learn** → Preprocesamiento, encoding y escalado
- **scipy** → Estadísticas avanzadas (skewness, etc.)
- **joblib** → Guardar transformadores (scalers)

---

## 📂 Estructura de Archivos

```
MLY0100-Parcial-1/
├── data/
│   ├── 01_raw/                    # Datasets originales (CSV)
│   ├── 02_intermediate/           # Datos con limpieza básica
│   ├── 03_processed/              # Datos finales preprocesados
│   ├── 06_models/                  # Modelos y transformadores guardados
│   └── 08_reporting/               # Figuras y reportes exportados
│
├── notebooks/
│   ├── 01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb  # Notebook principal
│   └── 02_Modelado.ipynb          # Notebook de modelado (futuro)
│
├── src/
│   ├── preprocessing.py           # Funciones de preprocesamiento
│   ├── visualization.py            # Funciones de visualización
│   └── features.py                 # Creación de variables derivadas
│
├── conf/
│   └── parameters.yml              # Parámetros configurables
│
├── PLAN_PROYECTO_BRAZILIAN_ECOMMERCE.md  # Plan detallado del proyecto
├── README.md                       # Este archivo
└── requirements.txt                # Dependencias del proyecto
```

---

## 📝 Targets Definidos

### Target para Regresión
**Variable:** `order_total_value` (valor total del pedido)

**Justificación:**
- Variable numérica continua
- Permite predecir el valor de compra
- Útil para planificación de inventario y estrategias de pricing

### Target para Clasificación
**Variable:** `order_status_category` o `customer_segment`

**Justificación:**
- Variable categórica
- Permite clasificar pedidos o clientes
- Útil para estrategias de marketing segmentadas

**Nota:** Los targets específicos se ajustarán una vez que se carguen y exploren los datos reales.

---

## 🔍 Funciones Auxiliares

El proyecto incluye funciones auxiliares en `src/`:

### `preprocessing.py`
- `load_csv()` - Cargar archivos CSV
- `save_csv()` - Guardar DataFrames
- `missing_summary()` - Resumen de valores faltantes
- `detect_outliers_iqr()` - Detectar outliers con IQR
- `cap_outliers()` - Limitar valores extremos
- `impute_numeric_median()` - Imputar numéricas con mediana
- `impute_categorical_mode()` - Imputar categóricas con moda

### `visualization.py`
- `hist_plot()` - Histogramas
- `box_plot()` - Boxplots
- `corr_heatmap()` - Mapas de calor de correlación

### `features.py`
- `create_ecommerce_features()` - Crear variables derivadas para e-commerce
- `spend_category()` - Crear categorías de gasto
- `age_group()` - Agrupar edades en rangos

---

## 📊 Resultados Esperados

Después de ejecutar el notebook, se generarán:

1. **Datos procesados** en `data/03_processed/df_processed_final.csv`
2. **Visualizaciones** guardadas en `data/08_reporting/`:
   - Distribuciones de variables numéricas
   - Análisis de missing values
   - Análisis de outliers
   - Distribuciones categóricas
   - Matriz de correlación
3. **Comparación antes/después** en `data/08_reporting/comparacion_preprocesamiento.csv`
4. **Transformadores guardados** en `data/06_models/`:
   - `scaler_standard.pkl`
   - `scaler_minmax.pkl`

---

## 🎓 Metodología CRISP-DM

Este proyecto sigue la metodología **CRISP-DM** (Cross-Industry Standard Process for Data Mining):

1. **Business Understanding** ✅
2. **Data Understanding** ✅
3. **Data Preparation** ✅
4. **Modeling** (Futuro)
5. **Evaluation** (Futuro)
6. **Deployment** (Futuro)





## 📖 Referencias

- [CRISP-DM Methodology](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview)
- [Brazilian E-commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
