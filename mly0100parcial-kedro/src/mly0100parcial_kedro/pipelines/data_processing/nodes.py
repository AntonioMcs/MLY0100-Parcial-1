import pandas as pd
from sklearn.impute import SimpleImputer


def clean_diabetes_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset de diabetes:
    - Reemplaza ceros imposibles por NaN en columnas biométricas.
    - Elimina duplicados.
    """
    df = df.copy()

    # Columnas donde un 0 es MUY sospechoso (caso clásico del dataset Pima)
    biometrics_zero_invalid = [
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
    ]

    for col in biometrics_zero_invalid:
        if col in df.columns:
            df[col] = df[col].replace(0, pd.NA)

    df = df.drop_duplicates()

    return df


def impute_diabetes_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Imputa valores faltantes en todas las columnas numéricas usando la mediana.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    imputer = SimpleImputer(strategy="median")
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

    return df
