import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análisis de anuncios de vehículos usados")

car_data = pd.read_csv("vehicles_us.csv")

st.write("Esta aplicación permite explorar datos de anuncios de venta de coches usados.")

st.subheader("Vista previa de los datos")
st.dataframe(car_data.head())

build_histogram = st.checkbox("Construir histograma del odómetro")

if build_histogram:
    st.write("Histograma de la columna odometer")

    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje"
    )

    st.plotly_chart(fig_hist, use_container_width=True)

build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_scatter:
    st.write("Relación entre precio y kilometraje")

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Precio vs kilometraje"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)