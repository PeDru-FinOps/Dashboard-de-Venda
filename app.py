import streamlit as st
import plotly.express as px
from dataset import df
from auth import autenticar_usuario
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores, grafico_vendas_vendedores

st.set_page_config(layout='wide')

st.title("Dashboard de Vendas :shopping_trolley:")

# Criar sessão para autenticação
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# Se o usuário não estiver autenticado, exibir login e impedir acesso
if not st.session_state["autenticado"]:
    st.subheader("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if autenticar_usuario(username, password):
            st.session_state["autenticado"] = True
            st.session_state["usuario"] = username
            st.success("Login bem-sucedido!")
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
    st.stop()  # Interrompe a execução do código até que o usuário faça login

st.sidebar.success(f"Bem-vindo, {st.session_state['usuario']}!")

st.sidebar.title('Filtro de Vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)

if filtro_vendedor:
    df = df[df['Vendedor'].isin(filtro_vendedor)]

# Criar abas

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_estado, use_container_width = True)
        st.plotly_chart(grafico_rec_estado, use_container_width = True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)
with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores)
    with coluna2:
        st.plotly_chart(grafico_vendas_vendedores)