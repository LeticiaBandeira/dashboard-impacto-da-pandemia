import streamlit as st
import pandas as pd
import plotly.express as px

tema = st.context.theme.type
ICON = "img/InSOCIO_c.png" if tema == "dark" else "img/InSOCIO_p.png"
st.logo(ICON, size="small")

st.set_page_config(page_title="InSocio - Indicadores Sociais da Pandemia", page_icon="📊", layout="wide")

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
    st.markdown("Neste dashboard serão apresentados os impactos da pandemia da covid-19 nos Indicadores Sociais (IS) de trabalho e rendimentos do Rio Grande do Norte (RN) com base nos dados da Síntese de Indicadores Sociais (SIS) produzida pelo Instituto Brasileiro de Geografia e Estatísticado (IBGE).")

    st.subheader("Dados Gerais")
    st.markdown("Esta seção apresenta os indicadores sociais gerais relacionados ao trabalho.")
    col1, col2, col3 = st.columns(3)
    with col1:
        #População em idade de trabalhar
        df = pd.read_json("dados/dados_dash.populacao_em_idade_de_trabalhar.json")
        fig1 = px.bar(df, x=df.columns[2], y=df.columns[3], title="População em idade de trabalhar (1 000 pessoas)")

        fig1.update_traces(textposition="outside")
        fig1.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )

        st.plotly_chart(fig1, key="gerais1")

    with col2:
        #População na força de trabalho
        df = pd.read_json("dados/dados_dash.populacao_na_forca_de_trabalho.json")   
        fig2 = px.bar(df, x=df.columns[2], y=df.columns[3], title="População na força de trabalho (1 000 pessoas)")

        fig2.update_traces(textposition="outside")
        fig2.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )

        st.plotly_chart(fig2, key="gerais2")    
    with col3:
        #Força de trabalho potencial
        df = pd.read_json("dados/dados_dash.populacao_na_forca_de_trabalho_potencial.json")
        fig3 = px.line(df, x=df.columns[2], y=df.columns[3], title="População na força de trabalho potencial (1 000 pessoas)")

        fig3.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )
        max_val = df[df.columns[3]].max()
        fig3.update_yaxes(range=[0, max_val * 1.1]) 
        st.plotly_chart(fig3, key="gerais3")   
    
