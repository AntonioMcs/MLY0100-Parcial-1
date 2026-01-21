
def main():
    mensaje = []
    mensaje.append("Fase 1: Comprensión del negocio - E-commerce brasileño y Olist")
    mensaje.append("Objetivos del negocio:")
    mensaje.append("1. Comprender el comportamiento de compra de los clientes")
    mensaje.append("2. Identificar patrones en pedidos y productos")
    mensaje.append("3. Mejorar la experiencia del cliente y optimizar operaciones")
    mensaje.append("4. Predecir valores de pedidos para inventario y logística")
    mensaje.append("5. Clasificar clientes para marketing personalizado")
    mensaje.append("")
    mensaje.append("Preguntas de negocio:")
    mensaje.append("- ¿Cuál es el valor promedio de los pedidos?")
    mensaje.append("- ¿Qué factores influyen en el valor de un pedido?")
    mensaje.append("- ¿Cómo segmentar clientes según su comportamiento?")
    mensaje.append("- ¿Qué productos son más populares?")
    mensaje.append("- ¿Existen patrones temporales en las compras?")
    mensaje.append("")
    mensaje.append("Targets definidos:")
    mensaje.append("- Regresión: 'order_total_value' (valor total del pedido)")
    mensaje.append("- Clasificación: 'order_status_category' o 'customer_segment'")
    mensaje.append("")
    mensaje.append("Justificación: Permite predecir ingresos, optimizar inventario y personalizar marketing.")

    # Guardar log en archivo
    with open("logs/business_understanding.log", "w", encoding="utf-8") as f:
        for linea in mensaje:
            f.write(linea + "\n")

    # Mostrar por consola
    for linea in mensaje:
        print(linea)

if __name__ == "__main__":
    main()
