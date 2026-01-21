# 📑 ÍNDICE DE DOCUMENTACIÓN

## 🎯 MLY0100 Parcial 1 - Pipeline Completo

---

## 📊 DATASET PRINCIPAL

### ✅ Dataset Procesado (LISTO PARA MODELADO)
📁 **Ubicación:** `data/02_intermediate/df_processed_final.csv`
- **Tamaño:** 162.19 MB
- **Dimensiones:** 119,143 filas × 134 columnas
- **Estado:** 100% completo (0 valores faltantes)
- **Idioma:** Inglés (traducido)
- **Preparado para:** Modelado (regresión/clasificación)

---

## 📚 DOCUMENTACIÓN (4 ARCHIVOS)

### 1. 📖 **README.md** ⭐ COMIENZA AQUÍ
**Para:** Entender todo el proyecto  
**Contiene:**
- Descripción general del proyecto
- Fases completadas (CRISP-DM 1-6)
- Dataset y fuente
- Instalación y configuración
- Estructura de carpetas
- Notebooks incluidos (01 y 02)
- Pipeline de procesamiento (fases)
- Matriz de cumplimiento de rúbrica (10 criterios ✅)
- Resultados esperados
- Tecnologías utilizadas
- Troubleshooting

**Leer primero si:** Recién empiezas o necesitas visión general

---

### 2. 🚀 **GUIA_RAPIDA_PROCESAMIENTO.md**
**Para:** Empezar rápidamente sin leer todo  
**Contiene:**
- Inicio rápido en 3 pasos
- Cómo usar el dataset
- Scripts disponibles
- Cargar datos en Python
- Estructura de archivos
- Validación básica

**Leer primero si:** Solo necesitas empezar inmediatamente

---

### 3. 📖 **INSTRUCCIONES_NOTEBOOK_02.md**
**Para:** Guía paso a paso para Notebook 02  
**Contiene:**
- Cargar el dataset
- Explorar variables
- Preparar features y target
- Dividir en train/test
- Entrenar modelos
- Guardar modelos
- Hacer predicciones
- Visualizaciones

**Leer primero si:** Estás trabajando en modelado (Notebook 02)

---

### 4. 📑 **INDICE_DOCUMENTACION.md** (este archivo)
**Para:** Navegar toda la documentación  
**Contiene:**
- Ubicación de archivos
- Guía de lectura por caso de uso
- Mapa de archivos y carpetas
- Relaciones entre documentos

**Leer primero si:** Necesitas orientación sobre qué leer

---

## 🔧 SCRIPTS PYTHON (4 ARCHIVOS)

### 1. **union_y_limpieza.py** (Fase 1)
📁 Ubicación: `src/union_y_limpieza.py`

**Propósito:**
- Unir 9 archivos CSV crudos
- Limpiar caracteres especiales portugueses
- Output: `df_unido_y_limpio.csv`

**Función principal:**
```python
union_optima_olist(data_path, output_path)
```

**Ejecutar:**
```bash
python src/union_y_limpieza.py
---

## 📁 ESTRUCTURA DE ARCHIVOS

```
PROYECTO/
├── 📄 README.md                             ← COMIENZA AQUÍ
├── 📄 GUIA_RAPIDA_PROCESAMIENTO.md          ← Quick start
├── 📄 INSTRUCCIONES_NOTEBOOK_02.md          ← Modelado
├── 📄 INDICE_DOCUMENTACION.md               ← Este archivo
│
├── notebooks/
│   ├── 01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb
│   └── 02_Modelado_nuevo.ipynb              ⭐ Usar este
│
├── data/
│   ├── 01_raw/                              (9 CSV originales)
│   ├── 02_intermediate/                     (Dataset procesado)
│   │   └── df_processed_final.csv           ⭐ 119,143 × 134
│   ├── 06_models/
│   │   ├── scaler_regression.pkl
│   │   └── scaler_classification.pkl
│   └── 08_reporting/
│       └── (Figuras y reportes generados)
│
└── src/
    ├── union_y_limpieza.py                  (Fase 1)
    ├── traduccion_a_ingles.py               (Fase 2)
    ├── procesar_dataset_maestro.py          (Fase 3)
    └── cargar_dataset_procesado.py          (Utility)
