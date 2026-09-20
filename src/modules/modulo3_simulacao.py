"""
Módulo 3 — Probabilidade e Simulação (Monte Carlo)
Demonstração interativa da Lei dos Grandes Números (LGN) e do Teorema Central do Limite (TCL).
"""

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

from src.core.pystatistics import media, desvio_padrao, pdf_normal


def renderizar():
    st.header("🎲 Módulo 3 — Probabilidade e Simulação (Monte Carlo)")
    st.markdown(
        "Explore conceitos fundamentais da teoria das probabilidades por meio de simulações interativas "
        "com o **núcleo de cálculo autoral (`pystatistics`)**."
    )

    aba1, aba2 = st.tabs(["📜 Lei dos Grandes Números (LGN)", "🔔 Teorema Central do Limite (TCL)"])

    # ---------------------------------------------------------
    # ABA 1: LEI DOS GRANDES NÚMEROS (LGN)
    # ---------------------------------------------------------
    with aba1:
        st.subheader("1. Convergência da Média Amostral (LGN)")
        st.markdown(
            "A **Lei dos Grandes Números** estabelece que, conforme o número de experimentos ($n$) aumenta, "
            "a média amostral ($\bar{X}_n$) converge quase certamente para o valor esperado teórico ($E[X] = \mu$)."
        )

        col1, col2 = st.columns(2)
        with col1:
            experimento = st.selectbox(
                "Escolha o experimento aleatório:",
                ["Lançamento de Moeda Justa (Bernoulli, p=0.5)",
                 "Lançamento de Dado D6 Equilibrado (1 a 6)",
                 "Tempo de Espera Exponencial (λ = 0.2, μ = 5.0)"]
            )
        with col2:
            num_tentativas = st.slider("Número de repetições (n):", min_value=50, max_value=5000, value=1000, step=50)

        # Geração dos ensaios
        np.random.seed(42)
        if "Moeda" in experimento:
            valores = np.random.choice([0, 1], size=num_tentativas)
            mu_teorico = 0.5
            nome_var = "Proporção de Caras"
        elif "Dado" in experimento:
            valores = np.random.randint(1, 7, size=num_tentativas)
            mu_teorico = 3.5
            nome_var = "Média dos Resultados do Dado"
        else:
            valores = np.random.exponential(scale=5.0, size=num_tentativas)
            mu_teorico = 5.0
            nome_var = "Média Amostral de Tempos"

        # Cálculo da média acumulada
        soma_cumulativa = np.cumsum(valores)
        ensaios = np.arange(1, num_tentativas + 1)
        medias_cumulativas = soma_cumulativa / ensaios
        media_final = medias_cumulativas[-1]

        fig_lgn = go.Figure()
        fig_lgn.add_trace(go.Scatter(
            x=ensaios,
            y=medias_cumulativas,
            mode="lines",
            name="Média Amostral Acumulada",
            line=dict(color="#1f77b4", width=2)
        ))
        fig_lgn.add_trace(go.Scatter(
            x=[1, num_tentativas],
            y=[mu_teorico, mu_teorico],
            mode="lines",
            name=f"Esperança Teórica (μ = {mu_teorico:.2f})",
            line=dict(color="red", dash="dash", width=2.5)
        ))

        fig_lgn.update_layout(
            title=f"LGN: Convergência de {nome_var} para μ = {mu_teorico}",
            xaxis_title="Número de Ensaios (n)",
            yaxis_title="Média Acumulada",
            template="plotly_white",
            legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
        )
        st.plotly_chart(fig_lgn, use_container_width=True)

        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("Valor Teórico (E[X])", f"{mu_teorico:.4f}")
        m_col2.metric(f"Média Observada (n={num_tentativas})", f"{media_final:.4f}")
        m_col3.metric("Erro Absoluto", f"{abs(media_final - mu_teorico):.4f}")

    # ---------------------------------------------------------
    # ABA 2: TEOREMA CENTRAL DO LIMITE (TCL)
    # ---------------------------------------------------------
    with aba2:
        st.subheader("2. Teorema Central do Limite (TCL)")
        st.markdown(
            "O **TCL** garante que a soma ou média de um grande número de variáveis aleatórias independentes e "
            "identicamente distribuídas (i.i.d.) aproxima-se de uma **Distribuição Normal**, "
            "independentemente do formato da distribuição original da população!"
        )

        c_dist, c_n, c_k = st.columns(3)
        with c_dist:
            dist_origem = st.selectbox(
                "Distribuição original da população:",
                ["Exponencial (Muito Assimétrica)", "Uniforme Contínua [0, 10]", "Bimodal (Mistura de Normais)"]
            )
        with c_n:
            tamanho_amostra = st.slider("Tamanho de cada amostra (n):", min_value=2, max_value=100, value=30, step=1)
        with c_k:
            num_amostras = st.slider("Quantidade de amostras simuladas (K):", min_value=100, max_value=3000, value=1000, step=100)

        # Geração da população e cálculo das médias amostrais
        np.random.seed(42)
        medias_amostrais = []

        if "Exponencial" in dist_origem:
            pop_mu = 5.0
            pop_sigma = 5.0
            gerador = lambda: np.random.exponential(scale=5.0, size=tamanho_amostra)
        elif "Uniforme" in dist_origem:
            pop_mu = 5.0
            pop_sigma = np.sqrt((10 - 0)**2 / 12.0)
            gerador = lambda: np.random.uniform(0.0, 10.0, size=tamanho_amostra)
        else: # Bimodal
            pop_mu = 5.0
            pop_sigma = 2.5
            gerador = lambda: np.concatenate([
                np.random.normal(2.5, 0.8, size=tamanho_amostra // 2),
                np.random.normal(7.5, 0.8, size=tamanho_amostra - tamanho_amostra // 2)
            ])

        for _ in range(num_amostras):
            amostra = gerador().tolist()
            # Utiliza a função autoral de média
            medias_amostrais.append(media(amostra))

        # Estatísticas das médias amostrais calculadas via núcleo autoral
        m_medias = media(medias_amostrais)
        dp_medias = desvio_padrao(medias_amostrais, amostral=True)
        erro_padrao_teorico = pop_sigma / np.sqrt(tamanho_amostra)

        # Plotly Histogram + Normal Curve
        fig_tcl = go.Figure()
        fig_tcl.add_trace(go.Histogram(
            x=medias_amostrais,
            histnorm="probability density",
            name="Distribuição das Médias Amostrais",
            opacity=0.6,
            marker_color="#2ca02c"
        ))

        # Curva normal teórica
        eixo_x = np.linspace(min(medias_amostrais), max(medias_amostrais), 250)
        eixo_y = [pdf_normal(x, pop_mu, erro_padrao_teorico) for x in eixo_x]

        fig_tcl.add_trace(go.Scatter(
            x=eixo_x,
            y=eixo_y,
            mode="lines",
            name="Normal Teórica N(μ, σ/√n)",
            line=dict(color="red", width=3)
        ))

        fig_tcl.update_layout(
            title=f"TCL: Distribuição Amostral da Média (n = {tamanho_amostra}, K = {num_amostras})",
            xaxis_title="Médias Amostrais (x̄)",
            yaxis_title="Densidade de Probabilidade",
            template="plotly_white"
        )
        st.plotly_chart(fig_tcl, use_container_width=True)

        res1, res2, res3 = st.columns(3)
        res1.metric("Média da População (μ)", f"{pop_mu:.4f}")
        res2.metric("Média das Médias Amostrais (x̄̄)", f"{m_medias:.4f}")
        res3.metric("Erro Padrão Calculado vs Teórico", f"{dp_medias:.4f} / {erro_padrao_teorico:.4f}")

        st.info(
            f"💡 **Conclusão:** Mesmo com uma população de origem *{dist_origem}*, "
            f"a distribuição das médias amostrais aproxima-se de uma **Normal Simétrica** em forma de sino com $n={tamanho_amostra}$."
        )
