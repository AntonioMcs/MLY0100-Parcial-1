# src/data_loader.py
# Funciones para cargar y combinar datasets de Brazilian E-commerce

import pandas as pd
import os
from pathlib import Path

def list_available_datasets(data_dir='../data/01_raw'):
    """
    Lista todos los archivos CSV disponibles en el directorio de datos raw.
    
    Parámetros:
    -----------
    data_dir : str
        Ruta al directorio con los datos raw
    
    Retorna:
    --------
    list
        Lista de nombres de archivos CSV encontrados
    """
    data_path = Path(data_dir)
    csv_files = list(data_path.glob('*.csv'))
    return [f.name for f in csv_files]

def load_brazilian_ecommerce_datasets(data_dir='../data/01_raw', verbose=True):
    """
    Carga todos los datasets de Brazilian E-commerce disponibles.
    
    Parámetros:
    -----------
    data_dir : str
        Ruta al directorio con los datos raw
    verbose : bool
        Si True, imprime información sobre los datasets cargados
    
    Retorna:
    --------
    dict
        Diccionario con los DataFrames cargados, usando nombres de archivo como keys
    """
    data_path = Path(data_dir)
    datasets = {}
    
    # Mapeo de nombres de archivos esperados a nombres más cortos
    file_mapping = {
        'olist_orders_dataset.csv': 'orders',
        'olist_order_items_dataset.csv': 'order_items',
        'olist_customers_dataset.csv': 'customers',
        'olist_products_dataset.csv': 'products',
        'olist_sellers_dataset.csv': 'sellers',
        'olist_order_payments_dataset.csv': 'payments',
        'olist_order_reviews_dataset.csv': 'reviews',
        'olist_geolocation_dataset.csv': 'geolocation',
        'product_category_name_translation.csv': 'category_translation'
    }
    
    csv_files = list(data_path.glob('*.csv'))
    
    if verbose:
        print(f"📂 Buscando archivos CSV en: {data_path}")
        print(f"📊 Archivos encontrados: {len(csv_files)}\n")
    
    for csv_file in csv_files:
        try:
            # Intentar cargar con diferentes encodings
            try:
                df = pd.read_csv(csv_file, encoding='utf-8')
            except UnicodeDecodeError:
                try:
                    df = pd.read_csv(csv_file, encoding='latin-1')
                except:
                    df = pd.read_csv(csv_file, encoding='iso-8859-1')
            
            # Usar nombre mapeado si existe, sino usar nombre del archivo sin extensión
            file_name = csv_file.name
            key = file_mapping.get(file_name, file_name.replace('.csv', '').replace('olist_', '').replace('_dataset', ''))
            
            datasets[key] = df
            
            if verbose:
                print(f"✓ {file_name}")
                print(f"  → Cargado como '{key}': {df.shape[0]:,} filas × {df.shape[1]} columnas")
                print(f"  → Columnas: {', '.join(df.columns[:5].tolist())}{'...' if len(df.columns) > 5 else ''}\n")
        
        except Exception as e:
            if verbose:
                print(f"✗ Error cargando {csv_file.name}: {e}\n")
    
    return datasets

def combine_ecommerce_datasets(datasets):
    """
    Combina los datasets de e-commerce en un dataset unificado.
    
    Parámetros:
    -----------
    datasets : dict
        Diccionario con los DataFrames cargados
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame combinado con toda la información
    """
    if 'orders' not in datasets:
        raise ValueError("Se requiere el dataset 'orders' para combinar")
    
    df = datasets['orders'].copy()
    
    # Combinar con order_items si está disponible
    if 'order_items' in datasets:
        df = df.merge(
            datasets['order_items'],
            on='order_id',
            how='left',
            suffixes=('', '_item')
        )
    
    # Combinar con customers si está disponible
    if 'customers' in datasets:
        customer_key = 'customer_id' if 'customer_id' in df.columns else 'customer_unique_id'
        if customer_key in df.columns:
            df = df.merge(
                datasets['customers'],
                on=customer_key,
                how='left',
                suffixes=('', '_customer')
            )
    
    # Combinar con products si está disponible
    if 'products' in datasets and 'product_id' in df.columns:
        df = df.merge(
            datasets['products'],
            on='product_id',
            how='left',
            suffixes=('', '_product')
        )
    
    # Combinar con sellers si está disponible
    if 'sellers' in datasets and 'seller_id' in df.columns:
        df = df.merge(
            datasets['sellers'],
            on='seller_id',
            how='left',
            suffixes=('', '_seller')
        )
    
    # Combinar con payments si está disponible
    if 'payments' in datasets:
        # Agregar payments por order_id (puede haber múltiples pagos por pedido)
        payments_agg = datasets['payments'].groupby('order_id').agg({
            'payment_value': 'sum',
            'payment_installments': 'sum',
            'payment_type': lambda x: ', '.join(x.unique())
        }).reset_index()
        payments_agg.columns = ['order_id', 'total_payment_value', 'total_installments', 'payment_types']
        
        df = df.merge(
            payments_agg,
            on='order_id',
            how='left'
        )
    
    return df

def get_dataset_info(datasets):
    """
    Obtiene información resumida de todos los datasets cargados.
    
    Parámetros:
    -----------
    datasets : dict
        Diccionario con los DataFrames cargados
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame con información de cada dataset
    """
    info = []
    for name, df in datasets.items():
        info.append({
            'Dataset': name,
            'Filas': df.shape[0],
            'Columnas': df.shape[1],
            'Valores Faltantes': df.isnull().sum().sum(),
            'Memoria (MB)': df.memory_usage(deep=True).sum() / 1024**2
        })
    
    return pd.DataFrame(info)
