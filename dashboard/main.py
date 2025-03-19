import streamlit as st
from app.endpoints import get_all_data

# Configurações da página
st.set_page_config(page_title="Dashboard de Monitoramento", layout="wide")

# Título do dashboard
st.title("Dashboard de Monitoramento")

# Atualização dos dados com botão de refresh
if st.button("Atualizar Dados"):
    st.experimental_rerun()

# Exibição dos dados
data = get_all_data()
for key, value in data.items():
    with st.expander(key.capitalize()):
        if "error" in value:
            st.error(f"Erro ao buscar {key}: {value['error']}")
        else:
            st.json(value)
