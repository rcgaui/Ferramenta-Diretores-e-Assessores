import streamlit as st 
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_excel('Diversificador_.xlsx')
    df_data['Data de Vencimento'] = pd.to_datetime(df_data['Data de Vencimento']).dt.date
    df_data = df_data.sort_values(by = 'Data de Vencimento').reset_index(drop=True)
    st.session_state["data"] = df_data
    
if "data2" not in st.session_state:
    df_data2 = pd.read_excel('Relatorio_COE_.xlsx')
    st.session_state["data2"] = df_data2

if "data3" not in st.session_state:
    df_data3 = pd.read_excel('Relatorio_Ofertas_.xlsx')
    st.session_state["data3"] = df_data3

if "data4" not in st.session_state:
    df_data4 = pd.read_excel('Relatorio_Carteira_.xlsx')
    df_data4['Compra da carteira'] = pd.to_datetime(df_data4['Compra da carteira'], format='%d/%m/%Y').dt.date
    df_data4 = df_data4.sort_values(by = 'Compra da carteira').reset_index(drop=True)
    st.session_state["data4"] = df_data4

if "data5" not in st.session_state:
    df_data5 = pd.read_excel('Relatorio_Comissoes_.xlsx')
    st.session_state["data5"] = df_data5

st.write("# 2ª Etapa do Processo Seletivo")
st.write("Projeto que visa promover aos assessores uma ferramenta funcional onde eles possam ver os próximos vencimentos e uma projeção da receita esperada com alocação. Além disso, promover uma ferramenta para os diretores, onde eles podem analisar o desempenho de cada assessor.")