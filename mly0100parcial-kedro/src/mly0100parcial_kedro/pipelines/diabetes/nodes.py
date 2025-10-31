import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error

# ==========================
# 🧹 1. Limpieza de datos
# ==========================
def clean_diabetes_data(diabetes_raw: pd.DataFrame) -> pd.DataFrame:
    """Limpia y prepara los datos del dataset de diabetes."""
    df = diabetes_raw.copy()

    # Eliminar columnas irrelevantes si existen
    cols_to_drop = [col for col in df.columns if "unnamed" in col.lower()]
    df.drop(columns=cols_to_drop, inplace=True, errors="ignore")

    # Eliminar filas con valores nulos
    df.dropna(inplace=True)

    return df


# ==========================
# 🔀 2. División de datos
# ==========================
def split_diabetes_data(diabetes_cleaned: pd.DataFrame, params: dict):
    """Divide los datos en conjuntos de entrenamiento y prueba de forma estratificada."""
    X = diabetes_cleaned.drop("Diabetes_binary", axis=1)
    y = diabetes_cleaned["Diabetes_binary"]

    test_size = params.get("test_size", 0.2)
    random_state = params.get("random_state", 42)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=random_state,
        stratify=y  # ✅ asegura distribución balanceada de clases
    )

    return X_train, X_test, y_train, y_test


# ==========================
# 🤖 3. Entrenamiento del modelo
# ==========================
def train_diabetes_model(X_train: pd.DataFrame, y_train: pd.Series):
    """Entrena un modelo de clasificación para predecir diabetes."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


# ==========================
# 📊 4. Evaluación del modelo
# ==========================
def evaluate_diabetes_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> pd.DataFrame:
    """Evalúa el modelo y devuelve métricas clave."""
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    # Usa .get() para evitar errores si una clase falta
    precision_0 = report.get("0", {}).get("precision", None)
    recall_0 = report.get("0", {}).get("recall", None)
    precision_1 = report.get("1", {}).get("precision", None)
    recall_1 = report.get("1", {}).get("recall", None)

    results = pd.DataFrame({
        "accuracy": [acc],
        "mse": [mse],
        "precision_0": [precision_0],
        "recall_0": [recall_0],
        "precision_1": [precision_1],
        "recall_1": [recall_1],
    })

    print("✅ Modelo evaluado correctamente.")
    print(f"Accuracy: {acc:.4f} | MSE: {mse:.4f}")

    return results

# ==========================
# 📉 5. Visualización de resultados
# ==========================
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def visualize_diabetes_results(model, X_test, y_test):
    """Genera gráficos visuales del modelo: matriz de confusión y métricas."""
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)

    # === Matriz de Confusión ===
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicho")
    plt.ylabel("Real")
    plt.title("Matriz de Confusión - Diabetes")
    plt.tight_layout()
    plt.savefig("data/08_reporting/confusion_matrix_diabetes.png")
    plt.close()

    # === Gráfico de métricas ===
    from sklearn.metrics import classification_report, accuracy_score
    report = classification_report(y_test, y_pred, output_dict=True)
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision_0": report.get("0", {}).get("precision", 0),
        "Recall_0": report.get("0", {}).get("recall", 0),
        "Precision_1": report.get("1", {}).get("precision", 0),
        "Recall_1": report.get("1", {}).get("recall", 0),
    }

    plt.figure(figsize=(6, 4))
    plt.bar(metrics.keys(), metrics.values(), color="skyblue")
    plt.title("Métricas del modelo de Diabetes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/08_reporting/metrics_diabetes.png")
    plt.close()

    print("📊 Gráficos generados en data/08_reporting/")
