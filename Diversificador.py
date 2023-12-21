import pandas as pd
import numpy as np

data = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=0)
data['Data de Vencimento'] = pd.to_datetime(data['Data de Vencimento'])
datas_vencimentos_proximas = data['Data de Vencimento'] < '2024-01-01'
df_data = data[datas_vencimentos_proximas].sort_values(by = 'Data de Vencimento')
df_data.reset_index(drop=True)

data_assessor = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=2)
data_assessor.rename(columns={
    'Código assessor': 'Assessor'
}, inplace=True)
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Nome assessor']], on = 'Assessor')
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Time']], on = 'Assessor')

nome_cliente = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=1)
nome_cliente.rename(columns={
    'Código Cliente': 'Cliente'
}, inplace=True)
df_data = pd.merge(df_data, nome_cliente[['Cliente', 'NomeCliente']], on = 'Cliente')

perfil_cliente = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=1)
perfil_cliente.rename(columns={
    'Código Cliente': 'Cliente'
}, inplace=True)
df_data = pd.merge(df_data, perfil_cliente[['Cliente', 'Perfil do Investidor']], on = 'Cliente')

def calculoProj(data):
    nrows = data.shape[0]
    PROJECAO_COE = np.zeros(nrows, dtype=np.float64)
    PROJECAO_OFERTAS = np.zeros(nrows, dtype=np.float64)
    PROJECAO_CARTEIRAS = np.zeros(nrows, dtype=np.float64)
    PROJECAO_RENDAFIXA = np.zeros(nrows, dtype=np.float64)
    RISCO = [None] * nrows
    for i in range(nrows):
        PROJECAO_COE[i] = (2.5 / 100) * data['NET'][i]
        PROJECAO_OFERTAS[i] = (1 / 100) * data['NET'][i]
        PROJECAO_RENDAFIXA[i] = (0.15 / 100) * data['NET'][i]
        PROJECAO_CARTEIRAS[i] = (1.2 / 100) * data['NET'][i]        
        if(data['Sub Produto'][i] == 'Produto Estruturado'):
            RISCO[i] = 'Alto'
        elif(data['Sub Produto'][i] == 'Crédito Privado'):
            RISCO[i] = 'Médio'
        else:
            RISCO[i] = 'Baixo'
    data['Projeção COE'] = PROJECAO_COE
    data['Projeção Ofertas'] = PROJECAO_OFERTAS
    data['Projeção Renda Fixa'] = PROJECAO_RENDAFIXA
    data['Projeção Carteiras'] = PROJECAO_CARTEIRAS
    data['RISCO'] = RISCO

    return data

calculoProj(df_data)

df_data.rename(columns={
    'Cliente': 'Cod Cliente',
    'Assessor': 'Cod Assessor',
    'NomeCliente': 'Nome Cliente',
    'Nome assessor': 'Nome Assessor',
}, inplace=True)