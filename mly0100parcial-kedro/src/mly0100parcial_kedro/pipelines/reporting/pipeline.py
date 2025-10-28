from kedro.pipeline import Node, Pipeline
import pandas as pd
import matplotlib.pyplot as plt

from .nodes import (
    compare_passenger_capacity_go,
    create_confusion_matrix,
)


def compare_passenger_capacity_exp(preprocessed_shuttles: pd.DataFrame):
    """
    Genera una figura comparando la distribución de la capacidad de pasajeros
    entre shuttles con tipo 'EXP' y el resto.
    """

    import matplotlib.pyplot as plt
    import pandas as pd

    # --- 🔍 Validación inicial ---
    if not isinstance(preprocessed_shuttles, pd.DataFrame):
        raise TypeError("El parámetro preprocessed_shuttles debe ser un pandas.DataFrame")

    # --- 🔎 Detectar columna de tipo de nave ---
    type_candidates = (
        "shuttle_type",  # ✅ agregado explícitamente
        "service_type",
        "type",
        "category",
        "vehicle_type",
        "line",
        "name",
    )
    type_col = next((c for c in type_candidates if c in preprocessed_shuttles.columns), None)
    if type_col is None:
        raise ValueError(
            "❌ No se encontró una columna para identificar el tipo de shuttle ('EXP'). "
            f"Columnas disponibles: {list(preprocessed_shuttles.columns)}"
        )

    # --- 👥 Detectar columna de capacidad de pasajeros ---
    cap_candidates = ("passenger_capacity", "capacity", "seats", "passenger_capacity_seats")
    cap_col = next((c for c in cap_candidates if c in preprocessed_shuttles.columns), None)
    if cap_col is None:
        raise ValueError(
            "❌ No se encontró columna de capacidad de pasajeros. "
            f"Buscando una de: {cap_candidates}"
        )

    # --- 🧹 Preparar datos ---
    df = preprocessed_shuttles[[type_col, cap_col]].dropna().copy()
    df["is_exp"] = df[type_col].astype(str).str.upper().str.contains("EXP")

    if df.empty:
        raise ValueError("❌ El DataFrame no contiene datos válidos después de limpiar valores NA.")

    # --- 📊 Crear figura (comparativa visual) ---
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    # Boxplot
    df.boxplot(column=cap_col, by="is_exp", ax=axes[0], grid=False)
    axes[0].set_title("Distribución de capacidad de pasajeros")
    axes[0].set_xlabel("")

    # ✅ Ajustar dinámicamente las etiquetas X según los grupos presentes
    unique_labels = df["is_exp"].unique()
    label_map = {True: "EXP", False: "NO EXP"}
    labels = [label_map[val] for val in sorted(unique_labels)]
    axes[0].set_xticklabels(labels)

    axes[0].set_ylabel("Capacidad de pasajeros")

    # Barras de medias
    means = df.groupby("is_exp")[cap_col].mean().rename(index={True: "EXP", False: "NO EXP"})
    axes[1].bar(means.index, means.values, color=["#4C72B0", "#55A868"])
    axes[1].set_title("Media de capacidad de pasajeros")
    axes[1].set_ylabel("Capacidad promedio")

    plt.suptitle("")  # Elimina el título automático del boxplot
    plt.tight_layout()

    return fig


def create_pipeline(**kwargs) -> Pipeline:
    """
    Pipeline de reporting:
    - Compara la capacidad de pasajeros entre naves EXP y no EXP.
    - Compara también para naves GO (otro tipo).
    - Genera una matriz de confusión dummy para validar integridad.
    """
    return Pipeline(
        [
            Node(
                func=compare_passenger_capacity_exp,
                inputs="preprocessed_shuttles",
                outputs="shuttle_passenger_capacity_plot_exp",
                name="compare_passenger_capacity_exp_node",
            ),
            Node(
                func=compare_passenger_capacity_go,
                inputs="preprocessed_shuttles",
                outputs="shuttle_passenger_capacity_plot_go",
                name="compare_passenger_capacity_go_node",
            ),
            Node(
                func=create_confusion_matrix,
                inputs="companies",
                outputs="dummy_confusion_matrix",
                name="create_confusion_matrix_node",
            ),
        ]
    )
