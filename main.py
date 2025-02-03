import streamlit as st
import pandas as pd
import query as qr
import altair as alt
import cx_Oracle

# Carregar dados e renomear colunas
df = qr.get_data()
df = df.rename(columns={"APELIDO": "Vendedor",
                        "CODEMP": "Empresa",
                        "CODVEND": "Cód. Vend.",
                        "LITROS_IPIRANGA": "Litros IPI",
                        "LITROS_TEXACO": "Litros Tex",
                        "TECFIL": "Tecfil",
                        "LITROS_TOTAL": "Litros Total"
                        })

with st.sidebar:
    st.title("Análise Posto Ipiranga") 

    distinct_vendedor = df["Vendedor"].unique().tolist()
    distinct_empresa = df["Empresa"].unique().tolist()

    # Usando multiselect para permitir seleção de múltiplos vendedores e empresas
    vendedores_selected = st.multiselect("Vendedores", distinct_vendedor)
    empresa_selected = st.multiselect("Empresa", distinct_empresa)

# Aplicando os filtros antes de calcular o total de litros
df_filtered = df.copy()
if vendedores_selected:
    df_filtered = df_filtered[df_filtered["Vendedor"].isin(vendedores_selected)]

if empresa_selected:
    df_filtered = df_filtered[df_filtered["Empresa"].isin(empresa_selected)]

# Calculando o total de Litros Total após aplicar os filtros
total_litros = df_filtered["Litros Total"].sum()

# Formatando o total de Litros Total para remover os decimais
total_litros_formatado = round(total_litros)

# Exibindo o total de Litros Total acima dos gráficos
st.write(f"**Total de Litros: {total_litros_formatado:,}**")

# Criando colunas para colocar os gráficos lado a lado
col1, col2 = st.columns([3, 1])  # Ajustando a proporção das colunas para aumentar a largura do gráfico de barras

with col1:
    # Criando o gráfico de barras com altair
    bar_chart = alt.Chart(df_filtered).mark_bar().encode(
        x='Vendedor:N',  # Eixo x com os nomes dos vendedores
        y='Litros Total:Q',  # Eixo y com os valores de volume
        color=alt.Color('Vendedor:N', legend=None),  # Define a cor das barras com base no "Vendedor"
        tooltip=['Vendedor', 'Litros Total']  # Exibe os valores ao passar o mouse
    ).properties(
        width=700,  # Aumentando a largura do gráfico
        height=400  # Altura do gráfico
    )
    st.altair_chart(bar_chart, use_container_width=True)

with col2:
    # Criando o gráfico de pizza com altair
    pie_chart = alt.Chart(df_filtered).mark_arc().encode(
        theta=alt.Theta(field="Litros Total", type="quantitative"),  # Tamanho das fatias
        color=alt.Color(field="Vendedor", type="nominal", legend=None),  # Cor das fatias
        tooltip=['Vendedor', 'Litros Total']  # Exibe os valores ao passar o mouse
    ).properties(
        width=400,  # Largura do gráfico
        height=400  # Altura do gráfico
    )
    st.altair_chart(pie_chart, use_container_width=True)

# Exibir a tabela abaixo dos gráficos
st.dataframe(df_filtered, use_container_width=True)
