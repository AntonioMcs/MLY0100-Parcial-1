import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    # Elimina nulos
    data = data.dropna()
    # Ejemplo: eliminar duplicados
    data = data.drop_duplicates()
    return data

def encode_features(data: pd.DataFrame) -> pd.DataFrame:
    if "total_spent" in data.columns:
        data["spend_category"] = pd.cut(
            data["total_spent"],
            bins=[-1, 500, 2000, float("inf")],
            labels=["Low", "Medium", "High"]
        )
    else:
        # Solo para depuración
        print("⚠️ La columna 'total_spent' no existe en el dataset. encode_features no aplicó categorías.")
    return data

