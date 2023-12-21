import pandas as pd

df_data = pd.read_excel('Bases_de_Dados.xlsx', sheet_name='Relatório de Carteiras Auto')

df_data['Compra da carteira'] = pd.to_datetime(df_data['Compra da carteira'], format="%d/%m/%Y")
datas_vencimentos_proximas = df_data['Compra da carteira'] >= '2023-12-01'
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

df_data['Comissão fixa'] = df_data['Valor aportado'] * (1.2 / 100)

df_data.drop_duplicates(inplace=True)

df_data.rename(columns={
    'Cliente': 'Cod Cliente',
    'Assessor': 'Cod Assessor',
    'NomeCliente': 'Nome Cliente',
    'Nome assessor': 'Nome Assessor',
}, inplace=True)