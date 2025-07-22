import streamlit as st
import pandas as pd
import plotly.express as px

dados = '[organizar] Análises a serem realizadas _ v1.xlsx'

ICON = "img/grafico.png"
st.logo(ICON)

st.set_page_config(page_title="Impacto da pandemia no RN", page_icon="📊", layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "Dados Gerais"
    
with st.sidebar:
    st.header("Dados")
    if st.button("Gerais", type="tertiary", icon="⭐"):
        st.session_state.page = "Dados Gerais"
    if st.button("Trabalhando", type="tertiary", icon="📋"):
        st.session_state.page = "Trabalhando"
    if st.button("Rendimentos", type="tertiary", icon="💲"):
        st.session_state.page = "Rendimentos"
    if st.button("Jovens", type="tertiary", icon="👥"):
        st.session_state.page = "Jovens"
    if st.button("Desocupados", type="tertiary", icon="📉"):
        st.session_state.page = "Desocupados"
    if st.button("Subutilização", type="tertiary", icon="⚠️"):
        st.session_state.page = "Subutilização"

if st.session_state.page == "Dados Gerais":
    st.title("Impactos da pandemia nos IS do RN")
    st.markdown("Neste dashboard serão apresentados os impactos da pandemia da covid-19 nos indicadores sociais de trabalho e rendimentos do RN com base nos dados da Síntese de Indicadores Sociais do IBGE.")
    st.subheader("Indicadores sociais de trabalho e rendimento")
    st.markdown("Esta seção apresenta os indicadores sociais relacionados ao trabalho e rendimento")

    st.subheader("Dados Gerais")
    col1, col2, col3 = st.columns(3)
    with col1:
        df = pd.read_excel(dados, sheet_name="26 - População em idade de trab", header=1)    
        df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))
        df = df.astype(int)
        col_x = df.columns[0] 
        col_y = df.columns[1] 
        fig1 = px.bar(df, x=col_x, y=col_y, title="População em idade de trabalhar (1 000 pessoas)")

        fig1.update_traces(textposition="outside")
        fig1.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor",
            uniformtext_minsize=8,
            uniformtext_mode='hide'
        )

        st.plotly_chart(fig1)

    with col2:
        df = pd.read_excel(dados, sheet_name="27 - População na força de trab", header=1)
        df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))
        df = df.astype(int)
        col_x = df.columns[0] 
        col_y = df.columns[1] 
        fig2 = px.bar(df, x=col_x, y=col_y, title="População na força de trabalho (1 000 pessoas)")

        fig2.update_traces(textposition="outside")
        fig2.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor",
            uniformtext_minsize=8,
            uniformtext_mode='hide'
        )

        st.plotly_chart(fig2)    
    with col3:
        df = pd.read_excel(dados, sheet_name="31 - População na força de trab", header=1)
        df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))
        df = df.astype(int)
        col_x = df.columns[0] 
        col_y = df.columns[1] 
        fig3 = px.line(df, x=col_x, y=col_y, title="População na força de trabalho potencial (1 000 pessoas)")

        fig3.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor",
            uniformtext_minsize=8,
            uniformtext_mode='hide',
        )
        max_val = df[col_y].max()
        fig3.update_yaxes(range=[0, max_val * 1.1]) 
        st.plotly_chart(fig3)   
    
elif st.session_state.page == "Trabalhando":
    st.subheader("Trabalhando")
    col1, col2, col3 = st.columns(3)
    with col1:
        df = pd.read_excel(dados, sheet_name="17 - Pessoas trabalhando ", header=1)
        df = df.apply(lambda col: pd.to_numeric(col, errors='coerce'))
        df = df.astype(int)
        col_x = df.columns[0] 
        col_y = df.columns[1] 
        fig4 = px.line(df, x=col_x, y=col_y, title="Pessoas trabalhando (1 000 pessoas)")

        fig4.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor",
            uniformtext_minsize=8,
            uniformtext_mode='hide',
        )
        max_val = df[col_y].max()
        fig4.update_yaxes(range=[0, max_val * 1.1]) 
        st.plotly_chart(fig4)   

    with col2:
        st.write("col2")
    with col3:
        st.write("col2")
 

elif st.session_state.page == "Rendimentos":
    st.write(st.session_state.page)
elif st.session_state.page == "Jovens":
    st.write(st.session_state.page)
elif st.session_state.page == "Desocupados":
    st.write(st.session_state.page)
elif st.session_state.page == "Subutilização":
    st.write(st.session_state.page)
