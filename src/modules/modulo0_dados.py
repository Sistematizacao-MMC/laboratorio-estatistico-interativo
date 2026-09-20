"""
Módulo 0 — Carga e Pré-processamento de Dados
Gerencia a leitura, seleção, amostragem e exploração preliminar dos dados.
"""

import os
import streamlit as st
import pandas as pd
import numpy as np


def gerar_dados_demonstracao() -> pd.DataFrame:
    """Gera um DataFrame sintético representativo de dados cadastrais empresariais."""
    np.random.seed(42)
    n = 1000
    capital_social = np.random.exponential(scale=50000, size=n) + 1000
    # Injeta alguns outliers realistas
    outliers_idx = np.random.choice(n, size=20, replace=False)
    capital_social[outliers_idx] = capital_social[outliers_idx] * np.random.uniform(5, 20, size=20)

    faturamento_estimado = capital_social * np.random.uniform(1.2, 3.5, size=n) + np.random.normal(5000, 2000, size=n)
    faturamento_estimado = np.maximum(faturamento_estimado, 500)

    tempo_atividade_anos = np.random.gamma(shape=3.0, scale=2.5, size=n)
    quantidade_socios = np.random.choice([1, 2, 3, 4, 5, 8], size=n, p=[0.55, 0.25, 0.12, 0.05, 0.02, 0.01])
    porte = np.random.choice(["ME (Microempresa)", "EPP (Pequeno Porte)", "Demais (Médio/Grande)"], size=n, p=[0.70, 0.22, 0.08])
    uf = np.random.choice(["SP", "RJ", "MG", "RS", "PR", "BA", "SC", "GO"], size=n, p=[0.30, 0.15, 0.12, 0.10, 0.10, 0.08, 0.08, 0.07])

    return pd.DataFrame({
        "capital_social": np.round(capital_social, 2),
        "faturamento_estimado": np.round(faturamento_estimado, 2),
        "tempo_atividade_anos": np.round(tempo_atividade_anos, 1),
        "quantidade_socios": quantidade_socios,
        "porte": porte,
        "uf": uf
    })


def renderizar():
    st.header("📁 Módulo 0 — Carga e Pré-processamento de Dados")
    st.markdown(
        "Carregue os dados do **CNPJ**, importe um arquivo **CSV próprio** ou utilize "
        "o **conjunto de dados de demonstração** integrado para explorar todas as ferramentas."
    )

    fonte = st.radio(
        "Selecione a fonte de dados:",
        ["Dataset de Demonstração (Empresas/CNPJ)", "Arquivo local da pasta `data/`", "Upload de CSV"],
        horizontal=True
    )

    df_carregado = None

    if fonte == "Dataset de Demonstração (Empresas/CNPJ)":
        st.info("💡 Usando conjunto simulado com 1.000 registros e variáveis numéricas e categóricas.")
        df_carregado = gerar_dados_demonstracao()

    elif fonte == "Arquivo local da pasta `data/`":
        pasta_data = "data"
        arquivos = [f for f in os.listdir(pasta_data) if f.endswith(".csv")] if os.path.exists(pasta_data) else []

        if not arquivos:
            st.warning("⚠️ Nenhum arquivo `.csv` encontrado na pasta `data/`. Execute `python data/download_dataset.py` ou use o Upload.")
        else:
            arq_selecionado = st.selectbox("Selecione o arquivo CSV:", arquivos)
            caminho = os.path.join(pasta_data, arq_selecionado)
            nrows = st.slider("Quantidade máxima de linhas para leitura rápida:", min_value=1000, max_value=50000, value=10000, step=1000)
            try:
                try:
                    df_carregado = pd.read_csv(caminho, sep=";", encoding="latin1", nrows=nrows)
                except Exception:
                    df_carregado = pd.read_csv(caminho, nrows=nrows)
            except Exception as e:
                st.error(f"Erro ao ler arquivo: {e}")

    elif fonte == "Upload de CSV":
        arquivo = st.file_uploader("Selecione um arquivo CSV no seu computador:", type=["csv"])
        if arquivo is not None:
            sep = st.text_input("Separador do CSV (deixe vazio para detecção automática):", value="")
            try:
                if sep:
                    df_carregado = pd.read_csv(arquivo, sep=sep)
                else:
                    try:
                        df_carregado = pd.read_csv(arquivo)
                    except Exception:
                        arquivo.seek(0)
                        df_carregado = pd.read_csv(arquivo, sep=";", encoding="latin1")
            except Exception as e:
                st.error(f"Erro ao processar CSV: {e}")

    if df_carregado is not None:
        st.session_state["df"] = df_carregado

        st.success(f"✅ Dados carregados com sucesso! Total de **{len(df_carregado):,}** linhas e **{len(df_carregado.columns)}** colunas.")

        col1, col2, col3 = st.columns(3)
        num_cols = df_carregado.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = df_carregado.select_dtypes(exclude=[np.number]).columns.tolist()

        col1.metric("Linhas", f"{len(df_carregado):,}")
        col2.metric("Colunas Numéricas", f"{len(num_cols)}")
        col3.metric("Colunas Categóricas", f"{len(cat_cols)}")

        st.subheader("🔍 Visualização das Primeiras Linhas")
        st.dataframe(df_carregado.head(10), use_container_width=True)

        st.subheader("📋 Resumo dos Tipos e Nulos")
        resumo = pd.DataFrame({
            "Tipo": df_carregado.dtypes.astype(str),
            "Valores Não-Nulos": df_carregado.notnull().sum(),
            "Valores Nulos": df_carregado.isnull().sum(),
            "% Nulos": (df_carregado.isnull().sum() / len(df_carregado) * 100).round(2)
        })
        st.dataframe(resumo, use_container_width=True)
