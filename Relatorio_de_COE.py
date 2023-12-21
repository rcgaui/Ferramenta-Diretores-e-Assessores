import pandas as pd
import numpy as np

df_data = pd.read_excel('Bases_de_Dados.xlsx', sheet_name='Relatório de COE')

df_data['Data'] = pd.to_datetime(df_data['Data'])
datas_vencimentos_proximas = df_data['Data'] >= '2023-12-01'
df_data = df_data[datas_vencimentos_proximas]

nome_cliente = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=1)
nome_cliente.rename(columns={
    'Código Cliente': 'Cliente'
}, inplace=True)
df_data = pd.merge(df_data, nome_cliente[['Cliente', 'NomeCliente']], on = 'Cliente')

cod_assessor = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=0)
cod_assessor.rename(columns={
    'Cliente': 'Cliente'
}, inplace = True)
df_data = pd.merge(df_data, cod_assessor[['Cliente', 'Assessor']], on = 'Cliente')

data_assessor = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=2)
data_assessor.rename(columns={
    'Código assessor': 'Assessor'
}, inplace=True)
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Nome assessor']], on = 'Assessor')
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Time']], on = 'Assessor')

df_data['Comissão fixa'] = np.where(df_data['Status'] == 'Liquidada', df_data['Valor Aplicado'] * (2.5 / 100), np.nan)

df_data.drop_duplicates(inplace=True)

df_data.rename(columns={
    'Cliente': 'Cod Cliente',
    'Assessor': 'Cod Assessor',
    'NomeCliente': 'Nome Cliente',
    'Nome assessor': 'Nome Assessor',
    'Nome do Produto (30)': 'Nome do Produto'
}, inplace=True)

df_data = df_data[['Cod Assessor', 'Nome Assessor', 'Cod Cliente', 'Nome Cliente', 'Nome do Produto', 'Valor Aplicado', 'Data', 'Tipo', 'Status', 'Comissão fixa', 'Time']]