# 🚀 Guía de Despliegue - MLY0100 CRISP-DM Pipeline

## 📋 Descripción General

Este proyecto implementa un pipeline completo de CRISP-DM (Comprensión del Negocio, Exploración de Datos, Preparación, Modelado, Evaluación y Despliegue) para análisis de e-commerce brasileño usando:

- **Docker**: Contenerización del ambiente
- **Docker Compose**: Orquestación de servicios (Airflow, PostgreSQL, Python)
- **Airflow**: Orquestación visual del pipeline
- **Python**: Scripts modularizados para cada fase CRISP-DM

---

## 📁 Estructura del Proyecto

```
MLY0100-Parcial-1/
├── docker-compose.yml          # Configuración de servicios Docker
├── Dockerfile                  # Imagen Docker para Python
├── .env                        # Variables de entorno
├── requirements.txt            # Dependencias Python
├── airflow/
│   └── dags/
│       └── mly0100_pipeline.py # DAG principal de Airflow
├── src/
│   └── crispdm/
│       ├── business_understanding.py
│       ├── data_understanding.py
│       ├── data_preparation.py
│       ├── modeling_classification.py
│       ├── modeling_regression.py
│       ├── evaluation.py
│       └── deployment.py
├── logs/                       # Directorio para logs de ejecución
├── data/
│   ├── 01_raw/                # Datos crudos
│   ├── 02_intermediate/       # Datos procesados
│   ├── 03_processed/          # Datos preparados para modelado
│   └── 08_reporting/          # Reportes y resultados
└── README.md
```

---

## 🛠️ Requisitos Previos

### Opción 1: Despliegue con Docker (Recomendado)

