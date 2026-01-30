
import pandas as pd
from pathlib import Path
import os

def main():
    mensaje = []
    mensaje.append("Fase 2: Comprensión de los datos - Exploración inicial")
    os.makedirs("logs", exist_ok=True)
    base_path = Path("data/02_intermediate")
    files = list(base_path.glob("*.csv"))
    if not files:
        mensaje.append("No hay archivos CSV en data/02_intermediate")
        with open("logs/data_understanding.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    df = pd.read_csv(files[0])
    mensaje.append(f"Archivo cargado: {files[0].name}")
    mensaje.append(f"Dimensiones: {df.shape[0]:,} filas × {df.shape[1]} columnas")
    mensaje.append(f"Primeras columnas: {list(df.columns[:5])} ...")
    mensaje.append(f"Tipos de datos: {df.dtypes.value_counts().to_dict()}")
    mensaje.append(f"Valores faltantes: {df.isnull().sum().sum()}")

    with open("logs/data_understanding.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
