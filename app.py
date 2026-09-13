import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.core.pystatistics import (
    correlacao_pearson,
    regrecao_linear_simples
)


# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

st.set_page_config(
    page_title="Laboratório Estatístico Interativo",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Laboratório Estatístico Interativo")
st.header("Módulo 5 — Correlação e Regressão Linear Simples")

st.write(
    "Análise da relação entre duas variáveis numéricas "
    "utilizando correlação de Pearson e regressão linear simples."
)

st.warning(
    "⚠️ Correlação não implica causalidade."
)


# ==========================================================
# CARREGAMENTO DO DATASET
# ==========================================================

st.subheader("📂 Carregamento dos dados")

arquivo = st.file_uploader(
    "Selecione o arquivo CSV do conjunto de dados",
    type=["csv"]
)

if arquivo is None:
    st.info(
        "Envie um arquivo CSV para iniciar a análise."
    )
    st.stop()


try:
    df = pd.read_csv(arquivo)

except Exception as erro:
    st.error(
        f"Não foi possível carregar o arquivo: {erro}"
    )
    st.stop()


st.success(
    f"Dataset carregado com sucesso: "
    f"{df.shape[0]:,} registros e {df.shape[1]} colunas."
)


# ==========================================================
# IDENTIFICAÇÃO DAS VARIÁVEIS NUMÉRICAS
# ==========================================================

st.subheader("🔎 Escolha das variáveis")

colunas_numericas = df.select_dtypes(
    include=np.number
).columns.tolist()


if len(colunas_numericas) < 2:
    st.error(
        "O dataset precisa possuir pelo menos duas "
        "variáveis numéricas."
    )
    st.stop()


coluna_x = st.selectbox(
    "Variável X — independente",
    colunas_numericas,
    index=0
)


colunas_y = [
    coluna for coluna in colunas_numericas
    if coluna != coluna_x
]


coluna_y = st.selectbox(
    "Variável Y — dependente",
    colunas_y,
    index=0
)


# ==========================================================
# PREPARAÇÃO DOS DADOS
# ==========================================================

dados = df[[coluna_x, coluna_y]].copy()


dados[coluna_x] = pd.to_numeric(
    dados[coluna_x],
    errors="coerce"
)


dados[coluna_y] = pd.to_numeric(
    dados[coluna_y],
    errors="coerce"
)


dados = dados.dropna()


if len(dados) < 3:
    st.error(
        "Não existem dados suficientes para realizar "
        "a análise."
    )
    st.stop()


# ==========================================================
# AMOSTRAGEM
# ==========================================================

MAX_AMOSTRA = 10000


if len(dados) > MAX_AMOSTRA:

    dados_analise = dados.sample(
        n=MAX_AMOSTRA,
        random_state=42
    )

    st.info(
        f"O dataset possui {len(dados):,} registros válidos. "
        f"Para manter a aplicação leve, foram utilizados "
        f"{MAX_AMOSTRA:,} registros como amostra."
    )

else:

    dados_analise = dados


x = dados_analise[coluna_x].tolist()
y = dados_analise[coluna_y].tolist()


# ==========================================================
# CORRELAÇÃO DE PEARSON
# ==========================================================

st.subheader("📈 Correlação de Pearson")


try:

    r = correlacao_pearson(x, y)

except Exception as erro:

    st.error(
        f"Erro no cálculo da correlação: {erro}"
    )
    st.stop()


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Coeficiente de correlação (r)",
        f"{r:.4f}"
    )


with col2:

    if abs(r) < 0.30:
        intensidade = "fraca"

    elif abs(r) < 0.70:
        intensidade = "moderada"

    else:
        intensidade = "forte"


    if r > 0:
        sentido = "positiva"

    elif r < 0:
        sentido = "negativa"

    else:
        sentido = "nula"


    st.metric(
        "Interpretação",
        f"{intensidade} e {sentido}"
    )


# ==========================================================
# REGRESSÃO LINEAR SIMPLES
# ==========================================================

st.subheader("📐 Regressão Linear Simples")


try:

    b0, b1, r2 = regrecao_linear_simples(
        x,
        y
    )

except Exception as erro:

    st.error(
        f"Erro no cálculo da regressão: {erro}"
    )
    st.stop()


# ==========================================================
# EQUAÇÃO DA RETA
# ==========================================================

st.write("### Equação da reta de regressão")


st.latex(
    rf"\hat{{Y}} = {b0:.4f} + ({b1:.4f})X"
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "β₀ — Intercepto",
        f"{b0:.4f}"
    )


with col2:

    st.metric(
        "β₁ — Coeficiente angular",
        f"{b1:.4f}"
    )


with col3:

    st.metric(
        "R²",
        f"{r2:.4f}"
    )


# ==========================================================
# GRÁFICO
# ==========================================================

st.subheader("📊 Gráfico de dispersão e reta de regressão")


x_array = np.array(x)
y_array = np.array(y)


ordem = np.argsort(x_array)


x_ordenado = x_array[ordem]


y_estimado = (
    b0 + b1 * x_ordenado
)


fig, ax = plt.subplots(
    figsize=(10, 6)
)


ax.scatter(
    x_array,
    y_array,
    alpha=0.5,
    label="Dados"
)


ax.plot(
    x_ordenado,
    y_estimado,
    linewidth=2,
    label="Reta de regressão"
)


ax.set_xlabel(coluna_x)
ax.set_ylabel(coluna_y)


ax.set_title(
    f"Regressão Linear: {coluna_x} × {coluna_y}"
)


ax.legend()


ax.grid(
    alpha=0.3
)


st.pyplot(fig)


# ==========================================================
# INTERPRETAÇÃO DOS COEFICIENTES
# ==========================================================

st.subheader("🧠 Interpretação dos resultados")


if b1 > 0:

    direcao = "aumenta"

elif b1 < 0:

    direcao = "diminui"

else:

    direcao = "permanece constante"


st.write(
    f"**β₁ = {b1:.4f}**. Para cada aumento de "
    f"1 unidade em **{coluna_x}**, o valor estimado "
    f"de **{coluna_y}** tende a {direcao} "
    f"aproximadamente **{abs(b1):.4f} unidade(s)**."
)


st.write(
    f"**β₀ = {b0:.4f}** representa o valor estimado "
    f"de **{coluna_y}** quando **{coluna_x} = 0**."
)


st.write(
    f"**R² = {r2:.4f}**, indicando que aproximadamente "
    f"**{r2 * 100:.2f}%** da variação de "
    f"**{coluna_y}** é explicada pelo modelo linear."
)


# ==========================================================
# PREVISÃO INTERATIVA
# ==========================================================

st.subheader("🔮 Predição Interativa")


valor_x = st.number_input(
    f"Digite um valor de {coluna_x}",
    value=float(np.mean(x))
)


previsao = (
    b0 + b1 * valor_x
)


st.success(
    f"Para **{coluna_x} = {valor_x:.4f}**, "
    f"a previsão de **{coluna_y}** é "
    f"**{previsao:.4f}**."
)


# ==========================================================
# AVISO FINAL
# ==========================================================

st.warning(
    "⚠️ Importante: correlação não implica causalidade. "
    "Uma associação estatística entre duas variáveis "
    "não significa que uma variável seja a causa da outra."
)
