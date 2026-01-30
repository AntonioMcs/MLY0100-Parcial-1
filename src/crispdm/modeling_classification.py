
import pandas as pd
from pathlib import Path
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

def main():
    mensaje = []
    mensaje.append("Fase 4: Modelado (Clasificación) - Entrenamiento y evaluación")
    os.makedirs("logs", exist_ok=True)
    data_path = Path("data/03_processed/df_prepared.csv")
    if not data_path.exists():
        mensaje.append("No existe el archivo de datos preparados para clasificación.")
        with open("logs/modeling_classification.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    df = pd.read_csv(data_path)
    target = 'order_status_category' if 'order_status_category' in df.columns else None
    if not target:
        mensaje.append("No se encontró la variable objetivo de clasificación.")
        with open("logs/modeling_classification.log", "w", encoding="utf-8") as f:
            for linea in mensaje:
                f.write(linea + "\n")
        for linea in mensaje:
            print(linea)
        return
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    mensaje.append(f"Accuracy: {acc:.4f}")
    mensaje.append(f"Precision: {prec:.4f}")
    mensaje.append(f"Recall: {rec:.4f}")
    mensaje.append(f"F1 Score: {f1:.4f}")
    mensaje.append("Reporte de clasificación:")
    mensaje.append(str(classification_report(y_test, y_pred)))
    # Guardar log y métricas
    with open("logs/modeling_classification.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
