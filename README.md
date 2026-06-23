# Análisis de vehículos usados

Esta aplicación web fue desarrollada con Streamlit. La app permite explorar un conjunto de datos de anuncios de venta de vehículos usados. Incluye una vista previa de los datos, un histograma del kilometraje de los vehículos y un gráfico de dispersión que muestra la relación entre el kilometraje y el precio.

## Funcionalidades

- Visualización inicial del dataset.
- Histograma de la columna `odometer`.
- Gráfico de dispersión entre `odometer` y `price`.
- Interacción mediante casillas de verificación.

## Tecnologías utilizadas

- Python
- pandas
- plotly express
- streamlit

## Ejecutar localmente

```bash
streamlit run app.py
