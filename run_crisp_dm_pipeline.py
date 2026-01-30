#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de inicialización para ejecutar el pipeline CRISP-DM localmente.
Ejecuta todas las fases en secuencia: Negocio -> Datos -> Preparación -> Modelado -> Evaluación -> Despliegue
"""

import sys
import os
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def print_header(fase_num, fase_nombre):
    """Imprime un header para cada fase"""
    print("\n" + "="*70)
    print(f"FASE {fase_num}: {fase_nombre.upper()}")
    print("="*70 + "\n")

def main():
    """Ejecuta todas las fases del pipeline CRISP-DM"""
    print("\n" + "🚀 "*35)
    print("INICIANDO PIPELINE CRISP-DM - ECOMMERCE BRASILEÑO")
    print("🚀 "*35)

    # Crear directorio de logs si no existe
    os.makedirs("logs", exist_ok=True)

    try:
        # Fase 1: Comprensión del Negocio
        print_header(1, "Comprensión del Negocio")
        from crispdm.business_understanding import main as bu_main
        bu_main()

        # Fase 2: Comprensión de los Datos
        print_header(2, "Comprensión de los Datos")
        from crispdm.data_understanding import main as du_main
        du_main()

        # Fase 3: Preparación de Datos
        print_header(3, "Preparación de Datos")
        from crispdm.data_preparation import main as dp_main
        dp_main()

        # Fase 4a: Modelado - Clasificación
        print_header("4a", "Modelado - Clasificación")
        from crispdm.modeling_classification import main as mc_main
        mc_main()

        # Fase 4b: Modelado - Regresión
        print_header("4b", "Modelado - Regresión")
        from crispdm.modeling_regression import main as mr_main
        mr_main()

        # Fase 5: Evaluación
        print_header(5, "Evaluación")
        from crispdm.evaluation import main as ev_main
        ev_main()

        # Fase 6: Despliegue
        print_header(6, "Despliegue")
        from crispdm.deployment import main as dp_main
        dp_main()

        # Resumen final
        print("\n" + "="*70)
        print("✅ PIPELINE COMPLETADO EXITOSAMENTE")
        print("="*70)
        print("\n📁 Archivos de log generados en: ./logs/")
        print("📊 Reportes guardados en: ./data/08_reporting/")
        print("\n¡Revisá los logs y reportes para más detalles!\n")

    except Exception as e:
        print("\n" + "="*70)
        print(f"❌ ERROR EN EL PIPELINE: {str(e)}")
        print("="*70)
        print(f"\nDetalles del error:\n{type(e).__name__}: {str(e)}")
        print("\nRevisa los logs en ./logs/ para más información.")
        sys.exit(1)

if __name__ == "__main__":
    main()