elif st.session_state.page == "Trabalhando":
    st.subheader("Trabalhando")
    st.markdown("Nesta seção são apresentados os dados da população ocupada (população trabalhando).")
    col1, col2, col3 = st.columns(3)
    with col1:
        #População trabalhando 
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando.json")
        fig4 = px.line(df, x=df.columns[2], y=df.columns[3], title="Pessoas trabalhando (1 000 pessoas)")

        fig4.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )
        max_val = df[df.columns[3]].max()
        fig4.update_yaxes(range=[0, max_val * 1.1]) 
        st.plotly_chart(fig4, key="trabalhando1")   

        #Pessoas trabalhando de acordo com a idade %
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando_por_grupos_de_idade.json")

        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["14 a 29 anos", "30 a 49 anos", "50 a 59 anos","60 anos ou mais"],
                  var_name="Grupos de idade", 
                  value_name="Valor")
        
        fig5 = px.bar(df_long, 
             x="Valor", 
             y="Ano", 
             color="Grupos de idade", 
             orientation='h',
             barmode="stack", 
             labels={"Valor": "Valor", "Ano": "Ano", "Grupos de idade": "Grupos de idade"},
             title="Pessoas trabalhando por grupos de idade (%)")
        
        fig5.update_xaxes(range=[0, 100]) 
        st.plotly_chart(fig5, key="trabalhando2") 
    
    with col2:
        #Pessoas trabalhando de acordo com sexo %
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando_desagregado_por_sexo.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Homens", "Mulheres"],
                  var_name="Sexo", 
                  value_name="Valor")
        
        fig6 = px.bar(df_long, 
             x="Valor", 
             y="Ano", 
             color="Sexo", 
             orientation='h',
             barmode="stack", 
             labels={"Valor": "Valor", "Ano": "Ano", "Sexo": "Sexo"},
             title="Pessoas trabalhando desagregado por sexo (%)")

        
        fig6.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig6.update_xaxes(range=[0, 100]) 
        st.plotly_chart(fig6, key="trabalhando3")

        #Pessoas trabalhando de acordo com seu gênero e sua cor/raça %
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando_por_sexo_e_cor_ou_raca.json")

        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Homem branco", "Homem preto ou pardo", "Mulher branca", "Mulher preta ou parda"],
                  var_name="Sexo e cor/raça", 
                  value_name="Valor")
        
        fig7 = px.bar(df_long, 
             x="Valor", 
             y="Ano", 
             color="Sexo e cor/raça", 
             orientation='h',
             barmode="stack", 
             labels={"Valor": "Valor", "Ano": "Ano", "Sexo e cor/raça": "Sexo e cor/raça"},
             title="Pessoas trabalhando por sexo e cor ou raça (%)")

        fig7.update_xaxes(range=[0, 100]) 
        st.plotly_chart(fig7, key="trabalhando4")
        
    with col3:
        #Pessoas trabalhando de acordo com cor/raça %
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando_desagregado_por_cor_ou_raca.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Branca", "Preta", "Parda"],
                  var_name="Cor ou Raça", 
                  value_name="Valor")
        
        fig8 = px.bar(df_long, 
             x="Valor", 
             y="Ano", 
             color="Cor ou Raça", 
             orientation='h',
             barmode="stack", 
             labels={"Valor": "Valor", "Ano": "Ano", "Cor ou Raça": "Cor ou Raça"},
             title="Pessoas trabalhando desagregado por cor ou raça (%)")

        
        fig8.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig8.update_xaxes(range=[0, 100]) 
        st.plotly_chart(fig8, key="trabalhando5") 

        #Trabalhadores de acordo com nível de instrução %
        df = pd.read_json("dados/dados_dash.pessoas_trabalhando_de_acordo_com_nivel_de_instrucao.json")
    
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                      "Sem instrução ou fundamental incompleto", 
                      "Ensino fundamental completo ou médio incompleto", 
                      "Ensino médio completo ou superior incompleto", 
                      "Ensino superior completo"
                      ],
                  var_name="Nível de instrução", 
                  value_name="Valor")
        
        fig9 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Nível de instrução", 
             barmode="stack",
             labels={"Valor": "Valor", "Ano": "Ano", "Nível de instrução": "Nível de instrução"},
             title="Pessoas trabalhando de acordo com o nível de instrução (%)")  
        
        fig9.update_yaxes(range=[0, 100]) 
        st.plotly_chart(fig9, key="trabalhando6")
        
    col4, col5 = st.columns(2)
    with col4:
        #Pessoas ocupadas de acordo com carga horária de trabalho %
        df = pd.read_json("dados/dados_dash.percentuais_das_pessoas_ocupadas_de_acordo_com_carga_horaria_de_trabalho.json")
        
        df_long = pd.melt(df, id_vars=["Ano"],
                    value_vars=[
                        "Até 14 horas",
                        "De 15 a 30 horas",
                        "De 31 a 39 horas", 
                        "De 40 a 44 horas",
                        "De 45 a 48 horas",
                        "49 horas ou mais"
                    ],
                    var_name="Carga Horária",
                    value_name="Valor")
        
        fig10 = px.line(df_long,
                x="Ano",
                y="Valor",
                color="Carga Horária",
                labels={"Valor": "Valor", "Ano": "Ano", "Carga Horária": "Carga Horária"},
                title="Pessoas trabalhando de acordo com carga de horária de trabalho (%)")
        
        fig10.update_yaxes(range=[0, df_long["Valor"].max() * 1.5])
        st.plotly_chart(fig10, key="trabalhando7")
        
    with col5:
        #Pessoas ocupadas de acordo com a posição na ocupação %
        df = pd.read_json("dados/dados_dash.distribuicao_das_pessoas_ocupadas_de_acordo_com_posicao_na_ocupacao.json")
        
        df_long = pd.melt(df, id_vars=["Ano"],
                    value_vars=[
                        "Empregado (CTPS)",
                        "Empregado (informal)",
                        "Trabalhador doméstico (CTPS)",
                        "Trabalhador doméstico (informal)",
                        "Militar ou funcionário público estatutário",
                        "Conta própria",
                        "Empregador"
                    ],
                    var_name="Posição Ocupada",
                    value_name="Valor")
        
        fig11 = px.line(df_long,
                x="Ano",
                y="Valor",
                color="Posição Ocupada",
                labels={"Valor": "Valor", "Ano": "Ano", "Posição Ocupada": "Posição Ocupada"},
                title="Pessoas trabalhando de acordo com posição ocupada (%)")
        
        fig11.update_yaxes(range=[0, df_long["Valor"].max() * 1.5])
        st.plotly_chart(fig11, key="trabalhando8")
    
    col6, col7, col8 = st.columns(3)
    with col6:
        #População trabalhando em trabalhos formais
        df = pd.read_json("dados/dados_dash.populacao_trabalhando_em_trabalhos_formais.json")
        fig12 = px.bar(df, x=df.columns[2], y=df.columns[3], title="População trabalhando em trabalhos formais (1 000 pessoas)")

        fig12.update_traces(textposition="outside")
        fig12.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )

        st.plotly_chart(fig12, key="trabalhando9")
    with col7:
        #Pessoas ocupadas em trabalhos formais por gênero %
        df = pd.read_json("dados/dados_dash.proporcao_em_trabalhos_formais_por_genero.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Homens", "Mulheres"],
                  var_name="Sexo", 
                  value_name="Valor")
        
        fig13 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Sexo", 
             barmode="group", 
             labels={"Valor": "Valor", "Ano": "Ano", "Sexo": "Sexo"},
             title="Pessoas trabalhando em trabalhos formais de acordo com gênero (%)")
        
        fig13.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="right",
        x=0.6
        ))
        
        fig13.update_yaxes(range=[0, df_long["Valor"].max() * 1.1]) 
        st.plotly_chart(fig13, key="trabalhando10")
        
    with col8:
        #Ocupadas em trabalhos formais por cor ou raça %
        df = pd.read_json("dados/dados_dash.pessoas_em_trabalhos_formais_por_cor_ou_raca.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Branca", "Preta", "Parda"],
                  var_name="Cor ou raça", 
                  value_name="Valor")
        
        fig14 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Cor ou raça", 
             barmode="group", 
             labels={"Valor": "Valor", "Ano": "Ano", "Cor ou raça": "Cor ou raça"},
             title="Pessoas trabalhando em trabalhos formais de acordo com cor ou raça (%)")
        
        fig14.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="right",
        x=0.8
        ))
        
        fig14.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig14, key="trabalhando11")

