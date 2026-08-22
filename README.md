# 🧮 Laboratório Estatístico Interativo
> **Sistematização — Matemática e Estatística para Computação**  
> **Professor:** Romes

---

## 👥 Integrantes da Equipe

| Nome | GitHub |
| :--- | :--- |
| Rafael | [@Rafael](https://github.com/RafaelRLeite) |
| Matheus | [@Matheus](https://github.com/matheusbrito090108) |
| Fernando | [@Fernando](https://github.com/fernandoluca015) |
| Italo | [@Italo](https://github.com/Italo-917) |

---

## 📌 Sobre o Projeto

O **Laboratório Estatístico Interativo** é uma aplicação desenvolvida em Python voltada para a exploração de dados reais por meio de estatística descritiva, inferencial, distribuições de probabilidade, simulação e regressão linear.

O diferencial do projeto reside na implementação **autoral do núcleo estatístico** ("na unha"), sem o uso de funções prontas de cálculo de bibliotecas externas para a exibição dos resultados. As bibliotecas consolidadas (*NumPy*, *SciPy* e *statistics*) foram utilizadas exclusivamente para carga/manipulação de dados e validação dos cálculos via testes automatizados.

---

## 📦 Dataset Utilizado

* **Tema:** [Cadastro Nacional da Pessoa Jurídica - CNPJ]
* **Registros:** [49.872.124] linhas
* **Variáveis:** [X] numéricas e [Y] categóricas
* **Fonte Original:** [Link para a base de dados no dados.gov.br]([https://exemplo.com](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj))

---

## 📥 Download e preparação do dataset (dados abertos do CNPJ)

Os arquivos compactados são baixados diretamente das **Releases** do GitHub por meio de um script.

### 1. Instale o pacote `requests` para gerenciar o download em fluxo (*stream*):

```bash
pip install requests
```

### 2. Realize o download e a descompactação no diretório do projeto laboratorio-estatistico-interativo/data

```bash
python data/download_dataset.py
```

---

## 🎯 Módulos do Sistema

* **Módulo 0 — Carga e Pré-processamento:** Leitura, tratamento e limpeza do conjunto de dados selecionado.
* **Módulo 1 — Núcleo Estatístico Próprio (`minhastats`):** Biblioteca autoral contendo média, mediana, moda, amplitude, variâncias e desvios padrão (amostral/populacional), quartis/percentis, coeficiente de variação, covariância e correlação de Pearson.
* **Módulo 2 — Estatística Descritiva Interativa:** Tabelas de distribuição de frequência, medidas de dispersão/tendência central, gráficos (histograma, boxplot, barras) e detecção de outliers pelo método IQR com interpretação automática.
* **Módulo 3 — Probabilidade e Simulação (Monte Carlo):** Demonstração interativa da **Lei dos Grandes Números** e do **Teorema Central do Limite (TCL)** com parâmetros controlados pelo usuário.
* **Módulo 4 — Distribuições Teóricas:** Ajuste e sobreposição de curvas teóricas (Normal, Poisson, Exponencial, etc.) sobre o histograma dos dados.
* **Módulo 5 — Correlação e Regressão Linear Simples:** Cálculo analítico por Mínimos Quadrados Ordinários (MQO), plot da reta de ajuste, cálculo do $R^2$, predição interativa ($\hat{Y}$) e alerta metodológico de causalidade.
* **Módulo 6 — Relatório de Descobertas:** Análise fundamentada das 3 principais conclusões extraídas a partir dos dados.

---

## 🎬 Demonstração




---

## 🛠️ Tecnologias e Requisitos

* **Linguagem:** Python
* **Interface:** Streamlit (ou Dash / Gradio)
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn, Plotly

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/Sistematizacao-MMC/laboratorio-estatistico-interativo.git
cd laboratorio-estatistico-interativo
