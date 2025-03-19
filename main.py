import streamlit as st
from app.config import ENDPOINTS
from app.utils import fetch_data

# Configurações da página
st.set_page_config(page_title="Dashboard de Monitoramento", layout="wide")

# Título do dashboard
st.title("Dashboard de Monitoramento")

# Atualização dos dados com botão de refresh
if st.button("Atualizar Dados"):
    st.experimental_rerun()

# Exibição dos dados
for key, url in ENDPOINTS.items():
    with st.expander(key.capitalize()):  # Expande cada categoria
        data = fetch_data(url)
        if "error" in data:
            st.error(f"Erro ao buscar {key}: {data['error']}")
        else:
            st.json(data)