elif st.session_state.page == "Rendimentos":
    st.subheader("Rendimento")
    st.markdown("Nesta seção são apresentados os indicadores referentes aos rendimentos da população ocupada.")
    col1, col2 = st.columns(2)
    with col1:
        #Rendimento médio por hora de acordo com nível de instrução R$
        df = pd.read_json("dados/dados_dash.rendimento_medio_hora_de_acordo_com_nivel_de_instrucao.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                    "Sem instrução ou fundamental incompleto",
                    "Ensino fundamental completo ou médio incompleto",
                    "Ensino médio completo ou superior incompleto",
                    "Ensino superior completo"
                    ],
                  var_name="Nível de Instrução", 
                  value_name="Valor")
        
        fig15 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Nível de Instrução", 
             barmode="group", 
             labels={"Valor": "Valor", "Ano": "Ano", "Nível de Instrução": "Nível de Instrução"},
             title="Rendimento médio por hora de acordo com o nível de instrução (R$)")
        
        fig15.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.9,
        xanchor="right",
        x=0.8
        ))
        
        fig15.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
        st.plotly_chart(fig15, key="rendimentos1")
        
        #Rendimento médio por hora de todos os trabalhadores R$
        df = pd.read_json("dados/dados_dash.rendimento_medio_hora_de_todos_os_trabalhadores.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                    "Rendimento-hora médio real habitual do trabalho principal (R$/hora)",
                    "Rendimento-hora médio real habitual de todos os trabalhos (R$/hora)"
                    ],
                  var_name="Tipo", 
                  value_name="Valor")
        
        fig16 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Tipo", 
             barmode="group", 
             labels={"Valor": "Valor", "Ano": "Ano", "Tipo": ""},
             title="Rendimento médio por hora de todos os trabalhadores  (R$)")
        
        fig16.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=0.9,
        xanchor="right",
        x=0.55
        ))
        
        fig16.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
        st.plotly_chart(fig16, key="rendimentos2")
        
    with col2:
        #Rendimento medio mensal de acordo com a posição na ocupação R$
        df = pd.read_json("dados/dados_dash.rendimento_medio_mensal_de_acordo_com_posicao_ocupada.json")
        
        df_long = pd.melt(df, id_vars=["Ano"],
                    value_vars=[
                        "Empregado (CTPS)",
                        "Empregado (sem CTPS)",
                        "Trabalhador doméstico (CTPS)",
                        "Trabalhador doméstico (sem CTPS)",
                        "Militar ou funcionário público estatutário",
                        "Conta própria",
                        "Empregador"
                    ],
                    var_name="Posição Ocupada",
                    value_name="Valor")
        
        fig17 = px.line(df_long,
                x="Ano",
                y="Valor",
                color="Posição Ocupada",
                labels={"Valor": "Valor", "Ano": "Ano", "Posição Ocupada": "Posição Ocupada"},
                title="Rendimento médio mensal de acordo com posição ocupada (R$)")
        
        fig17.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
        st.plotly_chart(fig17, key="rendimentos3")

        #Rendimento medio mensal de todos os trabalhadores R$
        df = pd.read_json("dados/dados_dash.rendimento_medio_mensal_de_todos_os_trabalhadores.json")
        
        df_long = pd.melt(df, id_vars=["Ano"],
                    value_vars=[
                    "Rendimento médio real habitual do trabalho principal (R$/mês)",
                    "Rendimento médio real habitual de todos os trabalhos (R$/mês)"
                    ],
                    var_name="Tipo",
                    value_name="Valor")
        
        fig18 = px.line(df_long,
                x="Ano",
                y="Valor",
                color="Tipo",
                labels={"Valor": "Valor", "Ano": "Ano", "Tipo": ""},
                title="Rendimento médio mensal de todos os trabalhadores (R$)")
        
        fig18.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
        st.plotly_chart(fig18, key="rendimentos4")
        
