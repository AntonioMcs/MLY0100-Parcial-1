"""
Script maestro para procesar el dataset traducido de Olist.
Reemplaza el flujo manual del notebook 01 para usar df_translated_to_english.csv
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
import unicodedata

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent))

from preprocessing import (
    missing_summary, detect_outliers_iqr, cap_outliers,
    impute_numeric_median, impute_categorical_mode
)
from features import create_ecommerce_features


def limpiar_acentos(texto):
    """Limpia caracteres especiales."""
    if pd.isna(texto) or not isinstance(texto, str):
        return texto
    nfd = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in nfd if unicodedata.category(c) != 'Mn')


def procesar_dataset_traducido(input_file='data/02_intermediate/df_translated_to_english.csv',
                               output_dir='data/02_intermediate'):
    """
    Carga y procesa el dataset traducido con el mismo flujo que el notebook 01.
    """
    
    print("=" * 80)
    print("PROCESAMIENTO COMPLETO DEL DATASET TRADUCIDO")
    print("=" * 80)
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 1. CARGA DEL DATASET TRADUCIDO
    print("\n📥 PASO 1: Cargando dataset traducido...")
    try:
        df = pd.read_csv(input_file)
        print(f"  ✓ Dimensiones: {df.shape[0]:,} × {df.shape[1]}")
        print(f"  ✓ Primeras columnas: {list(df.columns[:5])}")
    except FileNotFoundError:
        print(f"  ✗ Archivo no encontrado: {input_file}")
        return None
    
    # 2. ANÁLISIS INICIAL
    print("\n📊 PASO 2: Análisis inicial de datos...")
    print(f"  Valores faltantes totales: {df.isnull().sum().sum()}")
    print(f"  Duplicados: {df.duplicated().sum()}")
    
    df_clean = df.copy()
    
    # 3. TRATAMIENTO DE VALORES FALTANTES
    print("\n🔧 PASO 3: Tratamiento de valores faltantes...")
    missing_before = df_clean.isnull().sum().sum()
    
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()
    
    numeric_missing = [col for col in numeric_cols if df_clean[col].isnull().sum() > 0]
    categorical_missing = [col for col in categorical_cols if df_clean[col].isnull().sum() > 0]
    
    if numeric_missing:
        df_clean = impute_numeric_median(df_clean, numeric_missing)
        print(f"  ✓ {len(numeric_missing)} variables numéricas imputadas con mediana")
    
    if categorical_missing:
        df_clean = impute_categorical_mode(df_clean, categorical_missing)
        print(f"  ✓ {len(categorical_missing)} variables categóricas imputadas con moda")
    
    missing_after = df_clean.isnull().sum().sum()
    print(f"  Valores faltantes: {missing_before:,} → {missing_after}")
    
    # Guardar checkpoint
    df_clean.to_csv(output_path / 'df_cleaned.csv', index=False)
    print(f"  💾 Guardado: df_cleaned.csv")
    
    # 4. TRATAMIENTO DE OUTLIERS
    print("\n🔧 PASO 4: Tratamiento de outliers...")
    cols_with_outliers = []
    for col in numeric_cols:
        outliers = detect_outliers_iqr(df_clean, col)
        pct = (len(outliers) / len(df_clean)) * 100
        if pct > 1:
            cols_with_outliers.append(col)
    
    if cols_with_outliers:
        for col in cols_with_outliers:
            df_clean = cap_outliers(df_clean, col, k=1.5)
        print(f"  ✓ {len(cols_with_outliers)} variables con capping IQR")
    else:
        print(f"  ✓ No se encontraron outliers significativos")
    
    df_clean.to_csv(output_path / 'df_cleaned_no_outliers.csv', index=False)
    print(f"  💾 Guardado: df_cleaned_no_outliers.csv")
    
    # 5. LIMPIEZA DE CATEGÓRICAS
    print("\n🔧 PASO 5: Limpieza de variables categóricas...")
    categorical_cols = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()
    
    for col in categorical_cols:
        value_counts = df_clean[col].value_counts()
        rare_threshold = len(df_clean) * 0.01
        rare_categories = value_counts[value_counts < rare_threshold].index.tolist()
        
        if len(rare_categories) > 0 and len(rare_categories) < len(value_counts) * 0.5:
            df_clean[col] = df_clean[col].replace(rare_categories, 'Other')
        
        if df_clean[col].dtype == 'object':
            df_clean[col] = df_clean[col].str.strip().str.title()
    
    print(f"  ✓ Variables categóricas normalizadas")
    
    df_clean.to_csv(output_path / 'df_cleaned_categorical.csv', index=False)
    print(f"  💾 Guardado: df_cleaned_categorical.csv")
    
    # 6. FEATURE ENGINEERING
    print("\n🔧 PASO 6: Creación de variables derivadas...")
    df_features = create_ecommerce_features(df_clean.copy())
    new_cols = [col for col in df_features.columns if col not in df_clean.columns]
    print(f"  ✓ {len(new_cols)} variables derivadas creadas")
    
    df_clean = df_features
    
    df_clean.to_csv(output_path / 'df_with_features.csv', index=False)
    print(f"  💾 Guardado: df_with_features.csv")
    
    # 7. ENCODING DE CATEGÓRICAS
    print("\n🔧 PASO 7: Encoding de variables categóricas...")
    from sklearn.preprocessing import LabelEncoder
    
    categorical_cols = df_clean.select_dtypes(include=['object', 'category']).columns.tolist()
    exclude_cols = [col for col in categorical_cols if 'id' in col.lower() or 'code' in col.lower() or 'date' in col.lower() or 'timestamp' in col.lower()]
    categorical_cols = [col for col in categorical_cols if col not in exclude_cols]
    
    df_encoded = df_clean.copy()
    one_hot_count = 0
    label_count = 0
    
    for col in categorical_cols:
        n_unique = df_clean[col].nunique()
        if n_unique <= 50:
            df_encoded = pd.get_dummies(df_encoded, columns=[col], drop_first=True, prefix_sep='_')
            one_hot_count += 1
        else:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
            label_count += 1
    
    print(f"  ✓ One-Hot Encoding: {one_hot_count} variables")
    print(f"  ✓ Label Encoding: {label_count} variables")
    print(f"  Columnas después encoding: {df_clean.shape[1]} → {df_encoded.shape[1]}")
    
    df_encoded.to_csv(output_path / 'df_encoded.csv', index=False)
    print(f"  💾 Guardado: df_encoded.csv")
    
    # 8. NORMALIZACIÓN/ESTANDARIZACIÓN
    print("\n🔧 PASO 8: Normalización/Estandarización...")
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from scipy import stats
    import joblib
    
    numeric_cols = df_encoded.select_dtypes(include=[np.number]).columns.tolist()
    
    # Excluir binarias de one-hot
    binary_cols = [col for col in numeric_cols if df_encoded[col].nunique() == 2 and set(df_encoded[col].unique()).issubset({0, 1})]
    numeric_cols = [col for col in numeric_cols if col not in binary_cols]
    
    # Excluir IDs
    exclude_cols = [col for col in numeric_cols if 'id' in col.lower()]
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]
    
    cols_standard = []
    cols_minmax = []
    
    for col in numeric_cols:
        skewness = stats.skew(df_encoded[col].dropna())
        if abs(skewness) < 1:
            cols_standard.append(col)
        else:
            cols_minmax.append(col)
    
    scaler_standard = None
    scaler_minmax = None
    
    if cols_standard:
        scaler_standard = StandardScaler()
        df_encoded[cols_standard] = scaler_standard.fit_transform(df_encoded[cols_standard])
        print(f"  ✓ StandardScaler: {len(cols_standard)} variables")
    
    if cols_minmax:
        scaler_minmax = MinMaxScaler()
        df_encoded[cols_minmax] = scaler_minmax.fit_transform(df_encoded[cols_minmax])
        print(f"  ✓ MinMaxScaler: {len(cols_minmax)} variables")
    
    # Guardar scalers
    models_path = Path('data/06_models')
    models_path.mkdir(parents=True, exist_ok=True)
    
    if scaler_standard:
        joblib.dump(scaler_standard, models_path / 'scaler_standard.pkl')
    if scaler_minmax:
        joblib.dump(scaler_minmax, models_path / 'scaler_minmax.pkl')
    print(f"  💾 Scalers guardados en data/06_models/")
    
    # 9. GUARDAR DATASET FINAL
    print("\n💾 PASO 9: Guardando dataset final procesado...")
    processed_path = Path('data/03_processed')
    processed_path.mkdir(parents=True, exist_ok=True)
    
    df_encoded.to_csv(processed_path / 'df_processed_final.csv', index=False)
    print(f"  ✓ Dataset final: {df_encoded.shape[0]:,} × {df_encoded.shape[1]}")
    
    # 10. RESUMEN FINAL
    print("\n" + "=" * 80)
    print("✅ PROCESAMIENTO COMPLETADO EXITOSAMENTE")
    print("=" * 80)
    
    print(f"\n📊 Resumen Final:")
    print(f"  Filas: {df_encoded.shape[0]:,}")
    print(f"  Columnas: {df_encoded.shape[1]}")
    print(f"  Valores faltantes: {df_encoded.isnull().sum().sum()}")
    print(f"  Duplicados: {df_encoded.duplicated().sum()}")
    
    print(f"\n📁 Archivos Generados:")
    for file in sorted(output_path.glob('df_*.csv')):
        size_mb = file.stat().st_size / (1024**2)
        print(f"  ✓ {file.name} ({size_mb:.2f} MB)")
    
    print(f"\n🎯 El dataset está listo para usarse en el notebook 02 (Modelado)")
    
    return df_encoded


if __name__ == "__main__":
    df_final = procesar_dataset_traducido(
        input_file='data/02_intermediate/df_translated_to_english.csv',
        output_dir='data/02_intermediate'
    )
