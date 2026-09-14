import os
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

        
from src.core.pystatistics import media, desvio_padrao, pdf_normal, pdf_exponencial

# Configuração visual do Streamlit
st.set_page_config(
    page_title="Laboratório Estatístico Interativo",
    layout="wide",
    initial_sidebar_state="expanded"
)


def renderizar_modulo_4(df):
    st.title("📈 Módulo 4 — Ajuste de Distribuições Teóricas")
    st.write("Sobreposição de curvas probabilísticas teóricas ao histograma dos dados reais.")

    # Identifica colunas numéricas do dataset
    colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if not colunas_numericas:
        st.warning("Nenhuma coluna numérica foi identificada no arquivo selecionado.")
        return

    col1, col2 = st.columns(2)
    
    with col1:
        coluna_escolhida = st.selectbox("1. Selecione a Variável Numérica:", colunas_numericas)
    
    with col2:
        distribuicao = st.selectbox("2. Selecione a Distribuição Teórica:", ["Normal", "Exponencial"])

 
    dados = df[coluna_escolhida].dropna().tolist()

    if len(dados) == 0:
        st.warning(f"A variável '{coluna_escolhida}' não possui valores válidos.")
        return

    m = media(dados)
    dp = desvio_padrao(dados, amostral=True)

    st.info(f"**Parâmetros Estimados:** Média ($\mu$) = **{m:.2f}** | Desvio Padrão ($\sigma$) = **{dp:.2f}**")

 
    fig = go.Figure()

 
    fig.add_trace(go.Histogram(
        x=dados,
        histnorm='probability density',
        name='Dados Reais (Densidade)',
        opacity=0.6,
        marker_color='#1f77b4'
    ))

  
    eixo_x = np.linspace(min(dados), max(dados), 300)

    if distribuicao == "Normal":
        eixo_y = [pdf_normal(x, m, dp) for x in eixo_x]
    else: # Exponencial
        lambd = 1.0 / m if m > 0 else 0.0001
        eixo_y = [pdf_exponencial(x, lambd) for x in eixo_x]

    fig.add_trace(go.Scatter(
        x=eixo_x,
        y=eixo_y,
        mode='lines',
        name=f'Curva Teórica ({distribuicao})',
        line=dict(color='red', width=3)
    ))

    fig.update_layout(
        title=f"Ajuste da Distribuição {distribuicao} sobre '{coluna_escolhida}'",
        xaxis_title=str(coluna_escolhida),
        yaxis_title="Densidade de Probabilidade",
        template="plotly_white",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )

    st.plotly_chart(fig, use_container_width=True)

  
    st.subheader("💡 Análise do Ajuste Teórico")
    if distribuicao == "Normal":
        st.markdown(
            "A **Distribuição Normal** pressupõe simetria em formato de sino. "
            "Se o histograma real for assimétrico, o ajuste da curva Normal não será perfeito."
        )
    else:
        st.markdown(
            "A **Distribuição Exponencial** modela contagens ou tempo de espera, "
            "sendo ideal para dados concentrados perto do zero e com queda rápida."
        )



@st.cache_data
def carregar_csv_cnpj(nome_arquivo):
    caminho = os.path.join("data", nome_arquivo)
    
   
    try:
        return pd.read_csv(caminho, sep=";", encoding="latin1", nrows=10000, header=None)
    except Exception:
        return pd.read_csv(caminho, nrows=10000)



def main():
    st.sidebar.title("Navegação")
    
    pasta_data = "data"
    arquivos_csv = [f for f in os.listdir(pasta_data) if f.endswith(".csv")] if os.path.exists(pasta_data) else []

    if arquivos_csv:
      
        arquivo_selecionado = st.sidebar.selectbox("Selecione a Tabela do CNPJ:", arquivos_csv)
        df = carregar_csv_cnpj(arquivo_selecionado)
        
        renderizar_modulo_4(df)
    else:
        st.error("Nenhum arquivo .csv encontrado na pasta `data/`.")

if __name__ == "__main__":
    main()