elif st.session_state.page == "Jovens":
    st.subheader("Jovens")
    st.markdown("Nesta seção são mostrados os indicadores referentes a população jovem (dos 15 aos 29 anos).")
    
    #Jovens de acordo com seu status de ocupação 
    df = pd.read_json("dados/dados_dash.distribuicao_de_jovens_de_acordo_com_status_de_ocupacao.json")
        
    df_long = pd.melt(df, id_vars=["Ano"],
                value_vars=[
                "Só estuda",
                "Estuda e está trabalhando", 
                "Só está trabalhando",
                "Não estuda e não está trabalhando"
                ],
                var_name="Status",
                value_name="Valor")
        
    fig19 = px.line(df_long,
            x="Ano",
            y="Valor",
            color="Status",
            labels={"Valor": "Valor", "Ano": "Ano", "Status": "Status"},
            title="Distribuição dos jovens de acordo com seu status de ocupação (1 000 pessoas)")
        
    fig19.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
    st.plotly_chart(fig19, key="jovens1")
   
    #Jovens de 15 a 29 anos de acordo com situação de ocupação e condição de estudo %
    df = pd.read_json("dados/dados_dash.grupos_de_jovens_por_situacao_de_ocupacao_e_estudo.json")
    
    df_long = pd.melt(df, id_vars=["Ano", "Faixa etária"],
                value_vars=[
                    "Só estuda",
                    "Estuda e está trabalhando",
                    "Só está trabalhando",
                    "Não estuda e não está trabalhando"
                ],
                var_name="Status",
                value_name="Valor")
    
    fig20 = px.bar(df_long, 
             x="Ano", 
             y="Valor", 
             color="Status", 
             barmode="stack",
             facet_col="Faixa etária",
             labels={"Valor": "Valor", "Ano": "Ano", "Faixa etária": "Faixa etária"},
             title="Jovens de 15 a 29 anos de acordo com a situação de ocupação e condição de estudo (%)")
    
    fig20.update_yaxes(range=[0, 100])
    st.plotly_chart(fig20, key="jovens2")

