"""
Módulo 4 — Distribuições Teóricas
Ajuste e sobreposição de curvas de densidade teóricas sobre dados reais.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from src.core.pystatistics import (
    media,
    desvio_padrao,
    pdf_normal,
    pdf_exponencial,
    pdf_uniforme
)


def renderizar(df: pd.DataFrame):
    st.header("📈 Módulo 4 — Ajuste de Distribuições Teóricas")
    st.markdown(
        "Sobreposição de curvas probabilísticas teóricas ao histograma de densidade dos dados reais, "
        "com parâmetros estimados pelo **núcleo autoral (`pystatistics`)**."
    )

    if df is None or df.empty:
        st.warning("⚠️ Nenhum dado carregado. Acesse o **Módulo 0** para selecionar ou gerar os dados.")
        return

    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    if not colunas_numericas:
        st.warning("Nenhuma coluna numérica identificada nos dados.")
        return

    col1, col2 = st.columns(2)
    with col1:
        coluna_escolhida = st.selectbox("1. Selecione a Variável Numérica:", colunas_numericas)
    with col2:
        distribuicao = st.selectbox("2. Selecione a Distribuição Teórica:", ["Normal", "Exponencial", "Uniforme"])

    serie = pd.to_numeric(df[coluna_escolhida], errors="coerce").dropna()
    dados = serie.tolist()

    if len(dados) < 3:
        st.warning(f"A variável '{coluna_escolhida}' não possui dados suficientes.")
        return

    # Amostragem para plot ágil
    max_pts = 10000
    if len(dados) > max_pts:
        dados_plot = np.random.choice(dados, size=max_pts, replace=False).tolist()
    else:
        dados_plot = dados

    m = media(dados_plot)
    dp = desvio_padrao(dados_plot, amostral=True)
    min_val, max_val = min(dados_plot), max(dados_plot)

    if distribuicao == "Normal":
        st.info(f"**Parâmetros Estimados (Normal):** Média ($\mu$) = **{m:,.2f}** | Desvio Padrão ($\sigma$) = **{dp:,.2f}**")
    elif distribuicao == "Exponencial":
        lambd = 1.0 / m if m > 0 else 0.0001
        st.info(f"**Parâmetros Estimados (Exponencial):** Média ($\mu$) = **{m:,.2f}** | Taxa ($\lambda = 1/\mu$) = **{lambd:.6f}**")
    else:
        st.info(f"**Parâmetros Estimados (Uniforme):** Mínimo ($a$) = **{min_val:,.2f}** | Máximo ($b$) = **{max_val:,.2f}**")

    fig = go.Figure()

    # Histograma de densidade dos dados reais
    fig.add_trace(go.Histogram(
        x=dados_plot,
        histnorm="probability density",
        name="Dados Reais (Densidade)",
        opacity=0.6,
        marker_color="#1f77b4"
    ))

    eixo_x = np.linspace(min_val, max_val, 300)

    if distribuicao == "Normal":
        eixo_y = [pdf_normal(x, m, dp) for x in eixo_x]
    elif distribuicao == "Exponencial":
        lambd = 1.0 / m if m > 0 else 0.0001
        eixo_y = [pdf_exponencial(x, lambd) for x in eixo_x]
    else:
        eixo_y = [pdf_uniforme(x, min_val, max_val) for x in eixo_x]

    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=eixo_y,
        mode="lines",
        name=f"Curva Teórica ({distribuicao})",
        line=dict(color="red", width=3)
    ))

    fig.update_layout(
        title=f"Ajuste da Distribuição {distribuicao} sobre '{coluna_escolhida}'",
        xaxis_title=str(coluna_escolhida),
        yaxis_title="Densidade de Probabilidade",
        template="plotly_white",
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💡 Análise do Ajuste Teórico")
    if distribuicao == "Normal":
        st.markdown(
            "A **Distribuição Normal** pressupõe simetria em formato de sino ($Mean \approx Median$). "
            "Se o histograma real for muito assimétrico à direita (como em salários, capitais sociais ou faturamentos), "
            "o modelo Normal subestima a concentração inicial e superestima a cauda esquerda."
        )
    elif distribuicao == "Exponencial":
        st.markdown(
            "A **Distribuição Exponencial** modela tempos de espera ou grandezas com alta frequência próxima a zero "
            "e decaimento rápido. Muito comum em valores monetários e volumes de transações com caudas longas."
        )
    else:
        st.markdown(
            "A **Distribuição Uniforme Contínua** assume que qualquer valor no intervalo $[a, b]$ possui exatamente a mesma probabilidade "
            "de ocorrência. Rara em dados financeiros reais, mas útil para testes de ruído e números pseudoaleatórios."
        )
