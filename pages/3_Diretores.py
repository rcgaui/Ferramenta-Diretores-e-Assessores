import streamlit as st
from datetime import datetime
import plotly.express as px
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR')

df_data = st.session_state["data"]
df_data2 = st.session_state["data2"]
df_data3 = st.session_state["data3"]
df_data4 = st.session_state["data4"]
df_data5 = st.session_state["data5"]

senha_correta = '1234'
senha = st.sidebar.text_input('Digite a senha:', type='password')

if senha:

    if senha == senha_correta:

        times = df_data['Time'].unique().tolist()
        times.append('Todos')
        time = st.sidebar.selectbox('Time', times)

        if time == 'Todos':
            df_assessores = df_data
        else:
            df_assessores = df_data[df_data['Time'] == time]

        assessores = sorted(df_assessores['Nome Assessor'].value_counts().index)
        assessor = st.sidebar.selectbox('Assessor', assessores)



        st.title(f'Relatório de {assessor}')
        st.divider()

        st.subheader('COE')

        if assessor in df_data2['Nome Assessor'].unique():

            qtd_clientes_coe = df_data2[df_data2['Nome Assessor'] == assessor]['Cod Cliente'].nunique()
            qtd_aplicacoes_coe = df_data2[df_data2['Nome Assessor'] == assessor].shape[0]
            total_aplicado_coe = df_data2[df_data2['Nome Assessor'] == assessor]['Valor Aplicado'].sum()
            media_valor_por_aplicacao_coe = total_aplicado_coe/qtd_aplicacoes_coe
            comissao_total_coe = df_data2[df_data2['Nome Assessor'] == assessor]['Comissão fixa'].sum()
            comissao_media_coe = comissao_total_coe/qtd_aplicacoes_coe
            total_aplicado_coe = locale.currency(total_aplicado_coe, grouping=True)
            media_valor_por_aplicacao_coe = locale.currency(media_valor_por_aplicacao_coe, grouping=True)
            comissao_total_coe = locale.currency(comissao_total_coe, grouping=True)
            comissao_media_coe = locale.currency(comissao_media_coe, grouping=True)

            col1, col2 = st.columns(2)
            col1.markdown(f'**Número de clientes:** {qtd_clientes_coe}')
            col2.markdown(f'**Número de aplicações:** {qtd_aplicacoes_coe}')
            col1.markdown(f'**Total aplicado:** {total_aplicado_coe}')
            col2.markdown(f'**Média de valor por aplicação:** {media_valor_por_aplicacao_coe}')
            col1.markdown(f'**Comissão total:** {comissao_total_coe}')
            col2.markdown(f'**Comissão média por aplicação:** {comissao_media_coe}')

        else:
            st.warning(f'{assessor} não possui dados de COE.')

        st.divider()

        st.subheader('Ofertas Públicas')

        if assessor in df_data3['Nome Assessor'].unique():

            qtd_clientes_of = df_data3[df_data3['Nome Assessor'] == assessor]['Conta XP'].nunique()
            qtd_aplicacoes_of = df_data3[df_data3['Nome Assessor'] == assessor].shape[0]
            total_aplicado_of = df_data3[df_data3['Nome Assessor'] == assessor]['Valor Solicitado'].sum()
            media_valor_por_aplicacao_of = total_aplicado_of/qtd_aplicacoes_of
            comissao_total_of = df_data3[df_data3['Nome Assessor'] == assessor]['Comissão fixa'].sum()
            comissao_media_of = comissao_total_of/qtd_aplicacoes_of
            total_aplicado_of = locale.currency(total_aplicado_of, grouping=True)
            media_valor_por_aplicacao_of = locale.currency(media_valor_por_aplicacao_of, grouping=True)
            comissao_total_of = locale.currency(comissao_total_of, grouping=True)
            comissao_media_of = locale.currency(comissao_media_of, grouping=True)

            col1, col2 = st.columns(2)
            col1.markdown(f'**Número de clientes:** {qtd_clientes_of}')
            col2.markdown(f'**Número de aplicações:** {qtd_aplicacoes_of}')
            col1.markdown(f'**Total aplicado:** {total_aplicado_of}')
            col2.markdown(f'**Média de valor por aplicação:** {media_valor_por_aplicacao_of}')
            col1.markdown(f'**Comissão total:** {comissao_total_of}')
            col2.markdown(f'**Comissão média por aplicação:** {comissao_media_of}')

        else:
            st.warning(f'{assessor} não possui dados de Oferta Pública.')

        st.divider()

        st.subheader('Carteira Automatizada')

        if assessor in df_data4['Nome Assessor'].unique():

            qtd_clientes_ca = df_data4[df_data4['Nome Assessor'] == assessor]['Cod Cliente'].nunique()
            qtd_aplicacoes_ca = df_data4[df_data4['Nome Assessor'] == assessor].shape[0]
            total_aplicado_ca = df_data4[df_data4['Nome Assessor'] == assessor]['Valor aportado'].sum()
            media_valor_por_aplicacao_ca = total_aplicado_ca/qtd_aplicacoes_ca
            comissao_total_ca = df_data4[df_data4['Nome Assessor'] == assessor]['Comissão fixa'].sum()
            comissao_media_ca = comissao_total_ca/qtd_aplicacoes_ca
            total_aplicado_ca = locale.currency(total_aplicado_ca, grouping=True)
            media_valor_por_aplicacao_ca = locale.currency(media_valor_por_aplicacao_ca, grouping=True)
            comissao_total_ca = locale.currency(comissao_total_ca, grouping=True)
            comissao_media_ca = locale.currency(comissao_media_ca, grouping=True)

            col1, col2 = st.columns(2)
            col1.markdown(f'**Número de clientes:** {qtd_clientes_ca}')
            col2.markdown(f'**Número de carteiras:** {qtd_aplicacoes_ca}')
            col1.markdown(f'**Total aportado:** {total_aplicado_ca}')
            col2.markdown(f'**Média de valor por aporte:** {media_valor_por_aplicacao_ca}')
            col1.markdown(f'**Comissão total:** {comissao_total_ca}')
            col2.markdown(f'**Comissão média por aporte:** {comissao_media_ca}')

            primeira_compra = df_data4[df_data4['Nome Assessor'] == assessor]['Compra da carteira'].min()
            primeira_compra = primeira_compra.strftime("%d/%m/%Y")
            date_atual = datetime.now()
            date_atual = date_atual.strftime("%d/%m/%Y")
            soma_rentabilidade = df_data4[df_data4['Nome Assessor'] == assessor]['Rentabilidade'].sum()
            media_rentabilidade = soma_rentabilidade/qtd_aplicacoes_ca
            media_rentabilidade = round(media_rentabilidade, 2)
            col1.markdown('\n')
            col1.metric(label= f"**Rentabilidade média ({primeira_compra} até {date_atual})**", value=media_rentabilidade, delta=media_rentabilidade,
            delta_color="normal")

        else:
            st.warning(f'{assessor} não possui dados de Carteira Automatizada.')

        st.divider()

        st.subheader('Comissões')

        if all(col in df_data5.columns for col in ['Comissao COE', 'Comissao Ofertas', 'Comissao Carteiras']):
            
            df_assessor_data5 = df_data5[df_data5['Nome assessor'] == assessor]

            if not df_assessor_data5.empty:

                df_assessor_data5['Comissao Total'] = df_assessor_data5[['Comissao COE', 'Comissao Ofertas', 'Comissao Carteiras']].sum(axis=1)
                comissao_total = df_assessor_data5['Comissao Total'].iloc[0]
                comissao_total = locale.currency(comissao_total, grouping=True)

                values = [
                    df_assessor_data5['Comissao COE'].iloc[0],
                    df_assessor_data5['Comissao Ofertas'].iloc[0],
                    df_assessor_data5['Comissao Carteiras'].iloc[0]
                ]

                fig_data5 = px.pie(names=['Comissão de COE', 'Comissão de Ofertas Públicas', 'Comissão de Carteiras Automatizadas'], values=values, title=f'Valor total recebido por comissões em dezembro: {comissao_total}')
                st.plotly_chart(fig_data5)
            else:
                st.warning(f'{assessor} não possui dados de comissão.')
        else:
            st.warning(f'{assessor} não possui dados de comissão.')

    else:
        st.sidebar.warning('Senha incorreta. Tente novamente.')
        