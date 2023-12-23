import pandas as pd
import plotly.express as px
import streamlit as st


st.header('Análisis de Datos de Vehículos')
st.subheader('Histograma y Gráfico de Dispersión')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
dispersion_button = st.button('Construir gráfico de dispersión') # crear un botón para el gráfico de dispersión


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dispersion_button:
    st.write('Construcción de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersión")
    st.plotly_chart(fig_scatter, use_container_width=True)