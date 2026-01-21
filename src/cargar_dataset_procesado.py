#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utility para cargar el dataset procesado listo para modelado

Uso en Notebook:
    from cargar_dataset_procesado import cargar_dataset_procesado
    
    df = cargar_dataset_procesado()
    X = df.drop(columns=['review_score'])
    y = df['review_score']

Características:
    - Carga desde data/03_processed/df_processed_final.csv
    - Valida integridad (filas, columnas, valores faltantes)
    - Retorna DataFrame listo para modelado
    - Información sobre tipos de datos
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

DATASET_PATH = Path('data') / '03_processed' / 'df_processed_final.csv'
EXPECTED_ROWS = 119_143
EXPECTED_COLS = 134


def cargar_dataset_procesado(path=None, verbose=True):
    """
    Carga el dataset procesado y listo para modelado.
    
    Parámetros:
    -----------
    path : str, optional
        Ruta al archivo CSV. Si no se proporciona, usa ruta por defecto.
    verbose : bool, default True
        Si True, imprime información sobre el dataset.
    
    Retorna:
    --------
    pd.DataFrame
        Dataset con 119,143 filas y 134 columnas, listo para modelado.
    
    Raises:
    -------
    FileNotFoundError
        Si el archivo no existe.
    ValueError
        Si el dataset no tiene las dimensiones esperadas.
    
    Ejemplos:
    ---------
    >>> df = cargar_dataset_procesado()
    >>> print(df.shape)
    (119143, 134)
    
    >>> df = cargar_dataset_procesado(verbose=False)
    >>> X = df.drop(columns=['review_score'])
    >>> y = df['review_score']
    """
    
    if path is None:
        path = DATASET_PATH
    else:
        path = Path(path)
    
    # Validar que el archivo existe
    if not path.exists():
        raise FileNotFoundError(
            f"❌ Archivo no encontrado: {path}\n"
            f"   Solución: Ejecuta 'python src/procesar_dataset_maestro.py' primero"
        )
    
    if verbose:
        print(f"\n{'='*80}")
        print(f"📥 CARGANDO DATASET PROCESADO")
        print(f"{'='*80}")
        print(f"Ruta: {path}")
    
    try:
        # Cargar dataset
        df = pd.read_csv(path)
        
        # Validar dimensiones
        if df.shape[0] != EXPECTED_ROWS:
            raise ValueError(
                f"⚠️ Número de filas inesperado: {df.shape[0]} (esperado: {EXPECTED_ROWS})"
            )
        
        if df.shape[1] != EXPECTED_COLS:
            raise ValueError(
                f"⚠️ Número de columnas inesperado: {df.shape[1]} (esperado: {EXPECTED_COLS})"
            )
        
        if verbose:
            print(f"\n✅ Dataset cargado exitosamente")
            print(f"\n📊 INFORMACIÓN:")
            print(f"  Filas: {df.shape[0]:,}")
            print(f"  Columnas: {df.shape[1]}")
            print(f"  Memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
            
            # Información de completitud
            missing = df.isnull().sum().sum()
            print(f"\n🔍 COMPLETITUD:")
            print(f"  Valores faltantes: {missing}")
            print(f"  Completitud: {(1 - missing / (df.shape[0] * df.shape[1])) * 100:.2f}%")
            
            # Información de tipos de datos
            print(f"\n📋 TIPOS DE DATOS:")
            dtype_counts = df.dtypes.value_counts()
            for dtype, count in dtype_counts.items():
                print(f"  {str(dtype):15} : {count:3} columnas")
            
            # Información de columnas
            print(f"\n📝 PRIMERAS 10 COLUMNAS:")
            for i, col in enumerate(df.columns[:10], 1):
                dtype = str(df[col].dtype)
                print(f"  {i:2}. {col:35} ({dtype})")
            
            print(f"\n{'='*80}\n")
        
        return df
    
    except Exception as e:
        print(f"❌ Error al cargar dataset: {e}")
        raise


def obtener_estadisticas_dataset(df):
    """
    Retorna estadísticas útiles del dataset.
    
    Parámetros:
    -----------
    df : pd.DataFrame
        Dataset procesado
    
    Retorna:
    --------
    dict
        Diccionario con estadísticas
    """
    
    stats = {
        'filas': df.shape[0],
        'columnas': df.shape[1],
        'valores_faltantes': df.isnull().sum().sum(),
        'duplicados': df.duplicated().sum(),
        'memoria_mb': df.memory_usage(deep=True).sum() / 1024**2,
        'tipos_datos': df.dtypes.value_counts().to_dict(),
        'columnas_numericas': len(df.select_dtypes(include=[np.number]).columns),
        'columnas_categoricas': len(df.select_dtypes(include=['object']).columns),
        'columnas_booleanas': len(df.select_dtypes(include=['bool']).columns),
    }
    
    return stats


def mostrar_estadisticas(df):
    """
    Imprime estadísticas útiles del dataset.
    
    Parámetros:
    -----------
    df : pd.DataFrame
        Dataset procesado
    """
    
    stats = obtener_estadisticas_dataset(df)
    
    print("\n" + "="*80)
    print("📊 ESTADÍSTICAS DEL DATASET")
    print("="*80)
    
    print(f"\nDimensiones:")
    print(f"  Filas: {stats['filas']:,}")
    print(f"  Columnas: {stats['columnas']}")
    
    print(f"\nMemoria:")
    print(f"  Total: {stats['memoria_mb']:.2f} MB")
    
    print(f"\nIntegridad:")
    print(f"  Valores faltantes: {stats['valores_faltantes']}")
    print(f"  Duplicados: {stats['duplicados']:,}")
    
    print(f"\nTipos de datos:")
    print(f"  Numéricas: {stats['columnas_numericas']}")
    print(f"  Categóricas: {stats['columnas_categoricas']}")
    print(f"  Booleanas: {stats['columnas_booleanas']}")
    
    print(f"\nDetalles de tipos:")
    for dtype, count in stats['tipos_datos'].items():
        print(f"  {str(dtype):15} : {count:3}")
    
    print("\n" + "="*80 + "\n")


if __name__ == '__main__':
    # Ejemplo de uso
    print("\nEjemplo: Cargar dataset")
    df = cargar_dataset_procesado()
    
    print("\nEjemplo: Ver estadísticas")
    mostrar_estadisticas(df)
    
    print("✅ Dataset listo para modelado")