elif st.session_state.page == "Desocupados":
    st.subheader("Desocupados")
    st.markdown("Nesta seção são mostrados os indicadores referentes a população desocupada (população que não está trabalhando).")
    
    col1, col2 = st.columns(2)
    with col1:
        #População desocupada
        df = pd.read_json("dados/dados_dash.populacao_desocupada.json")
        fig21 = px.line(df, x=df.columns[2], y=df.columns[3], title="População desocupada (1 000 pessoas)")

        fig21.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )
        fig21.update_yaxes(range=[0, df["Valor"].max() * 1.2]) 
        st.plotly_chart(fig21, key="desocupados1")  
        
        #Desocupação por cor ou raça %
        df = pd.read_json("dados/dados_dash.taxa_desocupacao_desgregada_por_cor_ou_raca.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Branca", "Preta ou Parda"],
                  var_name="Cor ou raça", 
                  value_name="Valor")
        
        fig22 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Cor ou raça", 
             labels={"Valor": "Valor", "Ano": "Ano", "Cor ou raça": "Cor ou raça"},
             title="Taxa de desocupação por cor ou raça (%)")

        fig22.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig22.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig22, key="desocupados2")
    with col2:
        #Desocupação por sexo %
        df = pd.read_json("dados/dados_dash.taxa_desocupacao_desgregada_por_sexo.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Homens", "Mulheres"],
                  var_name="Sexo", 
                  value_name="Valor")
        
        fig23 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Sexo", 
             labels={"Valor": "Valor", "Ano": "Ano", "Sexo": "Sexo"},
             title="Taxa de desocupação por sexo (%)")

        
        fig23.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig23.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig23, key="desocupados3")
        
        #Desocupação por grupos de idade %
        df = pd.read_json("dados/dados_dash.taxa_desocupacao_desgregada_por_grupos_de_idade.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                      "14 a 29 anos",
                      "30 a 49 anos",
                      "50 anos ou mais"],
                  var_name="Grupos de Idade", 
                  value_name="Valor")
        
        fig24 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Grupos de Idade", 
             labels={"Valor": "Valor", "Ano": "Ano", "Grupos de Idade": "Grupos de Idade"},
             title="Taxa de desocupação por grupos de idade (%)")

        
        fig24.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig24.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig24, key="desocupados4")
    
    #Pessoas desocupadas e procurando emprego agrupadas por tempo %      
    df = pd.read_json("dados/dados_dash.pessoas_desocupadas_procurando_trabalho_agrupadas_por_tempo.json")
    
    df_long = pd.melt(df, id_vars=["Ano"], 
                value_vars=[
                     "Até um mês", 
                     "Mais de um mês a menos de um ano",
                     "De um ano a menos de dois anos",
                     "Dois anos ou mais"
                      ],
                var_name="Tempo", 
                value_name="Valor")
        
    fig25 = px.bar(df_long, 
            x="Ano", 
            y="Valor", 
            color="Tempo", 
            barmode="stack",
            labels={"Valor": "Valor", "Ano": "Ano", "Tempo": "Tempo"},
            title="Pessoas desocupadas e procurando emprego agrupadas por tempo (%)")  
        
    fig25.update_yaxes(range=[0, 100]) 
    st.plotly_chart(fig25, key="desocupados5")

