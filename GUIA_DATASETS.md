# Guía de Adaptación a Datasets Brazilian E-commerce

## ✅ Cambios Realizados

### 1. Nuevo Módulo `data_loader.py`
Se creó un módulo especializado para cargar y combinar los datasets de Brazilian E-commerce:

**Ubicación:** `src/data_loader.py`

**Funciones principales:**
- `list_available_datasets()` - Lista todos los archivos CSV disponibles
- `load_brazilian_ecommerce_datasets()` - Carga automáticamente todos los datasets
- `combine_ecommerce_datasets()` - Combina los datasets relacionados
- `get_dataset_info()` - Obtiene información resumida de los datasets

**Características:**
- ✅ Detección automática de archivos CSV
- ✅ Manejo de diferentes encodings (UTF-8, Latin-1, ISO-8859-1)
- ✅ Mapeo inteligente de nombres de archivos
- ✅ Combinación automática basada en claves comunes (order_id, customer_id, etc.)

### 2. Notebook Actualizado
El notebook `01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb` ahora:

- ✅ Importa las funciones de `data_loader`
- ✅ Carga automáticamente todos los archivos CSV disponibles
- ✅ Combina los datasets automáticamente
- ✅ Muestra información detallada de cada dataset cargado

### 3. Archivos Esperados

El sistema detecta automáticamente estos archivos (si están disponibles):

- `olist_orders_dataset.csv` → Cargado como `orders`
- `olist_order_items_dataset.csv` → Cargado como `order_items`
- `olist_customers_dataset.csv` → Cargado como `customers`
- `olist_products_dataset.csv` → Cargado como `products`
- `olist_sellers_dataset.csv` → Cargado como `sellers`
- `olist_order_payments_dataset.csv` → Cargado como `payments`
- `olist_order_reviews_dataset.csv` → Cargado como `reviews`
- `olist_geolocation_dataset.csv` → Cargado como `geolocation`
- `product_category_name_translation.csv` → Cargado como `category_translation`

**Nota:** El sistema funciona con cualquier nombre de archivo CSV, pero los nombres estándar de Olist se mapean automáticamente.

## 📋 Próximos Pasos

### 1. Verificar Archivos
Asegúrate de que todos los archivos CSV estén en `data/01_raw/`:

```bash
# Verificar archivos
ls data/01_raw/*.csv
```

### 2. Ejecutar el Notebook
1. Abre el notebook: `notebooks/01_EDA_Preprocesamiento_Brazilian_Ecommerce.ipynb`
2. Ejecuta las celdas en orden
3. La celda de carga detectará automáticamente todos los archivos disponibles

### 3. Ajustar Targets
Una vez cargados los datos, verifica y ajusta los targets en:

- **Regresión:** Busca columnas relacionadas con valores (price, payment_value, freight_value, etc.)
- **Clasificación:** Busca columnas categóricas (order_status, payment_type, etc.)

Luego actualiza `conf/parameters.yml` con los nombres reales de las columnas.

### 4. Validar Combinación
El dataset combinado (`df`) incluirá:
- Información de pedidos (orders)
- Items de cada pedido (order_items)
- Información de clientes (customers)
- Información de productos (products)
- Información de vendedores (sellers)
- Pagos agregados por pedido (payments)

## 🔍 Identificación de Targets

### Target para Regresión
Busca columnas numéricas relacionadas con valores:
- `price` - Precio del producto
- `payment_value` - Valor del pago
- `freight_value` - Valor del flete
- `total_payment_value` - Valor total del pago (agregado)

**Recomendación:** Crear una columna `order_total_value` que sume price + freight_value

### Target para Clasificación
Busca columnas categóricas:
- `order_status` - Estado del pedido (delivered, shipped, etc.)
- `payment_type` - Tipo de pago (credit_card, boleto, etc.)
- Crear `customer_segment` basado en comportamiento de compra

## ⚠️ Notas Importantes

1. **Encoding:** Los archivos pueden tener diferentes encodings. El sistema intenta automáticamente UTF-8, Latin-1 e ISO-8859-1.

2. **Memoria:** Si los datasets son muy grandes, considera trabajar con muestras o usar `chunksize` en `pd.read_csv()`.

3. **Combinación:** La función de combinación usa `left` joins para preservar todos los pedidos. Si necesitas solo pedidos completos, cambia a `inner` join.

4. **Columnas duplicadas:** Después de combinar, pueden haber columnas con sufijos `_item`, `_customer`, etc. Revisa y renombra según sea necesario.

## 🐛 Solución de Problemas

### Error: "No se encontraron archivos CSV"
- Verifica que los archivos estén en `data/01_raw/`
- Verifica que tengan extensión `.csv`
- Verifica permisos de lectura

### Error: "UnicodeDecodeError"
- El sistema intenta automáticamente diferentes encodings
- Si persiste, abre el archivo manualmente y verifica su encoding

### Error: "KeyError" al combinar
- Verifica que los datasets tengan las columnas de clave esperadas (order_id, customer_id, etc.)
- Revisa los nombres de las columnas en cada dataset

### Dataset combinado muy grande
- Considera trabajar con una muestra: `df_sample = df.sample(n=10000)`
- O filtra por fecha/rango específico antes de combinar

## 📊 Estructura del Dataset Combinado

El dataset combinado (`df`) tendrá esta estructura aproximada:

```
order_id (clave principal)
├── order_status
├── order_purchase_timestamp
├── order_approved_at
├── order_delivered_carrier_date
├── order_delivered_customer_date
├── order_estimated_delivery_date
├── order_item_id
├── product_id
├── seller_id
├── shipping_limit_date
├── price
├── freight_value
├── customer_id / customer_unique_id
├── customer_zip_code_prefix
├── customer_city
├── customer_state
├── product_category_name
├── product_name_lenght
├── product_description_lenght
├── product_photos_qty
├── product_weight_g
├── product_length_cm
├── product_height_cm
├── product_width_cm
├── seller_zip_code_prefix
├── seller_city
├── seller_state
├── total_payment_value (agregado)
├── total_installments (agregado)
└── payment_types (agregado)
```

---

**Última actualización:** 13/01/2026
