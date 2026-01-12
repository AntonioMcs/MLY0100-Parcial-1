# Plan de Proyecto: Brazilian E-commerce
## Adaptación del Proyecto según Rúbrica MLY0100

---

## 📋 Resumen del Proyecto

**Dataset:** Brazilian E-commerce (Olist)
**Objetivo:** Análisis exploratorio y preprocesamiento de datos de e-commerce brasileño siguiendo metodología CRISP-DM

---

## 🎯 Cobertura de la Rúbrica

### ✅ Criterio 1: CRISP-DM en Jupyter Notebook (10%)
- **Fase 1: Business Understanding** - Entender el contexto del e-commerce brasileño
- **Fase 2: Data Understanding** - Exploración completa de los datasets
- **Fase 3: Data Preparation** - Limpieza, transformación y preprocesamiento
- **Fase 4: Modeling** - (Para entrega final) Identificación de targets para regresión y clasificación
- **Fase 5: Evaluation** - (Para entrega final) Evaluación de modelos
- **Fase 6: Deployment** - (Para entrega final) Documentación final

### ✅ Criterio 2: Target para Regresión (10%)
**Target propuesto:** `order_total_value` o `price` (valor total del pedido)
- Justificación: Variable numérica continua que permite predecir el valor de compra
- Contexto de negocio: Predecir el valor de pedidos ayuda a planificar inventario y estrategias de pricing

### ✅ Criterio 3: Target para Clasificación (10%)
**Target propuesto:** `order_status_category` (categoría de estado del pedido) o `customer_segment` (segmento de cliente)
- Justificación: Variable categórica que permite clasificar pedidos o clientes
- Contexto de negocio: Clasificar clientes ayuda en estrategias de marketing y retención

### ✅ Criterio 4: Librerías Python ML (10%)
- `numpy` - Operaciones numéricas
- `pandas` - Manipulación de datos
- `scikit-learn` - Preprocesamiento y modelado
- `matplotlib` - Visualización básica
- `seaborn` - Visualización estadística avanzada
- `scipy` - Estadísticas avanzadas (opcional)

### ✅ Criterio 5: Limpieza y Preparación (10%)
- Manejo de valores faltantes
- Tratamiento de outliers
- Normalización de datos categóricos
- Creación de variables derivadas
- Validación de calidad de datos

### ✅ Criterio 6: Documentación del Proceso (10%)
- Comparación de resultados antes/después del preprocesamiento
- Análisis de impacto de las transformaciones
- Documentación de decisiones tomadas

### ✅ Criterio 7: Tratamiento de Outliers y Missing Values (10%)
- Análisis de distribución para decidir estrategia
- Imputación según naturaleza de los datos
- Detección y tratamiento de outliers con IQR o Z-score
- Justificación de métodos elegidos

### ✅ Criterio 8: Estadísticos de Tendencia Central y Dispersión (10%)
- Media, mediana, moda
- Desviación estándar, varianza, rango intercuartílico
- Uso de estos estadísticos para explicar los datos

### ✅ Criterio 9: Normalización/Estandarización (10%)
- Análisis de distribuciones (normal, sesgada, etc.)
- Aplicación de StandardScaler o MinMaxScaler según distribución
- Justificación de la técnica elegida

### ✅ Criterio 10: Documentación con Markdown (10%)
- Cada sección documentada con markdown
- Justificación de cada técnica utilizada
- Explicación del razonamiento detrás de cada decisión

---

## 📊 Estructura del Notebook Principal

### **Fase 1: Business Understanding**
1. Contexto del negocio
2. Objetivos del proyecto
3. Preguntas de negocio a responder
4. Definición de targets:
   - Regresión: `order_total_value` (valor total del pedido)
   - Clasificación: `order_status_category` o `customer_segment`

### **Fase 2: Data Understanding**
1. Carga de datos
2. Análisis de estructura:
   - Dimensiones (filas, columnas)
   - Tipos de datos
   - Información general
3. Estadísticos descriptivos:
   - Tendencia central (media, mediana, moda)
   - Dispersión (desviación estándar, varianza, IQR)