elif st.session_state.page == "Subutilização":
    st.subheader("Subutilizados")
    st.markdown("Nesta seção são mostrados os indicadores referentes a população subutilizada. Esse grupo é composto po todas as pessoas desempregadas, aquelas que trabalham menos horas do que poderiam, as que estão disponíveis para trabalhar mas não buscaram emprego e também as que procuraram emprego, mas não estavam disponíveis para assumir uma vaga..")
    col1, col2 = st.columns(2)
    
    with col1:
       
        #População subutilizada 
        df = pd.read_json("dados/dados_dash.populacao_subutilizada.json")
        fig26 = px.line(df, x=df.columns[2], y=df.columns[3], title="População subutilizada (1 000 pessoas)")

        fig26.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )
        fig26.update_yaxes(range=[0, df["Valor"].max() * 1.2]) 
        st.plotly_chart(fig26, key="subutilizados1")
        
        #Subutilização da força de trabalho desagregado por sexo %
        df = pd.read_json("dados/dados_dash.subutilizacao_forca_trabalho_desagrupada_por_sexo.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=["Homens", "Mulheres"],
                  var_name="Sexo", 
                  value_name="Valor")
        
        fig27 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Sexo", 
             labels={"Valor": "Valor", "Ano": "Ano", "Sexo": "Sexo"},
             title="Subutilização da força de trabalho desagregada por sexo (%)")

        
        fig27.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig27.update_yaxes(range=[0, df_long["Valor"].max() * 1.2])
        st.plotly_chart(fig27, key="subutilizados2")
        
        #Subutilização da força de trabalho desagregado por grupos de idade %
        df = pd.read_json("dados/dados_dash.subutilizacao_forca_trabalho_desagrupada_por_grupos_de_idade.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                      "14 a 29 anos",
                      "30 a 49 anos",
                      "50 anos ou mais"],
                  var_name="Grupos de Idade", 
                  value_name="Valor")
        
        fig28 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Grupos de Idade", 
             labels={"Valor": "Valor", "Ano": "Ano", "Grupos de Idade": "Grupos de Idade"},
             title="Subutilização da força de trabalho desagregada por grupos de idade (%)")

        
        fig28.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig28.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig28, key="subutilizados3")
    with col2:
        
        #Subutilização da força de trabalho ao longo dos anos %
        df = pd.read_json("dados/dados_dash.porcentagem_subutilizacao_da_forca_de_trabalho.json")
        fig29 = px.line(df, x=df.columns[2], y=df.columns[3], title="Subutilização da força de trabalho ao longo dos anos (%)")

        fig29.update_layout(
            xaxis_title="Ano",
            yaxis_title="Valor"
        )
        fig29.update_yaxes(range=[0, df["Valor"].max() * 1.2]) 
        st.plotly_chart(fig29, key="subutilizados")
        
        #Subutilização da força de trabalho desagregado por cor ou raça %
        df = pd.read_json("dados/dados_dash.subutilizacao_forca_trabalho_desagrupada_por_grupos_de_idade.json")
        
        df_long = pd.melt(df, id_vars=["Ano"], 
                  value_vars=[
                      "14 a 29 anos",
                      "30 a 49 anos",
                      "50 anos ou mais"],
                  var_name="Grupos de Idade", 
                  value_name="Valor")
        
        fig30 = px.line(df_long, 
             x="Ano", 
             y="Valor", 
             color="Grupos de Idade", 
             labels={"Valor": "Valor", "Ano": "Ano", "Grupos de Idade": "Grupos de Idade"},
             title="Subutilização da força de trabalho desagregada por grupos de idade (%)")

        
        fig30.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.0,
        xanchor="center",
        x=0.5
        ))
        
        fig30.update_yaxes(range=[0, df_long["Valor"].max() * 1.2]) 
        st.plotly_chart(fig30, key="subutilizados5")