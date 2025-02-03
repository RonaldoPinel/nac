import streamlit as st
import query2 as qr

# Carregar dados
df = qr.get_data()

# Verificar se as colunas existem antes de somar
if {"FILTROS", "IPIRANGA", "TEXACO"}.issubset(df.columns):
    # Calculando os totais
    filtros = df["FILTROS"].sum()
    ipiranga = df["IPIRANGA"].sum()
    texaco = df["TEXACO"].sum()

    # Arredondando valores
    total_filtros_formatado = round(filtros)
    total_ipi_formatado = round(ipiranga)
    total_tex_formatado = round(texaco)
    total = total_ipi_formatado + total_tex_formatado

    # Exibindo mensagens de meta
    if total_filtros_formatado >= 25360:
        st.title("Parabéns!!! Bateram a meta 2!")
    elif total_filtros_formatado >= 24257:
        st.title("Parabéns!!! Bateram a meta 1!")

    # Exibindo os totais
    st.title(f'**Total de Filtros: {total_filtros_formatado}.**')
    st.title(f'**Total de Litros Ipiranga: {total_ipi_formatado}.**')
    st.title(f'**Total de Litros Texaco: {total_tex_formatado}.**')
    st.title(f'**Total de Litros: {total}.**')

else:
    st.error("Erro: O DataFrame não contém todas as colunas esperadas.")
