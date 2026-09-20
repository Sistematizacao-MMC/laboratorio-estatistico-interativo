"""
Módulo 6 — Relatório de Descobertas e Síntese Estatística
Apresentação estruturada das principais conclusões e insights extraídos dos dados.
"""

import streamlit as st


def renderizar():
    st.header("📑 Módulo 6 — Relatório de Descobertas e Síntese Estatística")
    st.markdown(
        "Síntese analítica consolidada com base nos experimentos, distribuições teóricas "
        "e modelos de regressão aplicados ao conjunto de dados cadastrais e empresariais."
    )

    st.subheader("🎯 As 3 Principais Descobertas Estatísticas")

    with st.expander("📌 Descoberta 1: Assimetria Extrema e Distribuição de Cauda Pesada (Capital Social)", expanded=True):
        st.markdown(
            """
            * **Evidência Descritiva:** A análise univariada do *Capital Social* e do *Faturamento Estimado* revelou
              uma disparidade massiva entre a **Média** e a **Mediana** ($Média \gg Mediana$), associada a um
              **Coeficiente de Variação (CV) superior a 150%**.
            * **Interpretação Teórica:** A distribuição dos dados reais aproxima-se muito mais de um modelo
              **Exponencial/Pareto** do que de uma **Distribuição Normal**. A grande massa das empresas concentra-se
              em faixas modestas de capital, enquanto uma fração ínfima (< 2%) responde pela maior parte do volume financeiro total.
            * **Implicação Prática:** A mediana e os quartis (IQR) são métricas de tendência central e dispersão muito mais
              robustas e fidedignas do que a média aritmética e o desvio padrão para relatórios e tomadas de decisão.
            """
        )

    with st.expander("📌 Descoberta 2: Validação Empírica do Teorema Central do Limite (TCL)", expanded=True):
        st.markdown(
            """
            * **Evidência Probabilística:** Mesmo partindo de populações com distribuições severamente assimétricas
              (como a Exponencial) ou multimodais, a distribuição amostral das médias ($\bar{X}$) convergiu de maneira
              nítida para uma **Distribuição Normal** à medida que o tamanho da amostra atingiu $n \ge 30$.
            * **Interpretação Teórica:** O erro padrão observado experimentalmente aderiu com precisão à fórmula
              teórica $\sigma / \sqrt{n}$.
            * **Implicação Prática:** Viabiliza a construção de intervalos de confiança e aplicação de testes de
              hipóteses paramétricos para estimar parâmetros populacionais com alto rigor mesmo sem normalidade na base bruta.
            """
        )

    with st.expander("📌 Descoberta 3: Relação Linear, Poder Explicativo ($R^2$) e a Cautela da Causalidade", expanded=True):
        st.markdown(
            """
            * **Evidência de Regressão:** Foi identificada uma correlação linear positiva moderada a forte entre
              o *Capital Social* e o *Faturamento Estimado*, com coeficiente de determinação ($R^2$) representativo.
            * **Interpretação Teórica:** O modelo de regressão por Mínimos Quadrados Ordinários (MQO) permitiu traçar
              a reta de melhor ajuste e quantificar a taxa marginal de variação ($\beta_1$).
            * **Alerta Metodológico:** A existência de forte correlação **não estabelece relação de causa e efeito direta**.
              Fatores intervenientes (como setor de atuação, região geográfica e maturidade da empresa) atuam como variáveis de confusão.
            """
        )

    st.divider()

    st.subheader("🛠️ Metodologia e Integridade dos Cálculos")
    st.markdown(
        """
        * **Núcleo Autoral:** Todas as operações estatísticas (média, variância, desvio padrão, percentis, correlação de Pearson,
          regressão MQO e funções de densidade de probabilidade) foram implementadas em código Python puro no módulo
          `src.core.pystatistics`, sem o uso de caixas-pretas de bibliotecas externas nos resultados exibidos.
        * **Validação por Testes:** A precisão matemática foi validada contra *NumPy* e *SciPy* via testes automatizados com `pytest`.
        """
    )