4. Análisis de entidades:
   - Distribuciones de variables numéricas
   - Distribuciones de variables categóricas
   - Detección de distribuciones (normal, sesgada, etc.)
5. Análisis de calidad:
   - Valores faltantes por columna
   - Duplicados
   - Inconsistencias
6. Visualizaciones:
   - Histogramas
   - Boxplots
   - Mapas de calor de correlación
   - Gráficos de barras para categóricas

### **Fase 3: Data Preparation**
1. Tratamiento de valores faltantes:
   - Análisis de patrones de missing values
   - Estrategia de imputación según tipo de variable
   - Justificación de métodos
2. Tratamiento de outliers:
   - Detección con IQR y Z-score
   - Análisis de impacto
   - Decisión: eliminar, capar o mantener
   - Justificación
3. Limpieza de variables categóricas:
   - Corrección de errores de captura
   - Agrupación de categorías raras
   - Normalización de formatos
4. Creación de variables derivadas:
   - Variables de tiempo (día de semana, mes, etc.)
   - Variables de agregación
   - Variables de interacción
5. Encoding de variables categóricas:
   - One-hot encoding
   - Label encoding (si aplica)
6. Escalamiento/Normalización:
   - Análisis de distribuciones
   - Decisión: StandardScaler vs MinMaxScaler
   - Aplicación y verificación
7. Guardado de datos procesados

---

## 📁 Estructura de Archivos Propuesta

```
MLY0100-Parcial-1/
├── notebooks/
│   └── 01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb  # Notebook principal
├── data/
│   ├── 01_raw/                    # Datasets originales (cuando se suban)
│   ├── 02_intermediate/           # Datos con limpieza básica
│   ├── 03_processed/              # Datos finales preprocesados
│   └── 08_reporting/               # Figuras y reportes
├── src/
│   ├── preprocessing.py            # Funciones de preprocesamiento
│   ├── visualization.py           # Funciones de visualización
│   └── features.py                # Creación de variables derivadas
├── conf/
│   └── parameters.yml              # Parámetros configurables
└── README.md                       # Documentación del proyecto
```

---

## 🔄 Flujo de Trabajo

1. **Carga de datos** → `data/01_raw/`
2. **Análisis exploratorio** → Identificar problemas y patrones
3. **Limpieza básica** → Guardar en `data/02_intermediate/`
4. **Preprocesamiento avanzado** → Guardar en `data/03_processed/`
5. **Visualizaciones** → Guardar en `data/08_reporting/`

---

## 📝 Checklist de Entrega (Fases 1-3 CRISP-DM)

### Business Understanding
- [ ] Contexto del negocio documentado
- [ ] Objetivos claramente definidos
- [ ] Targets identificados (regresión y clasificación)

### Data Understanding
- [ ] Análisis de estructura de datos
- [ ] Estadísticos descriptivos (tendencia central y dispersión)
- [ ] Análisis de distribuciones
- [ ] Visualizaciones exploratorias
- [ ] Análisis de calidad de datos

### Data Preparation
- [ ] Tratamiento de missing values (justificado)
- [ ] Tratamiento de outliers (justificado)
- [ ] Limpieza de variables categóricas
- [ ] Encoding aplicado
- [ ] Normalización/estandarización aplicada (justificada)
- [ ] Datos guardados en formato procesado

### Documentación
- [ ] Todo documentado con Markdown
- [ ] Justificaciones de técnicas utilizadas
- [ ] Comparación antes/después del preprocesamiento

---

## 🚀 Próximos Pasos

1. **Esperar dataset** de brazilian-ecommerce
2. **Cargar y explorar** los datos disponibles
3. **Ajustar targets** según los datos reales
4. **Implementar** el notebook siguiendo este plan
5. **Validar** que se cumplan todos los criterios de la rúbrica

---

## 📚 Referencias

- CRISP-DM Methodology
- Brazilian E-commerce Dataset (Olist) - Kaggle
- Best Practices in Data Preprocessing
- Scikit-learn Documentation
