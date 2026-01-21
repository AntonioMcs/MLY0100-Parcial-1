"""
Script para unir tablas del dataset de Olist de forma óptima y limpiar caracteres especiales.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import unicodedata
import re


def limpiar_caracteres_especiales(texto):
    """
    Convierte caracteres acentuados y especiales del portugués al inglés.
    
    Ejemplos:
    - São Paulo → Sao Paulo
    - José → Jose
    - Guanabara → Guanabara
    """
    if pd.isna(texto) or not isinstance(texto, str):
        return texto
    
    # Normalizar a NFD (separar caracteres base de diacríticos)
    nfd = unicodedata.normalize('NFD', texto)
    # Eliminar diacríticos
    sin_acentos = ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')
    
    return sin_acentos


def limpiar_dataframe(df):
    """
    Limpia todos los campos de texto en un DataFrame.
    """
    df_limpio = df.copy()
    
    for col in df_limpio.columns:
        if df_limpio[col].dtype == 'object':  # Solo columnas de texto
            df_limpio[col] = df_limpio[col].apply(limpiar_caracteres_especiales)
    
    return df_limpio


def union_optima_olist(data_path='data/01_raw', output_path='data/02_intermediate'):
    """
    Realiza la unión óptima de todas las tablas del dataset Olist.
    
    Flujo de uniones:
    1. orders ← customers
    2. orders ← items
    3. items ← products
    4. items ← sellers
    5. orders ← payments
    6. orders ← reviews
    7. Agregar traducción de categorías
    8. Agregar geolocalización
    """
    
    print("=" * 80)
    print("UNIÓN ÓPTIMA DE TABLAS - OLIST DATASET")
    print("=" * 80)
    
    base_path = Path(data_path)
    output = Path(output_path)
    output.mkdir(exist_ok=True)
    
    # 1. Cargar todas las tablas
    print("\n📥 Cargando tablas...")
    orders = pd.read_csv(base_path / 'olist_orders_dataset.csv')
    customers = pd.read_csv(base_path / 'olist_customers_dataset.csv')
    items = pd.read_csv(base_path / 'olist_order_items_dataset.csv')
    products = pd.read_csv(base_path / 'olist_products_dataset.csv')
    sellers = pd.read_csv(base_path / 'olist_sellers_dataset.csv')
    payments = pd.read_csv(base_path / 'olist_order_payments_dataset.csv')
    reviews = pd.read_csv(base_path / 'olist_order_reviews_dataset.csv')
    geolocation = pd.read_csv(base_path / 'olist_geolocation_dataset.csv')
    translation = pd.read_csv(base_path / 'product_category_name_translation.csv')
    
    print(f"  ✓ Orders: {orders.shape[0]:,} registros")
    print(f"  ✓ Customers: {customers.shape[0]:,} registros")
    print(f"  ✓ Items: {items.shape[0]:,} registros")
    print(f"  ✓ Products: {products.shape[0]:,} registros")
    print(f"  ✓ Sellers: {sellers.shape[0]:,} registros")
    print(f"  ✓ Payments: {payments.shape[0]:,} registros")
    print(f"  ✓ Reviews: {reviews.shape[0]:,} registros")
    
    # 2. PASO 1: Unir orders con customers (1-to-1)
    print("\n🔗 PASO 1: Orders + Customers...")
    df = orders.merge(customers, on='customer_id', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 3. PASO 2: Unir con items (1-to-many, orders puede tener múltiples items)
    print("\n🔗 PASO 2: Resultado + Items...")
    df = df.merge(items, on='order_id', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 4. PASO 3: Unir con products (por product_id)
    print("\n🔗 PASO 3: Resultado + Products...")
    df = df.merge(products, on='product_id', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 5. PASO 4: Unir con sellers (por seller_id)
    print("\n🔗 PASO 4: Resultado + Sellers...")
    df = df.merge(sellers, on='seller_id', how='left', suffixes=('_customer', '_seller'))
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 6. PASO 5: Unir con payments (1-to-many, un order puede tener múltiples pagos)
    print("\n🔗 PASO 5: Resultado + Payments...")
    df = df.merge(payments, on='order_id', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 7. PASO 6: Unir con reviews (1-to-1 con order)
    print("\n🔗 PASO 6: Resultado + Reviews...")
    df = df.merge(reviews, on='order_id', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 8. PASO 7: Unir con traducción de categorías
    print("\n🔗 PASO 7: Resultado + Traducción de categorías...")
    df = df.merge(translation, on='product_category_name', how='left')
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    # 9. PASO 8: Agregar geolocalización (por zip code del cliente)
    print("\n🔗 PASO 8: Resultado + Geolocalización (cliente)...")
    # Limitar geolocation a una fila por zip para evitar explosion
    geo_unique = geolocation.drop_duplicates(subset='geolocation_zip_code_prefix', keep='first')
    df = df.merge(
        geo_unique.rename(columns={
            'geolocation_zip_code_prefix': 'customer_zip_code_prefix',
            'geolocation_lat': 'customer_geolocation_lat',
            'geolocation_lng': 'customer_geolocation_lng',
            'geolocation_city': 'customer_geolocation_city',
            'geolocation_state': 'customer_geolocation_state'
        }),
        on='customer_zip_code_prefix',
        how='left'
    )
    print(f"  ✓ Resultado: {df.shape[0]:,} × {df.shape[1]}")
    
    print("\n" + "=" * 80)
    print("LIMPIEZA DE CARACTERES ESPECIALES")
    print("=" * 80)
    
    # Identificar columnas con caracteres especiales
    print("\n🔍 Buscando caracteres especiales...")
    columnas_texto = df.select_dtypes(include='object').columns
    
    columnas_con_especiales = []
    for col in columnas_texto:
        if df[col].dtype == 'object':
            # Verificar si hay caracteres no-ASCII
            for val in df[col].dropna().unique()[:100]:  # Revisar primeros 100 únicos
                try:
                    val.encode('ascii')
                except (AttributeError, UnicodeEncodeError):
                    columnas_con_especiales.append(col)
                    break
    
    print(f"\n📝 Columnas con caracteres especiales encontradas:")
    for col in columnas_con_especiales:
        print(f"  - {col}")
    
    # Aplicar limpieza
    print("\n🧹 Aplicando limpieza...")
    df_limpio = limpiar_dataframe(df)
    
    print(f"  ✓ Limpieza completada")
    
    # Comparación antes/después
    print("\n" + "=" * 80)
    print("EJEMPLOS DE LIMPIEZA")
    print("=" * 80)
    
    for col in columnas_con_especiales[:3]:  # Mostrar primeros 3
        print(f"\n📌 {col}:")
        unique_original = df[col].dropna().unique()[:5]
        unique_limpio = df_limpio[col].dropna().unique()[:5]
        
        for orig, limp in zip(unique_original, unique_limpio):
            if orig != limp:
                print(f"  {orig} → {limp}")
    
    # Guardar resultados
    print("\n" + "=" * 80)
    print("GUARDANDO RESULTADOS")
    print("=" * 80)
    
    output_file = output / 'df_unido_y_limpio.csv'
    df_limpio.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"\n✓ Dataset unido y limpio guardado:")
    print(f"  Ubicación: {output_file}")
    print(f"  Tamaño: {df_limpio.shape[0]:,} filas × {df_limpio.shape[1]} columnas")
    print(f"  Tamaño en disco: {output_file.stat().st_size / (1024**2):.2f} MB")
    
    # Información del resultado
    print("\n" + "=" * 80)
    print("INFORMACIÓN DEL RESULTADO")
    print("=" * 80)
    print(f"\nTipos de datos:")
    print(df_limpio.dtypes.value_counts())
    
    print(f"\nValores faltantes:")
    missing = df_limpio.isnull().sum()
    missing_pct = (missing / len(df_limpio) * 100).round(2)
    for col, count in missing.nlargest(10).items():
        print(f"  {col}: {count:,} ({missing_pct[col]}%)")
    
    print(f"\n✅ UNIÓN Y LIMPIEZA COMPLETADA EXITOSAMENTE")
    
    return df_limpio


if __name__ == "__main__":
    # Ejecutar desde el directorio raíz del proyecto
    df = union_optima_olist(
        data_path='mly0100parcial-kedro/data/01_raw',
        output_path='data/02_intermediate'
    )
