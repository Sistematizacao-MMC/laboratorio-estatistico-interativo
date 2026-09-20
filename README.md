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

O **Laboratório Estatístico Interativo** é uma aplicação interativa desenvolvida em Python para exploração de dados reais e simulações probabilísticas através de estatística descritiva, inferência, distribuições teóricas, métodos de Monte Carlo e regressão linear simples.

### 🌟 Diferencial Pedagógico
O núcleo estatístico foi **implementado de forma autoral ("na unha")** no módulo `src.core.pystatistics`, sem o uso de funções prontas de bibliotecas externas para a realização dos cálculos exibidos ao usuário. Bibliotecas consolidadas (*NumPy*, *SciPy*) foram empregadas exclusivamente na manipulação de dados e na **validação rigorosa dos cálculos via testes automatizados**.

---

## 📦 Base de Dados (Dataset)

* **Tema:** Cadastro Nacional da Pessoa Jurídica — CNPJ (Receita Federal do Brasil)
* **Registros Brutos:** Mais de 49 milhões de linhas consolidadas
* **Fonte Original:** [Dados Abertos do CNPJ - dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj)
* **Dataset Integrado:** A aplicação conta com um gerador embutido de dados de demonstração (1.000 empresas simuladas com métricas financeiras realistas e *outliers*), permitindo testar e explorar 100% dos módulos imediatamente sem a necessidade de baixar bases externas.

---

## 🎯 Módulos do Sistema

* **Módulo 0 — Carga e Pré-processamento:** Leitura de arquivos locais na pasta `data/`, upload de CSV personalizado ou uso do dataset de demonstração integrado.
* **Módulo 1 — Núcleo Estatístico Autoral (`src/core/pystatistics.py`):** Média, mediana, moda, amplitude, variância, desvio padrão, coeficiente de variação, separatrizes/quartis, IQR, detecção de outliers, covariância, correlação de Pearson, regressão linear MQO e PDFs de distribuições teóricas.
* **Módulo 2 — Estatística Descritiva Interativa:** Medidas de tendência central, dispersão, separatrizes, detecção de outliers (IQR de Tukey), histogramas, boxplots interativos (Plotly), tabelas de frequência e diagnósticos automáticos.
* **Módulo 3 — Probabilidade e Simulação (Monte Carlo):** Demonstração interativa da **Lei dos Grandes Números (LGN)** e do **Teorema Central do Limite (TCL)** com parâmetros dinâmicos (tamanho da amostra $n$ e iterações $K$).
* **Módulo 4 — Distribuições Teóricas:** Ajuste e sobreposição de curvas probabilísticas contínuas (Normal, Exponencial e Uniforme) sobre o histograma dos dados.
* **Módulo 5 — Correlação e Regressão Linear Simples:** Cálculo analítico por Mínimos Quadrados Ordinários (MQO), equações em LaTeX, plot da reta ajustada, coeficiente $R^2$, simulador de predição ($\hat{Y}$) e aviso metodológico de causalidade.
* **Módulo 6 — Relatório de Descobertas:** Síntese analítica das 3 principais conclusões extraídas dos dados reais.

---

## 🛠️ Tecnologias e Requisitos

* **Linguagem:** Python 3.10 ou superior
* **Interface Web:** Streamlit
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Plotly, Matplotlib, Seaborn
* **Testes Automatizados:** Pytest, SciPy

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/Sistematizacao-MMC/laboratorio-estatistico-interativo.git
cd laboratorio-estatistico-interativo
```

### 2. Criar e ativar o ambiente virtual

* **No Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
  *(Caso o PowerShell restrinja a execução de scripts, execute antes: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`)*

* **No Windows (Prompt de Comando / CMD):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```

* **No Linux / macOS:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

---

### 3. Instalar as dependências

Com o ambiente virtual ativado:
```bash
pip install -r requirements.txt
```

---

### 4. Executar a suíte de testes automatizados

Valida todas as fórmulas matemáticas autorais contra *NumPy* e *SciPy*:
```bash
pytest
```
*(Ou, alternativamente sem ativar o venv no Windows: `.\.venv\Scripts\pytest`)*

---

### 5. Iniciar a aplicação web (Streamlit)

```bash
streamlit run app.py
```
*(Ou, alternativamente sem ativar o venv no Windows: `.\.venv\Scripts\streamlit run app.py`)*

A aplicação será aberta automaticamente no seu navegador padrão no endereço:
```
http://localhost:8501
```

---

### 📥 (Opcional) Download do Dataset Real do CNPJ

Para baixar as tabelas completas de dados abertos do CNPJ diretamente das releases do projeto para a pasta `data/`:

```bash
python data/download_dataset.py
```
