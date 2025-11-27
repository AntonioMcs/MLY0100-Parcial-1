import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_target_distribution(data: pd.DataFrame):
    """
    Distribución de pacientes con y sin diabetes.
    """
    fig, ax = plt.subplots()
    data["Outcome"].value_counts().sort_index().plot(kind="bar", ax=ax)
    ax.set_xlabel("Outcome (0 = No diabetes, 1 = Diabetes)")
    ax.set_ylabel("Cantidad de pacientes")
    ax.set_title("Distribución de la variable objetivo")
    return fig


def plot_correlation_matrix(data: pd.DataFrame, parameters: dict):
    features = parameters["features"]

    """
    Mapa de calor de correlaciones entre features y el target.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    corr = data[features + ["Outcome"]].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title("Matriz de correlación (diabetes)")
    return fig


def plot_bmi_vs_glucose(data: pd.DataFrame):
    """
    Relación BMI vs Glucose, coloreado por Outcome.
    """
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x="BMI", y="Glucose", hue="Outcome", ax=ax)
    ax.set_title("Relación Glucosa vs BMI según Outcome")
    return fig
