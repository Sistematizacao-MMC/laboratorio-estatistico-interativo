"""
Módulo 2 — Estatística Descritiva Interativa
Calcula medidas de tendência central, dispersão, separatrizes, detecção de outliers
e gráficos interativos utilizando o núcleo estatístico autoral (pystatistics).
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from src.core.pystatistics import (
    media,
    mediana,
    moda,
    amplitude,
    variancia,
    desvio_padrao,
    coeficiente_variacao,
    percentil,
    quartis,
    detectar_outliers_iqr
)


def renderizar(df: pd.DataFrame):
    st.header("📊 Módulo 2 — Estatística Descritiva Interativa")
    st.markdown(
        "Explore a distribuição das variáveis do dataset através de medidas descritivas calculadas **"
        "pelo núcleo autoral (`pystatistics`)**, gráficos interativos e detecção automática de outliers."
    )

    if df is None or df.empty:
        st.warning("⚠️ Nenhum dado carregado. Por favor, acesse o **Módulo 0** para selecionar ou gerar os dados.")
        return

    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

    if not colunas_numericas:
        st.warning("Nenhuma coluna numérica identificada nos dados atuais.")
        return

    col_sel = st.selectbox("📌 Selecione a variável numérica para análise:", colunas_numericas)

    # Prepara lista de valores limpos
    serie = pd.to_numeric(df[col_sel], errors="coerce").dropna()
    dados = serie.tolist()

    if len(dados) < 2:
        st.error("A coluna selecionada não possui dados numéricos válidos suficientes para a análise.")
        return

    # Amostragem para evitar estouro de memória/tempo em datasets massivos
    max_itens = 20000
    if len(dados) > max_itens:
        st.info(f"ℹ️ Amostrando {max_itens:,} de {len(dados):,} registros para otimização do cálculo.")
        dados_calc = np.random.choice(dados, size=max_itens, replace=False).tolist()
    else:
        dados_calc = dados

    # Cálculos com o núcleo autoral
    m = media(dados_calc)
    med = mediana(dados_calc)
    modas = moda(dados_calc)
    amp = amplitude(dados_calc)
    var_amostral = variancia(dados_calc, amostral=True)
    dp_amostral = desvio_padrao(dados_calc, amostral=True)
    cv = coeficiente_variacao(dados_calc, amostral=True) if m != 0 else 0.0
    q1, q2, q3, iqr = quartis(dados_calc)
    outliers, lim_inf, lim_sup = detectar_outliers_iqr(dados_calc)
    pct_outliers = (len(outliers) / len(dados_calc)) * 100.0

    st.subheader("🎯 Medidas de Tendência Central e Dispersão")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Média (μ/x̄)", f"{m:,.2f}")
    c2.metric("Mediana (Md)", f"{med:,.2f}")
    moda_str = ", ".join([f"{x:,.2f}" for x in modas[:3]]) if modas else "Amodal"
    if len(modas) > 3:
        moda_str += f" (+{len(modas)-3})"
    c3.metric("Moda (Mo)", moda_str)
    c4.metric("Amplitude Total", f"{amp:,.2f}")

    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Variância Amostral (s²)", f"{var_amostral:,.2f}")
    c6.metric("Desvio Padrão Amostral (s)", f"{dp_amostral:,.2f}")
    c7.metric("Coef. de Variação (CV)", f"{cv:.2f}%")
    c8.metric("Dist. Interquartílica (IQR)", f"{iqr:,.2f}")

    st.divider()

    st.subheader("📦 Separatrizes e Detecção de Outliers (Método IQR)")
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)
    q_col1.metric("1º Quartil (Q1 - 25%)", f"{q1:,.2f}")
    q_col2.metric("2º Quartil (Q2 - 50%)", f"{q2:,.2f}")
    q_col3.metric("3º Quartil (Q3 - 75%)", f"{q3:,.2f}")
    q_col4.metric("Outliers Detectados", f"{len(outliers):,} ({pct_outliers:.1f}%)")

    st.caption(
        f"Regra dos 1.5×IQR: Limite Inferior = **{lim_inf:,.2f}** | Limite Superior = **{lim_sup:,.2f}**"
    )

    st.divider()

    # Visualizações Interativas
    st.subheader("📈 Gráficos Interativos")

    tab1, tab2, tab3 = st.tabs(["📊 Histograma", "📦 Boxplot", "📋 Tabela de Frequências"])

    with tab1:
        num_bins = st.slider("Número de Bins (Classes):", min_value=10, max_value=100, value=30, step=5)
        fig_hist = px.histogram(
            x=dados_calc,
            nbins=num_bins,
            title=f"Distribuição de Frequência — {col_sel}",
            labels={"x": col_sel, "y": "Contagem (Frequência Absoluta)"},
            color_discrete_sequence=["#1f77b4"]
        )
        fig_hist.add_vline(x=m, line_dash="dash", line_color="red", annotation_text="Média")
        fig_hist.add_vline(x=med, line_dash="dot", line_color="green", annotation_text="Mediana")
        fig_hist.update_layout(template="plotly_white")
        st.plotly_chart(fig_hist, use_container_width=True)

    with tab2:
        fig_box = px.box(
            y=dados_calc,
            title=f"Diagrama de Caixa (Boxplot) — {col_sel}",
            labels={"y": col_sel},
            color_discrete_sequence=["#2ca02c"]
        )
        fig_box.update_layout(template="plotly_white")
        st.plotly_chart(fig_box, use_container_width=True)

    with tab3:
        faixas = pd.cut(dados_calc, bins=10)
        tab_freq = pd.DataFrame(faixas.value_counts().sort_index())
        tab_freq.columns = ["Frequência Absoluta (fi)"]
        tab_freq["Frequência Relativa (fr)"] = (tab_freq["Frequência Absoluta (fi)"] / len(dados_calc)).round(4)
        tab_freq["Frequência Acumulada (Fi)"] = tab_freq["Frequência Absoluta (fi)"].cumsum()
        tab_freq["Frequência Rel. Acum. (%)"] = (tab_freq["Frequência Relativa (fr)"].cumsum() * 100).round(2)
        tab_freq.index.name = "Intervalo de Classe"
        st.dataframe(tab_freq, use_container_width=True)

    # Interpretação Automática
    st.subheader("💡 Diagnóstico Estatístico Automático")
    assimetria = ""
    if abs(m - med) / (dp_amostral if dp_amostral > 0 else 1.0) < 0.1:
        assimetria = "A distribuição é aproximadamente **simétrica** (média e mediana muito próximas)."
    elif m > med:
        assimetria = "A distribuição apresenta **assimetria positiva (à direita)** (média significativamente superior à mediana, impulsionada por valores altos/outliers)."
    else:
        assimetria = "A distribuição apresenta **assimetria negativa (à esquerda)** (média inferior à mediana)."

    dispersao = ""
    if cv < 15:
        dispersao = "O coeficiente de variação indica **baixa dispersão** (conjunto homogêneo, CV < 15%)."
    elif cv <= 30:
        dispersao = "O coeficiente de variação indica **média dispersão** (moderadamente heterogêneo, 15% ≤ CV ≤ 30%)."
    else:
        dispersao = "O coeficiente de variação indica **alta dispersão** (conjunto bastante heterogêneo, CV > 30%)."

    st.markdown(f"- **Forma:** {assimetria}")
    st.markdown(f"- **Dispersão:** {dispersao}")
    st.markdown(f"- **Valores Atípicos:** Foram identificados **{len(outliers):,}** valores fora das cercas de Tukey ({pct_outliers:.1f}% da amostra).")
