import pandas as pd
import plotly.express as px
import streamlit as st # type: ignore

# Lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# Criar um botão
hist_button = st.button('Criar histograma')

# Se o botão for clicado
if hist_button:
    # Escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
