import exibir_dados_curitiba as dados
import streamlit as st
import questions
import intro


st.set_page_config(page_title="Consumo consciente", page_icon="♻️", layout="wide")

pagina = st.sidebar.selectbox("Navegação", ["Apresentação", "Dados de Curitiba", "Quiz"])
if pagina == "Apresentação":
    intro.apresentacao()

elif pagina == "Dados de Curitiba":
    dados.exibir_dados()

elif pagina == "Quiz":
    questions.exibir_perguntas()










