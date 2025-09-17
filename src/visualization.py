# src/visualization.py
# Funciones de visualización para análisis exploratorio

import matplotlib.pyplot as plt
import seaborn as sns

def hist_plot(df, col, savepath=None):
    """Histograma de una columna"""
    plt.figure(figsize=(8,4))
    sns.histplot(df[col].dropna(), kde=True)
    if savepath:
        plt.savefig(savepath, bbox_inches="tight", dpi=150)
    plt.show()

def box_plot(df, col, savepath=None):
    """Boxplot de una columna"""
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col].dropna())
    if savepath:
        plt.savefig(savepath, bbox_inches="tight", dpi=150)
    plt.show()

def corr_heatmap(df, savepath=None):
    """Matriz de correlación de variables numéricas"""
    plt.figure(figsize=(10,6))
    sns.heatmap(df.select_dtypes("number").corr(), annot=True, fmt=".2f", cmap="coolwarm")
    if savepath:
        plt.savefig(savepath, bbox_inches="tight", dpi=150)
    plt.show()
