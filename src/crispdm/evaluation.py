
import os

def main():
    mensaje = []
    mensaje.append("Fase 5: Evaluación - Comparación de resultados y validación de objetivos")
    os.makedirs("logs", exist_ok=True)
    # Leer logs de modelado
    try:
        with open("logs/modeling_classification.log", "r", encoding="utf-8") as f:
            clasif = f.read()
    except:
        clasif = "No hay resultados de clasificación."
    try:
        with open("logs/modeling_regression.log", "r", encoding="utf-8") as f:
            regres = f.read()
    except:
        regres = "No hay resultados de regresión."
    mensaje.append("--- Resultados Clasificación ---")
    mensaje.append(clasif)
    mensaje.append("--- Resultados Regresión ---")
    mensaje.append(regres)
    mensaje.append("Validación: ¿Se cumplen los objetivos de negocio?")
    mensaje.append("Revisar métricas y ajustar modelos si es necesario.")
    with open("logs/evaluation.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(str(linea) + "\n")
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
