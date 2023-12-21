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

df_data = df_data.drop(['Produto', 'Sub Produto', 'Ativo', 'Emissor', 'Data de Vencimento', 'Quantidade', 'NET'], axis=1)

df_data = df_data.drop_duplicates(subset='Nome assessor')
df_data = df_data.reset_index(drop=True)

df_coe = pd.read_excel('Relatorio_COE_.xlsx')
df_coe = df_coe.groupby('Nome Assessor', as_index = False)['Comissão fixa'].sum()
df_coe = df_coe.drop_duplicates(subset='Nome Assessor')
df_coe.rename(columns = {
    'Nome Assessor': 'Nome assessor'
}, inplace = True)
df_data = pd.merge(df_data, df_coe[['Nome assessor', 'Comissão fixa']], on='Nome assessor', how='left')

df_data.rename(columns = {
    'Comissão fixa': 'Comissao COE'
}, inplace = True)

df_ofertas = pd.read_excel('Relatorio_Ofertas_.xlsx')
df_ofertas = df_ofertas.groupby('Nome Assessor', as_index = False)['Comissão fixa'].sum()
df_ofertas = df_ofertas.drop_duplicates(subset='Nome Assessor')
df_ofertas.rename(columns = {
    'Nome Assessor': 'Nome assessor'
}, inplace = True)
df_data = pd.merge(df_data, df_ofertas[['Nome assessor', 'Comissão fixa']], on='Nome assessor', how='left')

df_data.rename(columns = {
    'Comissão fixa': 'Comissao Ofertas'
}, inplace = True)

df_carteiras = pd.read_excel('Relatorio_Carteira_.xlsx')
df_carteiras = df_carteiras.groupby('Nome Assessor', as_index = False)['Comissão fixa'].sum()
df_carteiras = df_carteiras.drop_duplicates(subset='Nome Assessor')
df_carteiras.rename(columns = {
    'Nome Assessor': 'Nome assessor'
}, inplace = True)
df_data = pd.merge(df_data, df_carteiras[['Nome assessor', 'Comissão fixa']], on='Nome assessor', how='left')

df_data.rename(columns = {
    'Comissão fixa': 'Comissao Carteiras'
}, inplace = True)

df_data['Comissao total'] = df_data[['Comissao COE', 'Comissao Ofertas', 'Comissao Carteiras']].sum(axis=1)
df_data['Comissao total'] = df_data['Comissao total'].replace(0, np.nan)
df_data['Comissao COE'] = df_data['Comissao COE'].replace(0, np.nan)
df_data = df_data.drop('Cliente', axis=1)