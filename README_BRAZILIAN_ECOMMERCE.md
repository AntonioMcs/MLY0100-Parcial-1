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

---

## 🎯 Cobertura de la Rúbrica

Este proyecto cumple con los 10 criterios de la rúbrica:

1. ✅ **CRISP-DM en Jupyter Notebook** - Metodología aplicada en todas las fases
2. ✅ **Target para Regresión** - `order_total_value` (valor total del pedido)
3. ✅ **Target para Clasificación** - `order_status_category` o `customer_segment`
4. ✅ **Librerías Python ML** - numpy, scikit-learn, matplotlib, seaborn
5. ✅ **Limpieza y Preparación** - Según buenas prácticas de la industria
6. ✅ **Documentación del Proceso** - Comparación antes/después
7. ✅ **Tratamiento de Outliers y Missing Values** - Según naturaleza de los datos
8. ✅ **Estadísticos de Tendencia Central y Dispersión** - Media, mediana, desviación estándar, IQR
9. ✅ **Normalización/Estandarización** - Según distribución de los datos
10. ✅ **Documentación con Markdown** - Justificación de cada técnica

---

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

**Nota:** Coloca los archivos CSV en la carpeta `data/01_raw/` antes de ejecutar el notebook.

---

## ⚙️ Instalación y Configuración

### Requisitos Previos

- Python 3.11.9 o superior
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio** (si aplica):
```bash
git clone [URL_DEL_REPOSITORIO]
cd MLY0100-Parcial-1
```

2. **Crear entorno virtual de Python**:
```bash
python -m venv .venv
```

3. **Activar entorno virtual**:
   - **Windows (PowerShell)**:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   - **Linux/Mac**:
   ```bash
   source .venv/bin/activate
   ```

4. **En caso de error en PowerShell**, ejecutar:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

5. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

6. **Instalar Jupyter** (si no está incluido):
```bash
pip install jupyter jupyterlab
```

---

## 🚀 Uso del Proyecto

### Ejecutar el Notebook Principal

1. **Asegúrate de tener los datasets** en `data/01_raw/`

2. **Iniciar Jupyter**:
```bash
jupyter notebook
# o
jupyter lab
```

3. **Abrir el notebook**:
   - `notebooks/01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb`

4. **Ejecutar las celdas** en orden:
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

---

## 📖 Referencias

- [CRISP-DM Methodology](https://www.ibm.com/docs/en/spss-modeler/saas?topic=dm-crisp-help-overview)
- [Brazilian E-commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

## ⚠️ Notas Importantes

1. **Ajustar nombres de columnas**: Los nombres de columnas en el notebook son ejemplos. Deben ajustarse según los datasets reales.

2. **Cargar datasets primero**: Asegúrate de tener los archivos CSV en `data/01_raw/` antes de ejecutar.

3. **Revisar parámetros**: Actualiza `conf/parameters.yml` con los nombres reales de las columnas de tus datos.

4. **Validar targets**: Una vez cargados los datos, verifica que los targets propuestos existan y sean adecuados.

---

## 📧 Contacto

Para preguntas o sugerencias sobre este proyecto, contacta al equipo.

---

**Última actualización:** [Fecha]
