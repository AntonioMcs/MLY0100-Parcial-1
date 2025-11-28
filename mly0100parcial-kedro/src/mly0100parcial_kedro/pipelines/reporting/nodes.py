import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_evaluation_results(df: pd.DataFrame) -> pd.DataFrame:
    return df


def generate_plots(df: pd.DataFrame):
    os.makedirs("data/08_reporting", exist_ok=True)

    plt.figure(figsize=(6,4))
    sns.barplot(data=df)
    plt.title("Métricas del Modelo Diabetes")
    plt.tight_layout()
    plt.savefig("data/08_reporting/metrics_diabetes.png")
    plt.close()

    return "data/08_reporting/metrics_diabetes.png"


def generate_report(df: pd.DataFrame, plots_path: str):
    print("\n📄 Reporte generado correctamente (versión simplificada).")
    print(f"Métricas cargadas: \n{df}")
    print(f"Gráfico generado en: {plots_path}")
