
import pandas as pd
from pathlib import Path
import os

def main():
    mensaje = []
    mensaje.append("Fase 3: Preparación de los datos - Limpieza y transformación")
    os.makedirs("logs", exist_ok=True)
    base_path = Path("data/02_intermediate")
    files = list(base_path.glob("*.csv"))
    if not files:
        mensaje.append("No hay archivos CSV en data/02_intermediate")
        with open("logs/data_preparation.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    df = pd.read_csv(files[0])
    # Imputación de nulos numéricos
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        df[col].fillna(df[col].median(), inplace=True)
    # Imputación de nulos categóricos
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        mode_value = df[col].mode()[0] if not df[col].mode().empty else 'Unknown'
        df[col].fillna(mode_value, inplace=True)
    mensaje.append("Nulos imputados correctamente.")
    # Guardar datos preparados
    output_path = Path("data/03_processed/df_prepared.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    mensaje.append(f"Datos preparados guardados en: {output_path}")

    with open("logs/data_preparation.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
