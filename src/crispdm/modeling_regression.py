
import pandas as pd
from pathlib import Path
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def main():
    mensaje = []
    mensaje.append("Fase 4: Modelado (Regresión) - Entrenamiento y evaluación")
    os.makedirs("logs", exist_ok=True)
    data_path = Path("data/03_processed/df_prepared.csv")
    if not data_path.exists():
        mensaje.append("No existe el archivo de datos preparados para regresión.")
        with open("logs/modeling_regression.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    df = pd.read_csv(data_path)
    target = 'order_total_value' if 'order_total_value' in df.columns else None
    if not target:
        mensaje.append("No se encontró la variable objetivo de regresión.")
        with open("logs/modeling_regression.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    reg = RandomForestRegressor(random_state=42)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mensaje.append(f"MAE: {mae:.2f}")
    mensaje.append(f"MSE: {mse:.2f}")
    mensaje.append(f"R2 Score: {r2:.4f}")
    # Guardar log y métricas
    with open("logs/modeling_regression.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
