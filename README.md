Parcial 1 – MLY0100

Este proyecto corresponde a la Evaluación Parcial 1 del curso Machine Learning (MLY0100).
Se desarrolla en formato Jupyter Notebook, aplicando las fases iniciales de la metodología CRISP-DM:

Entendimiento del negocio

Entendimiento de los datos

Preparación y preprocesamiento

Dataset utilizado

Link del dataset base: Customer Personality Analysis

Targets definidos:

Regresión: total_spent (gasto total del cliente)

Clasificación: spend_category (segmento del cliente: Low, Medium, High)

⚙️ Etapa de instalación

Una vez clonado el repositorio y cargado el proyecto, ejecutar los siguientes pasos:
1. Clonar el repositorio:

git clone https://github.com/AntonioMcs/MLY0100-Parcial-1.git
cd MLY0100-Parcial-1


2. Crear entorno virtual de Python:

python -m venv .venv

3. Activar entorno virtual (en PowerShell - Windows):

.\.venv\Scripts\Activate.ps1

4. En caso de error, ejecutar:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

5. Instalar dependencias:

pip install -r requirements.txt

6. Ejecutar notebooks principales:

notebooks/01_EDA.ipynb

notebooks/02_Preprocesamiento.ipynb

🛠️ Framework y Herramientas
Lenguaje: Python 3.11.9

IDE: VS Code

Control de versiones: Git

Notebooks: Jupyter

Soporte estructural: configuración de parámetros en conf/

📚 Librerías utilizadas
Instalar en el entorno virtual con pip install:

pandas → manipulación de datos

numpy → cálculos numéricos

matplotlib → visualización básica

seaborn → visualización estadística

scikit-learn → preprocesamiento, encoding y escalado

joblib → guardar transformadores

📂 Estructura de archivos
data/01_raw/ → dataset original en CSV

data/02_intermediate/ → datos intermedios con limpieza de nulos y outliers

data/03_processed/ → dataset final con encoding y escalado

data/08_reporting/ → figuras y reportes exportados

notebooks/ → Jupyter Notebooks (EDA y Preprocesamiento)

src/ → scripts Python con funciones auxiliares

preprocessing.py → imputación, limpieza, outliers

visualization.py → funciones de gráficos

features.py → creación de variables derivadas

conf/parameters.yml → parámetros configurables (columnas numéricas, categóricas, thresholds)