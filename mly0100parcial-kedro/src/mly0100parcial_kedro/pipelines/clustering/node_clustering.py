import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Escala las variables numéricas para clustering."""
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return pd.DataFrame(df_scaled, columns=df.columns)


def run_kmeans(df_scaled: pd.DataFrame, n_clusters: int) -> pd.DataFrame:
    """Aplica K-Means y retorna los clusters asignados."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(df_scaled)
    df_result = df_scaled.copy()
    df_result["cluster"] = clusters
    return df_result
