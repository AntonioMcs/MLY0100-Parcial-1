# src/features.py
# Funciones para crear nuevas variables (feature engineering)

import pandas as pd

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
