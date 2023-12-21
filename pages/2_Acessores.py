import streamlit as st 
import locale
import plotly.express as px

locale.setlocale(locale.LC_MONETARY, 'pt_BR')

df_data = st.session_state["data"]

assessores = sorted(df_data['Nome Assessor'].value_counts().index)
assessor = st.sidebar.selectbox('Assessor', assessores)
senha_correta = '1234'
senha = st.sidebar.text_input('Digite a senha:', type='password')

if senha:

    if senha == senha_correta:

        st.title('Próximos Vencimentos')

        df_assessor = df_data[df_data['Nome Assessor'] == assessor]

        grouped_by_date = df_assessor.groupby('Data de Vencimento')

        available_dates = sorted(df_assessor['Data de Vencimento'].unique())
        selected_date = st.selectbox('Selecione a Data de Vencimento', available_dates)

        info_selected_date = grouped_by_date.get_group(selected_date)

        st.divider()


        for index, row in info_selected_date.iterrows():
            col1, col2, col3 = st.columns(3)
            col1.subheader(f"Cliente: {row['Nome Cliente']}")
            col3.subheader(f"{selected_date.strftime('%Y-%m-%d')}")
            st.markdown(f"**Perfil:** {row['Perfil do Investidor']}")
            st.markdown(f"**Código Cliente:** {row['Cod Cliente']}")
            st.markdown(f"**Produto:** {row['Produto']}")
            st.markdown(f"**Sub Produto:** {row['Sub Produto']}")
            st.markdown(f"**Ativo:** {row['Ativo']}")
            st.markdown(f"**Emissor:** {row['Emissor']}")
            st.markdown(f"**Risco:** {row['RISCO']}")
            st.markdown(f"**NET:** {locale.currency(row['NET'], grouping=True)}")
            if col3.button('Projeções de receita', key=f'button_{row["Cod Cliente"]}_{index}'):
                valores = [
                    locale.currency(row['Projeção COE'], grouping=True),
                    locale.currency(row['Projeção Ofertas'], grouping=True),
                    locale.currency(row['Projeção Carteiras'], grouping=True),
                    locale.currency(row['Projeção Renda Fixa'], grouping=True)
                ]

                color_discrete_map = {'COE': 'red', 'Oferta Pública': 'blue', 'Carteira Automatizada': 'orange', 'Renda Fixa': 'green'}

                fig = px.bar(
                    x=['COE (Risco alto)', 'Oferta Pública (Risco médio)', 'Carteira Automatizada (Risco médio)', 'Renda Fixa (Risco baixo)'],
                    y=[row['Projeção COE'], row['Projeção Ofertas'], row['Projeção Carteiras'], row['Projeção Renda Fixa']],
                    labels={'y': 'Valor', 'x': 'Tipo de Projeção'},
                    title=f'Projeções da comissão esperada com a alocação de {locale.currency(row["NET"], grouping=True)}',
                    height=400,
                    color=['COE', 'Oferta Pública', 'Carteira Automatizada', 'Renda Fixa'],
                    text= valores,
                    color_discrete_map = color_discrete_map
                )
                st.plotly_chart(fig)
            st.divider()

    else:
        st.warning('Senha incorreta. Tente novamente.')