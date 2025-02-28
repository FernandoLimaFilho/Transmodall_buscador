import pandas as pd
import streamlit as st

st.title("Teste Simples")
try:
    df = pd.read_csv("tabela_fretes2025.csv")
    st.write("CSV carregado com sucesso!")
    st.write(df.head())  # Mostra as primeiras linhas do CSV
except Exception as e:
    st.write("Erro ao carregar CSV:", e)
