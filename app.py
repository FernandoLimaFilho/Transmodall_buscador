import pandas as pd  # Trabalhar com dados
import streamlit as st

# Carregar dados
Dados = pd.read_csv("tabela_fretes2025.csv")

st.title("Transmodall Aduaneira - Buscador de fretes por cidade")

# Verificar se a cidade já foi armazenada no estado da sessão
if 'cidade' not in st.session_state:
    st.session_state.cidade = ""

# Campo de entrada para o nome da cidade
cidade = st.text_input("Digite o nome da cidade:", value=st.session_state.cidade)

# Salvar a cidade digitada no estado da sessão
if cidade != st.session_state.cidade:
    st.session_state.cidade = cidade

# Verificar se a cidade foi digitada
if cidade:
    # Filtrando e exibindo os resultados
    resultado = Dados[Dados["CIDADE"].str.contains(cidade.upper(), case=False, na=False)]
    
    # Se houver resultados
    if not resultado.empty:
        st.write(f"Resultados encontrados para {cidade}:")
        st.write(resultado[["CIDADE", "VALOR"]])
    else:
        st.write("Nenhum resultado encontrado para essa cidade.")

# Adicionar um botão de interação para pesquisar novamente
if st.button('Pesquisar novamente'):
    # Limpa a cidade no estado da sessão para permitir nova pesquisa
    st.session_state.cidade = ""
    # O campo de texto será limpo e a pesquisa reiniciada sem precisar reiniciar o aplicativo
