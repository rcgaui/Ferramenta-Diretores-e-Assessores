import pandas as pd

df_data = pd.read_excel('Bases_de_Dados.xlsx', sheet_name='Relatório de Ofertas Públicas')

nome_cliente = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=1)
nome_cliente.rename(columns={
    'Código Cliente': 'Conta XP'
}, inplace=True)
df_data = pd.merge(df_data, nome_cliente[['Conta XP', 'NomeCliente']], on = 'Conta XP')

cod_assessor = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=0)
cod_assessor.rename(columns={
    'Cliente': 'Conta XP'
}, inplace = True)
df_data = pd.merge(df_data, cod_assessor[['Conta XP', 'Assessor']], on = 'Conta XP')

data_assessor = pd.read_excel('Bases_de_Dados.xlsx', sheet_name=2)
data_assessor.rename(columns={
    'Código assessor': 'Assessor'
}, inplace=True)
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Nome assessor']], on = 'Assessor')
df_data = pd.merge(df_data, data_assessor[['Assessor', 'Time']], on = 'Assessor')

df_data['Comissão fixa'] = df_data['Valor Solicitado'] * (1 / 100)

df_data.drop_duplicates(inplace=True)

df_data.rename(columns={
    'Assessor': 'Cod Assessor',
    'NomeCliente': 'Nome Cliente',
    'Nome assessor': 'Nome Assessor',
}, inplace=True)