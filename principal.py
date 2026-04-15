import streamlit as st

st.set_page_config(page_title="Flávia's App", page_icon="💻", layout="wide")

st.image("Panda-Vermelho.png", width=500)

st.markdown("Bem-vindo!")
st.write("Este é um app simples criado para acesso ao meu site.")

col1 = st.columns(1)

with col1:
    st.info("📘 Aula de Informática")

st.write("")

st.link_button("🌐 Acessar Site", "https://sites.google.com/academico.ifpb.edu.br/flaviaregina/in%C3%ADcio")