- **Docker**: [Descargar](https://www.docker.com/products/docker-desktop/)
- **Docker Compose**: Incluido en Docker Desktop

Verificar instalación:
```powershell
docker --version
docker-compose --version
```

### Opción 2: Ejecución Local (Sin Docker)

- **Python 3.11+**: [Descargar](https://www.python.org/downloads/)
- **Virtual Environment** (recomendado)

---

## 📦 Instalación y Despliegue

### Opción A: Usar Docker Compose (Recomendado)

#### Paso 1: Clonar/Navegar al directorio del proyecto
```powershell
cd C:\Users\goku8\OneDrive\Escritorio\MCHL - copiaaaaa\MLY0100-Parcial-1
```

#### Paso 2: Levantar los servicios
```powershell
docker-compose up -d
```

**Verificar servicios**:
```powershell
docker-compose ps
```

Deberías ver:
- `postgres` (puerto 5432)
- `airflow-webserver` (puerto 8080)
- `airflow-scheduler`
- `python` (servicio de ejecución)

#### Paso 3: Acceder a Airflow
- **URL**: http://localhost:8080
- **Usuario**: admin
- **Contraseña**: admin

#### Paso 4: Activar el DAG
1. Ve a la interfaz de Airflow
2. Busca el DAG: `mly0100_pipeline`
3. Haz clic en el toggle para activarlo
4. Haz clic en "Trigger DAG" para ejecutar

#### Paso 5: Monitorear ejecución
- Visualiza el progreso en Airflow UI
- Los logs estarán en: `logs/` (en tu máquina local)
- Los reportes en: `data/08_reporting/`

---

### Opción B: Ejecutar Localmente (Sin Docker)

#### Paso 1: Crear y activar virtual environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Paso 2: Instalar dependencias
```powershell
pip install -r requirements.txt
```

#### Paso 3: Ejecutar las fases manualmente
```powershell
# Fase 1: Comprensión del Negocio
python src/crispdm/business_understanding.py

# Fase 2: Comprensión de los Datos
python src/crispdm/data_understanding.py

# Fase 3: Preparación de Datos
python src/crispdm/data_preparation.py

# Fase 4a: Modelado Clasificación
python src/crispdm/modeling_classification.py

# Fase 4b: Modelado Regresión
python src/crispdm/modeling_regression.py

# Fase 5: Evaluación
python src/crispdm/evaluation.py

# Fase 6: Despliegue
python src/crispdm/deployment.py
```

O ejecutar el script de inicialización (ver siguiente sección):
```powershell
python run_crisp_dm_pipeline.py
```

---

## 🎯 Script de Inicialización Local

Para simplificar la ejecución local, hemos creado `run_crisp_dm_pipeline.py`:

```powershell
python run_crisp_dm_pipeline.py
```

Este script ejecuta todos los pasos en secuencia y genera reportes.

---

## 📊 Salida Esperada

### Estructura de Logs
```
logs/
├── business_understanding.log
├── data_understanding.log
├── data_preparation.log
├── modeling_classification.log
├── modeling_regression.log
├── evaluation.log
└── deployment.log
```

### Datos Procesados
```
data/
├── 02_intermediate/
│   └── df_cleaned.csv (o archivo procesado)
├── 03_processed/
│   └── df_prepared.csv (datos listos para modelado)
└── 08_reporting/
    └── *.log (reportes finales)
```

---

## 🔧 Solución de Problemas

### 1. Puerto 8080 ya está en uso

```powershell
# Cambiar puerto en docker-compose.yml
# Línea: ports: - "8081:8080"
docker-compose up -d
# Acceder a http://localhost:8081
```

### 2. Error de conexión a PostgreSQL

```powershell
# Reiniciar servicios
docker-compose down
docker-compose up -d
```

### 3. DAG no aparece en Airflow

- Asegurar que `airflow/dags/mly0100_pipeline.py` exista
- Reiniciar el scheduler:
```powershell
docker-compose restart airflow-scheduler
```

### 4. Error de importación de módulos

```powershell
# Dentro del contenedor Python
docker-compose exec python pip install -r requirements.txt
```

### 5. Archivo de datos no encontrado

- Verificar que los archivos CSV estén en `data/02_intermediate/`
- Asegurar que las rutas sean relativas al directorio raíz del proyecto

---

## 🚦 Comandos Útiles de Docker

```powershell
# Ver logs de un servicio
docker-compose logs airflow-webserver
docker-compose logs airflow-scheduler

# Ejecutar comando en contenedor
docker-compose exec python python src/crispdm/business_understanding.py

# Detener todos los servicios
docker-compose down

# Detener y eliminar volúmenes
docker-compose down -v

# Reconstruir imágenes
docker-compose build
```

---

## 📈 Monitoreo en Airflow

### Visualizar DAG
- Graph View: Muestra el flujo de tareas
- Tree View: Muestra la historia de ejecuciones
- Logs: Ver output de cada tarea

### Tareas del Pipeline
1. ✅ **business_understanding**: Define objetivos
2. ✅ **data_understanding**: Explora datos
3. ✅ **data_preparation**: Limpia y prepara
4. ⚙️ **modeling_classification**: Entrena modelos clasificadores (en paralelo)
5. ⚙️ **modeling_regression**: Entrena modelos regressores (en paralelo)
6. ✅ **evaluation**: Compara resultados
7. ✅ **deployment**: Guarda reportes y modelos

---

## 📝 Notas Importantes

- **Sin secretos**: El proyecto usa credenciales por defecto (solo para desarrollo)
- **Almacenamiento local**: Los datos y modelos se guardan localmente, no en nube
- **Ejecución paralela**: Las fases de modelado se ejecutan en paralelo para optimizar tiempo
- **Logs detallados**: Cada fase genera logs independientes para debugging

---

## ✅ Checklist de Despliegue

- [ ] Docker Desktop instalado y corriendo
- [ ] Navegar al directorio del proyecto
- [ ] Ejecutar `docker-compose up -d`
- [ ] Verificar servicios con `docker-compose ps`
- [ ] Acceder a http://localhost:8080
- [ ] Login (admin/admin)
- [ ] Activar DAG `mly0100_pipeline`
- [ ] Trigger manualmente o esperar schedule
- [ ] Monitorear en Graph/Tree View
- [ ] Revisar logs en `logs/` directorio local
- [ ] Verificar reportes en `data/08_reporting/`

---

## 🎓 Referencias

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [CRISP-DM Methodology](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining)

---

## 📞 Soporte

Si encontras problemas, revisa:
1. Los logs: `docker-compose logs [nombre-servicio]`
2. Las rutas: Asegurar que sean relativas al raíz del proyecto
3. Las dependencias: `pip install -r requirements.txt`

¡Éxito en tu despliegue! 🚀
