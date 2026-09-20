"""
Módulo 5 — Correlação e Regressão Linear Simples
Análise da relação linear entre duas variáveis contínuas com MQO e interpretações.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from src.core.pystatistics import (
    correlacao_pearson,
    regressao_linear_simples
)


def renderizar(df: pd.DataFrame):
    st.header("📐 Módulo 5 — Correlação e Regressão Linear Simples")
    st.markdown(
        "Avaliação do relacionamento bivariado entre duas variáveis numéricas utilizando "
        "o **coeficiente de Pearson** e a **regressão por Mínimos Quadrados Ordinários (MQO)** autoral."
    )

    st.warning("⚠️ **Alerta Metodológico Fundamental:** *Correlação estatística não implica causalidade.*")

    if df is None or df.empty:
        st.warning("⚠️ Nenhum dado carregado. Acesse o **Módulo 0** para selecionar ou gerar os dados.")
        return

    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(colunas_numericas) < 2:
        st.error("O conjunto de dados precisa possuir pelo menos duas variáveis numéricas.")
        return

    st.subheader("🔍 Seleção das Variáveis")
    col1, col2 = st.columns(2)

    with col1:
        coluna_x = st.selectbox("Variável Independente / Explicativa (X):", colunas_numericas, index=0)

    colunas_y = [c for c in colunas_numericas if c != coluna_x]
    with col2:
        coluna_y = st.selectbox("Variável Dependente / Resposta (Y):", colunas_y, index=0)

    # Limpeza e preparação dos pares (X, Y)
    dados_biv = df[[coluna_x, coluna_y]].dropna().copy()
    dados_biv[coluna_x] = pd.to_numeric(dados_biv[coluna_x], errors="coerce")
    dados_biv[coluna_y] = pd.to_numeric(dados_biv[coluna_y], errors="coerce")
    dados_biv = dados_biv.dropna()

    if len(dados_biv) < 3:
        st.error("Número insuficiente de pares de observações válidos.")
        return

    # Amostragem para gráficos responsivos
    max_amostra = 10000
    if len(dados_biv) > max_amostra:
        dados_analise = dados_biv.sample(n=max_amostra, random_state=42)
        st.info(f"Usando amostra representativa de {max_amostra:,} de {len(dados_biv):,} registros para manter a navegação ágil.")
    else:
        dados_analise = dados_biv

    x = dados_analise[coluna_x].tolist()
    y = dados_analise[coluna_y].tolist()

    # Cálculos via pystatistics
    try:
        r = correlacao_pearson(x, y)
        b0, b1, r2 = regressao_linear_simples(x, y)
    except Exception as err:
        st.error(f"Erro no cálculo estatístico: {err}")
        return

    # Seção de Correlação
    st.subheader("📊 1. Coeficiente de Correlação de Pearson (r)")
    c_r1, c_r2 = st.columns(2)

    if abs(r) < 0.30:
        intensidade = "Fraca"
    elif abs(r) < 0.70:
        intensidade = "Moderada"
    else:
        intensidade = "Forte"

    if r > 0:
        sentido = "Positiva (Direta)"
    elif r < 0:
        sentido = "Negativa (Inversa)"
    else:
        sentido = "Nula"

    c_r1.metric("Coeficiente de Pearson (r)", f"{r:.4f}")
    c_r2.metric("Classificação da Associação", f"{intensidade} e {sentido}")

    st.divider()

    # Seção de Regressão Linear
    st.subheader("📐 2. Modelo de Regressão Linear (MQO)")

    sinal_b1 = "+" if b1 >= 0 else "-"
    st.latex(rf"\hat{{Y}} = {b0:.4f} {sinal_b1} {abs(b1):.4f} \cdot X")

    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Intercepto (β₀)", f"{b0:,.4f}")
    col_m2.metric("Coeficiente Angular (β₁ / Inclinação)", f"{b1:,.4f}")
    col_m3.metric("Coef. de Determinação (R²)", f"{r2:.4f} ({r2 * 100:.2f}%)")

    # Gráfico de Dispersão com Linha de Tendência
    x_min, x_max = min(x), max(x)
    x_linha = np.linspace(x_min, x_max, 200)
    y_linha = b0 + b1 * x_linha

    fig_reg = go.Figure()
    fig_reg.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        name="Dados Amostrais",
        marker=dict(color="#1f77b4", opacity=0.4, size=6)
    ))
    fig_reg.add_trace(go.Scatter(
        x=x_linha,
        y=y_linha,
        mode="lines",
        name="Reta de Regressão (MQO)",
        line=dict(color="red", width=3)
    ))

    fig_reg.update_layout(
        title=f"Dispersão e Reta de Regressão: {coluna_x} × {coluna_y}",
        xaxis_title=coluna_x,
        yaxis_title=coluna_y,
        template="plotly_white"
    )
    st.plotly_chart(fig_reg, use_container_width=True)

    # Interpretação dos Resultados
    st.subheader("💡 Interpretação dos Coeficientes")
    direcao = "aumenta em média" if b1 > 0 else "diminui em média"
    st.markdown(
        f"- **Coeficiente Angular ($\beta_1 = {b1:.4f}$):** Para cada aumento de 1 unidade em **{coluna_x}**, "
        f"a variável **{coluna_y}** {direcao} aproximadamente **{abs(b1):.4f}** unidade(s).\n"
        f"- **Intercepto ($\beta_0 = {b0:.4f}$):** Valor teórico esperado para **{coluna_y}** quando **{coluna_x} = 0**.\n"
        f"- **Qualidade do Ajuste ($R^2 = {r2*100:.2f}\\%$):** O modelo linear explica aproximadamente "
        f"**{r2*100:.2f}%** da variabilidade total observada em **{coluna_y}**."
    )

    st.divider()

    # Predição Interativa
    st.subheader("🔮 3. Predição Interativa (ŷ)")
    val_medio_x = float(np.mean(x))
    val_input_x = st.number_input(f"Insira um valor para {coluna_x}:", value=round(val_medio_x, 2))
    val_predito = b0 + b1 * val_input_x

    st.success(
        f"🎯 Para **{coluna_x} = {val_input_x:,.2f}**, a estimativa prevista de **{coluna_y}** é **{val_predito:,.2f}**."
    )
