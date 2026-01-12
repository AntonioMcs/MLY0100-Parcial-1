# src/features.py
# Funciones para crear nuevas variables (feature engineering)

import pandas as pd
import numpy as np
from datetime import datetime

def spend_category(df, col='total_spent', bins=3, labels=['Low','Medium','High']):
    """Crea categorías de gasto a partir de total_spent"""
    if col in df.columns:
        df['spend_category'] = pd.qcut(df[col].rank(method="first"), q=bins, labels=labels)
    return df

def age_group(df, col='age'):
    """Agrupa edades en rangos"""
    bins = [0,18,30,45,60,100]
    labels = ['<18','18-30','31-45','46-60','60+']
    if col in df.columns:
        df['age_group'] = pd.cut(df[col], bins=bins, labels=labels)
    return df

def create_ecommerce_features(df):
    """
    Crea variables derivadas específicas para e-commerce.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con datos de e-commerce
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame con nuevas variables derivadas
    """
    df = df.copy()
    
    # Variables de tiempo (si existen columnas de fecha)
    date_columns = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
    
    for col in date_columns:
        try:
            # Convertir a datetime si es posible
            df[col] = pd.to_datetime(df[col], errors='coerce')
            
            # Extraer componentes de fecha
            col_base = col.replace('_date', '').replace('_time', '')
            
            if df[col].notna().sum() > 0:  # Solo si hay fechas válidas
                df[f'{col_base}_year'] = df[col].dt.year
                df[f'{col_base}_month'] = df[col].dt.month
                df[f'{col_base}_day'] = df[col].dt.day
                df[f'{col_base}_dayofweek'] = df[col].dt.dayofweek
                df[f'{col_base}_is_weekend'] = df[col].dt.dayofweek.isin([5, 6]).astype(int)
                df[f'{col_base}_quarter'] = df[col].dt.quarter
        except:
            pass
    
    # Variables de valor (si existen columnas de precio/valor)
    price_columns = [col for col in df.columns if 'price' in col.lower() or 'value' in col.lower() or 'total' in col.lower()]
    
    for col in price_columns:
        if df[col].dtype in [np.float64, np.int64]:
            # Valor promedio por transacción (si hay columna de cantidad)
            qty_cols = [c for c in df.columns if 'qty' in c.lower() or 'quantity' in c.lower()]
            if qty_cols:
                qty_col = qty_cols[0]
                if qty_col in df.columns and (df[qty_col] > 0).any():
                    df[f'{col}_per_unit'] = df[col] / (df[qty_col] + 1e-6)  # Evitar división por cero
    
    # Variables categóricas de segmentación
    # Crear segmentos de valor si existe una columna de valor total
    value_cols = [col for col in df.columns if 'total' in col.lower() and 'value' in col.lower()]
    if value_cols:
        value_col = value_cols[0]
        if value_col in df.columns:
            # Segmentar en terciles
            df[f'{value_col}_segment'] = pd.qcut(
                df[value_col].rank(method='first'), 
                q=3, 
                labels=['Low', 'Medium', 'High'],
                duplicates='drop'
            )
    
    # Variables de frecuencia (si hay IDs de cliente)
    customer_id_cols = [col for col in df.columns if 'customer' in col.lower() and 'id' in col.lower()]
    if customer_id_cols:
        customer_id_col = customer_id_cols[0]
        if customer_id_col in df.columns:
            # Contar frecuencia de pedidos por cliente
            customer_counts = df[customer_id_col].value_counts()
            df['customer_order_frequency'] = df[customer_id_col].map(customer_counts)
    
    return df
