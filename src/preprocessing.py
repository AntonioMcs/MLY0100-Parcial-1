# src/preprocessing.py
# Funciones básicas de carga, guardado y limpieza de datos

import pandas as pd
import numpy as np

def load_csv(path):
    """Carga un CSV desde la ruta dada y retorna un DataFrame"""
    return pd.read_csv(path)

def save_csv(df, path):
    """Guarda un DataFrame en CSV sin el índice"""
    df.to_csv(path, index=False)

def missing_summary(df):
    """Devuelve un resumen de valores nulos en el DataFrame"""
    n = df.isnull().sum()
    pct = (n / len(df)) * 100
    return pd.DataFrame({"nulos": n, "pct": pct}).sort_values("pct", ascending=False)

def drop_high_missing(df, thresh=40):
    """Elimina columnas con más de `thresh`% de valores nulos"""
    pct = df.isnull().mean() * 100
    keep = pct[pct <= thresh].index
    return df[keep]

def impute_numeric_median(df, cols):
    """Imputa columnas numéricas con la mediana"""
    for c in cols:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())
    return df

def impute_categorical_mode(df, cols):
    """Imputa columnas categóricas con la moda"""
    for c in cols:
        if c in df.columns:
            mode = df[c].mode()
            df[c] = df[c].fillna(mode[0] if not mode.empty else "Unknown")
    return df

def detect_outliers_iqr(df, col, k=1.5):
    """Devuelve los outliers de una columna usando IQR"""
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - k*IQR, Q3 + k*IQR
    return df[(df[col] < lower) | (df[col] > upper)]

def cap_outliers(df, col, k=1.5):
    """Capea los valores extremos de una columna usando IQR"""
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - k*IQR, Q3 + k*IQR
    if col in df.columns:
        df[col] = df[col].clip(lower, upper)
    return df
