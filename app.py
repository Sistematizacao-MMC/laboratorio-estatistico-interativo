"""
Laboratório Estatístico Interativo
Aplicação Principal em Streamlit integrando todos os módulos do projeto.
"""

import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Laboratório Estatístico Interativo",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializa sessão para dados compartilhados
if "df" not in st.session_state:
    st.session_state["df"] = None

# Importação dos módulos da aplicação
from src.modules import (
    modulo0_dados,
    modulo2_descritiva,
    modulo3_simulacao,
    modulo4_distribuicoes,
    modulo5_regressao,
    modulo6_relatorio,
)


def main():
    st.sidebar.title("🧮 Laboratório Estatístico")
    st.sidebar.caption("Matemática e Estatística para Computação")
    st.sidebar.markdown("---")

    opcoes_menu = [
        "Módulo 0 — Carga de Dados",
        "Módulo 2 — Estatística Descritiva",
        "Módulo 3 — Probabilidade & Monte Carlo",
        "Módulo 4 — Distribuições Teóricas",
        "Módulo 5 — Correlação & Regressão",
        "Módulo 6 — Relatório de Descobertas"
    ]

    modulo_selecionado = st.sidebar.radio(
        "Navegação pelos Módulos:",
        opcoes_menu,
        index=0
    )

    st.sidebar.markdown("---")
    st.sidebar.info(
        "**Equipe:**\n"
        "- Rafael\n"
        "- Matheus\n"
        "- Fernando\n"
        "- Italo\n\n"
        "**Orientação:** Prof. Romes"
    )

    # Roteamento dos módulos
    if modulo_selecionado == "Módulo 0 — Carga de Dados":
        modulo0_dados.renderizar()

    elif modulo_selecionado == "Módulo 2 — Estatística Descritiva":
        if st.session_state["df"] is None:
            st.session_state["df"] = modulo0_dados.gerar_dados_demonstracao()
        modulo2_descritiva.renderizar(st.session_state["df"])

    elif modulo_selecionado == "Módulo 3 — Probabilidade & Monte Carlo":
        modulo3_simulacao.renderizar()

    elif modulo_selecionado == "Módulo 4 — Distribuições Teóricas":
        if st.session_state["df"] is None:
            st.session_state["df"] = modulo0_dados.gerar_dados_demonstracao()
        modulo4_distribuicoes.renderizar(st.session_state["df"])

    elif modulo_selecionado == "Módulo 5 — Correlação & Regressão":
        if st.session_state["df"] is None:
            st.session_state["df"] = modulo0_dados.gerar_dados_demonstracao()
        modulo5_regressao.renderizar(st.session_state["df"])

    elif modulo_selecionado == "Módulo 6 — Relatório de Descobertas":
        modulo6_relatorio.renderizar()


if __name__ == "__main__":
    main()
