import pandas as pd


def add_bmi_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea categorías de IMC para interpretar mejor el riesgo.
    """
    df = df.copy()
    if "BMI" in df.columns:
        df["BMI_Category"] = pd.cut(
            df["BMI"],
            bins=[0, 18.5, 25, 30, float("inf")],
            labels=["Underweight", "Normal", "Overweight", "Obese"],
        )
    return df


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa la edad en rangos clínicamente interpretables.
    """
    df = df.copy()
    if "Age" in df.columns:
        df["Age_Group"] = pd.cut(
            df["Age"],
            bins=[20, 30, 40, 50, 60, float("inf")],
            labels=["20-29", "30-39", "40-49", "50-59", "60+"],
            include_lowest=True,
        )
    return df


def add_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea una métrica sintética de riesgo: Glucose * BMI / Age.
    No es médica real, pero sirve para análisis y visualización.
    """
    df = df.copy()
    required_cols = {"Glucose", "BMI", "Age"}
    if required_cols.issubset(df.columns):
        df["Risk_Score"] = df["Glucose"] * df["BMI"] / df["Age"].clip(lower=1)
    return df


def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """
    One-Hot encoding de todas las columnas categóricas.
    """
    df = df.copy()
    cat_cols = df.select_dtypes(include=["category", "object"]).columns.tolist()
    if cat_cols:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
    return df


def create_model_input_table(df: pd.DataFrame, target_col: str = "Outcome") -> pd.DataFrame:
    """
    Versión diabetes del 'model_input_table' del proyecto FIFA:
    - Se asegura de que no haya filas sin target.
    - Deja todo listo para el split train/test.
    """
    df = df.copy()
    if target_col in df.columns:
        df = df.dropna(subset=[target_col])
    return df