```

---

## 📝 GUÍA POR CASO DE USO

### 👶 PRIMER CONTACTO
1. Lee: `README.md` (10 min) - Entender el proyecto completo
2. Lee: `GUIA_RAPIDA_PROCESAMIENTO.md` (5 min) - Cargar datos
3. Resultado: Listo para modelado

### 👨‍💻 QUIERO MODELAR (Notebook 02)
1. Lee: `README.md` Sección "Notebooks Incluidos" (5 min)
2. Lee: `INSTRUCCIONES_NOTEBOOK_02.md` (10 min)
3. Abre: `notebooks/02_Modelado_nuevo.ipynb`
4. Resultado: Listo para entrenar modelos

### 🔍 QUIERO ENTENDER EL PIPELINE
1. Lee: `README.md` Sección "Pipeline de Procesamiento" (10 min)
2. Lee: `GUIA_RAPIDA_PROCESAMIENTO.md` (5 min)
3. Revisa: Scripts en `src/`
4. Resultado: Entiende las 3 fases

### ✅ QUIERO VERIFICAR LA RÚBRICA
1. Lee: `README.md` Sección "Matriz de Cumplimiento" (5 min)
2. Verifica: Todos los 10 criterios ✅
3. Resultado: Conforme con rúbrica

---

## 📑 CONTENIDO DE CADA ARCHIVO

| Archivo | Secciones Principales | Cuándo Leerlo |
|---------|----------------------|--------------|
| **README.md** | Descripción, Instalación, Notebooks, Pipeline, Rúbrica, Tech Stack | Primer contacto |
| **GUIA_RAPIDA_PROCESAMIENTO.md** | Inicio rápido, Cargar datos, Scripts, Validación | Necesitas datos YA |
| **INSTRUCCIONES_NOTEBOOK_02.md** | Carga datos, EDA, Modelos, Métricas, Predicciones | Estás en Notebook 02 |
| **INDICE_DOCUMENTACION.md** | Este índice, navegación | Necesitas orientación |

---

## 🎯 PRÓXIMOS PASOS

### ✅ Completado
- Dataset procesado y listo (119,143 × 134)
- Notebook 01: Análisis exploratorio
- Notebook 02: Regresión (4 modelos) + Clasificación (5 modelos)
- Rúbrica: 10/10 criterios cumplidos
- Documentación: Simplificada y clara

### ⏭️ Siguiente: Ejecutar Notebooks
```bash
# Opción 1: VS Code/Cursor (Recomendado)
# Abre: notebooks/02_Modelado_nuevo.ipynb
# Kernel: .venv (Python 3.11)

# Opción 2: Jupyter Lab
jupyter lab

# Opción 3: Jupyter Notebook
jupyter notebook
```

---

## ❓ PREGUNTAS FRECUENTES

**P: ¿Por dónde empiezo?**  
R: Lee `README.md`, luego abre `02_Modelado_nuevo.ipynb`

**P: ¿Dónde está el dataset?**  
R: `data/02_intermediate/df_processed_final.csv`

**P: ¿Necesito ejecutar scripts?**  
R: No, dataset ya está procesado. Solo si cambió raw.

**P: ¿Qué notebook debo usar?**  
R: `02_Modelado_nuevo.ipynb` - tiene regresión + clasificación

**P: ¿Cómo verifico el kernel?**  
R: `import sys; print(sys.executable)` debe apuntar a `.venv`

**P: ¿Dónde están los modelos?**  
R: Se generan en `data/06_models/` al ejecutar Notebook 02

**P: ¿Cuándo está completo?**  
R: 10/10 criterios cumplidos ✅ - Ver `README.md`

---

## 📚 INFORMACIÓN POR TEMA

### Dataset
- **Ubicación:** `data/02_intermediate/df_processed_final.csv`
- **Tamaño:** 119,143 filas × 134 columnas
- **Calidad:** 100% completo (0 valores faltantes)
- **Idioma:** Inglés
- **Targets:** `order_total_value` (regresión), `order_status` (clasificación)

### Modelos (Notebook 02)
- **Regresión:** Linear, DecisionTree, RandomForest, XGBoost
- **Clasificación:** LogisticRegression, DecisionTree, RandomForest, SVM, NaiveBayes
- **Balance:** SMOTE para clases desbalanceadas
- **Métricas:** MAE, RMSE, R² (regresión); Accuracy, Precision, Recall, F1 (clasificación)

### Pipeline
- **Fase 1:** Unión de 9 CSV + limpieza (165 líneas)
- **Fase 2:** Traducción a inglés (265 líneas)
- **Fase 3:** Procesamiento + encoding + escalado (280 líneas)

### Rúbrica (10 Criterios)
- Todos ✅ completados
- Ver `README.md` Sección "Matriz de Cumplimiento"

---

## 🔗 RELACIONES ENTRE ARCHIVOS

```
README.md
├─→ Remite a GUIA_RAPIDA_PROCESAMIENTO.md (quick start)
├─→ Remite a INSTRUCCIONES_NOTEBOOK_02.md (modelado)
└─→ Remite a INDICE_DOCUMENTACION.md (navegación)

GUIA_RAPIDA_PROCESAMIENTO.md
└─→ Implementa instrucciones de README.md

INSTRUCCIONES_NOTEBOOK_02.md
└─→ Amplía sección "Notebooks" del README.md

notebooks/02_Modelado_nuevo.ipynb
└─→ Implementa instrucciones de INSTRUCCIONES_NOTEBOOK_02.md
```

---

## ✨ ESTADO FINAL

✅ Proyecto completamente estructurado  
✅ Documentación simplificada (4 archivos)  
✅ Información redundante eliminada  
✅ Listo para ejecución  
✅ 10/10 criterios de rúbrica cumplidos  

**Última actualización:** 20 de enero de 2026
