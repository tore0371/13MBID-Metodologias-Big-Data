import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Se realiza la lectura de los datos
df = pd.read_csv("/Users/salvarodriguezabad/Desktop/13MBID-Metodologias-Big-Data/data/final/datos_finales.csv", sep=";")


# Título del dashboard
st.write("# 13MBID - Visualización de datos")
st.write("## Panel de visualización generado sobre los datos de créditos y tarjetas emitidas a clientes de la entidad")
st.write("#### Persona/s: Salvador Rodríguez Abad")
st.write("----")

# Gráficos
st.write("### Caracterización de los créditos otorgados")

# Se tienen que agregar las definiciones de gráficos desde la libreta
creditos_x_objetivo = px.histogram(df, x='objetivo_credito', 
                                   title='Conteo de créditos por objetivo')
creditos_x_objetivo.update_layout(xaxis_title='Objetivo del crédito', yaxis_title='Cantidad')

# Se realiza la "impresión" del gráfico en el dashboard
st.plotly_chart(creditos_x_objetivo)


# Histograma de los importes de créditos otorgados
histograma_importes = px.histogram(df, x='importe_solicitado', nbins=10, title='Importes solicitados en créditos')
histograma_importes.update_layout(xaxis_title='Importe solicitado', yaxis_title='Cantidad')

st.plotly_chart(histograma_importes)

# Filtros

option = st.selectbox(
    'Qué tipo de crédito desea filtrar?',
     df['objetivo_credito'].unique())

df_filtrado = df[df['objetivo_credito'] == option]

st.write(f"Tipo de crédito seleccionado: {option}")

if st.checkbox('Mostrar créditos finalizados?', value=True):

    # Conteo de ocurrencias por estado
    estado_credito_counts = df_filtrado['estado_credito'].value_counts()

    # Gráfico de torta de estos valores
    fig = go.Figure(data=[go.Pie(labels=estado_credito_counts.index, values=estado_credito_counts)])
    fig.update_layout(title_text='Distribución de créditos por estado registrado')
else:
    df_filtrado = df_filtrado[df_filtrado['estado_credito'] == 1]
    # Conteo de ocurrencias por caso
    falta_pago_counts = df_filtrado['falta_pago'].value_counts()

    # Create a Pie chart
    fig = go.Figure(data=[go.Pie(labels=falta_pago_counts.index, values=falta_pago_counts)])
    fig.update_layout(title_text='Distribución de créditos en función de registro de mora')

st.write(f"Cantidad de créditos con estas condiciones: {df_filtrado.shape[0]}")
st.plotly_chart(fig)