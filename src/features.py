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
    Optimizado para datasets grandes.
    
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
    
    # Variables de tiempo - Solo procesar la columna principal de fecha (order_purchase_timestamp)
    # Esto evita crear demasiadas columnas y acelera el procesamiento
    main_date_col = None
    date_candidates = ['order_purchase_timestamp', 'order_purchase_date', 'purchase_date']
    
    for candidate in date_candidates:
        if candidate in df.columns:
            main_date_col = candidate
            break
    
    # Si no encontramos, buscar cualquier columna con 'purchase' y 'timestamp'
    if main_date_col is None:
        for col in df.columns:
            if 'purchase' in col.lower() and ('timestamp' in col.lower() or 'date' in col.lower()):
                main_date_col = col
                break
    
    if main_date_col:
        try:
            # Convertir a datetime solo una vez
            df[main_date_col] = pd.to_datetime(df[main_date_col], errors='coerce')
            
            if df[main_date_col].notna().sum() > 0:
                # Extraer solo las características más útiles
                df['order_purchase_year'] = df[main_date_col].dt.year
                df['order_purchase_month'] = df[main_date_col].dt.month
                df['order_purchase_dayofweek'] = df[main_date_col].dt.dayofweek
                df['order_purchase_is_weekend'] = df[main_date_col].dt.dayofweek.isin([5, 6]).astype(int)
                df['order_purchase_quarter'] = df[main_date_col].dt.quarter
        except Exception as e:
            print(f"Advertencia: No se pudieron procesar fechas: {e}")
    
    # Crear variable order_total_value (suma de price + freight_value)
    if 'price' in df.columns and 'freight_value' in df.columns:
        df['order_total_value'] = df['price'] + df['freight_value']
    
    # Variables categóricas de segmentación
    # Crear segmentos de valor si existe una columna de valor total
    value_cols = [col for col in df.columns if 'total' in col.lower() and 'value' in col.lower()]
    if value_cols:
        value_col = value_cols[0]
        if value_col in df.columns and df[value_col].notna().sum() > 0:
            try:
                # Segmentar en terciles (solo si hay suficientes valores únicos)
                if df[value_col].nunique() >= 3:
                    df[f'{value_col}_segment'] = pd.qcut(
                        df[value_col].rank(method='first'), 
                        q=3, 
                        labels=['Low', 'Medium', 'High'],
                        duplicates='drop'
                    )
            except Exception:
                # Si falla, crear segmentos manuales
                q33 = df[value_col].quantile(0.33)
                q66 = df[value_col].quantile(0.66)
                df[f'{value_col}_segment'] = pd.cut(
                    df[value_col],
                    bins=[-np.inf, q33, q66, np.inf],
                    labels=['Low', 'Medium', 'High']
                )
    
    # Variables de frecuencia - Optimizado para datasets grandes
    customer_id_cols = [col for col in df.columns if 'customer' in col.lower() and 'id' in col.lower() and 'unique' not in col.lower()]
    if customer_id_cols:
        customer_id_col = customer_id_cols[0]
        if customer_id_col in df.columns:
            # Usar transform para calcular frecuencia de forma más eficiente
            customer_counts = df.groupby(customer_id_col).size()
            df['customer_order_frequency'] = df[customer_id_col].map(customer_counts)
            df['customer_order_frequency'] = df['customer_order_frequency'].fillna(0).astype(int)
    
    # Crear variable de tiempo de entrega (si hay fechas de entrega)
    if 'order_delivered_customer_date' in df.columns and main_date_col:
        try:
            df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'], errors='coerce')
            if df['order_delivered_customer_date'].notna().sum() > 0 and df[main_date_col].notna().sum() > 0:
                df['days_to_delivery'] = (df['order_delivered_customer_date'] - df[main_date_col]).dt.days
                # Reemplazar valores negativos o muy grandes con NaN
                df['days_to_delivery'] = df['days_to_delivery'].clip(lower=0, upper=365)
        except Exception:
            pass
    
    return df
