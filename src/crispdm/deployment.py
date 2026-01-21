
import shutil
from pathlib import Path

def main():
    mensaje = []
    mensaje.append("Fase 6: Despliegue - Guardar modelos y resultados")
    # Simulación de despliegue: copiar logs a carpeta de reporting
    reporting_path = Path("data/08_reporting")
    reporting_path.mkdir(parents=True, exist_ok=True)
    for log_file in ["business_understanding.log", "data_understanding.log", "data_preparation.log", "modeling_classification.log", "modeling_regression.log", "evaluation.log"]:
        src = Path(f"logs/{log_file}")
        dst = reporting_path / log_file
        if src.exists():
            shutil.copy(src, dst)
            mensaje.append(f"Log {log_file} copiado a {dst}")
        else:
            mensaje.append(f"No existe {log_file} para copiar.")
    mensaje.append("Despliegue simulado completado. Revisar data/08_reporting para resultados.")
    with open("logs/deployment.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
