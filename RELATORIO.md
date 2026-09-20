# 📑 Relatório de Descobertas e Síntese Estatística

> **Projeto:** Laboratório Estatístico Interativo  
> **Disciplina:** Matemática e Estatística para Computação  
> **Professor:** Romes  
> **Integrantes:** Rafael, Matheus, Fernando, Italo  

---

## 1. 🎯 Introdução e Contexto

Este relatório documenta as principais descobertas obtidas a partir do desenvolvimento e experimentação com o **Laboratório Estatístico Interativo**. O projeto foi concebido para investigar propriedades teóricas e empíricas da estatística descritiva, probabilidade, distribuições teóricas e modelos lineares aplicados a dados cadastrais e econômicos empresariais (baseados nos Dados Abertos do CNPJ da Receita Federal do Brasil).

Todos os cálculos centrais (média, mediana, moda, variância, desvio padrão, separatrizes, IQR, correlação de Pearson, regressão linear MQO e PDFs de distribuições) foram implementados de forma **autoral** no módulo `src.core.pystatistics` e validados via testes automatizados comparativos com *NumPy* e *SciPy*.

---

## 2. 📊 As 3 Principais Descobertas Estatísticas

### 📌 Descoberta 1: Assimetria Extrema e Distribuição de Cauda Pesada nas Variáveis Financeiras
* **Evidência Descritiva:** Na análise univariada das variáveis de *Capital Social* e *Faturamento Estimado*, observou-se uma discrepância marcante entre a média aritmética e a mediana ($\text{Média} \gg \text{Mediana}$), acompanhada de um **Coeficiente de Variação (CV) frequentemente superior a 150%**.
* **Interpretação Teórica:** Variáveis econômicas reais no contexto empresarial não seguem uma curva simétrica gaussiana (Normal). A grande maioria dos registros concentra-se em valores de pequeno e médio porte, enquanto uma fração ínfima (menos de 2% dos registros, identificados como *outliers* pelas cercas de Tukey $Q_3 + 1.5 \times \text{IQR}$) concentra volumes financeiros massivos. O ajuste teórico da **Distribuição Exponencial/Pareto** demonstrou aderência muito superior ao modelo Normal.
* **Impacto Metodológico:** A média aritmética é altamente vulnerável a valores extremos, tornando a **Mediana** e o **Intervalo Interquartílico (IQR)** medidas de tendência central e dispersão muito mais robustas e confiáveis para caracterizar a realidade da maior parte das empresas.

---

### 📌 Descoberta 2: Validação Experimental da Lei dos Grandes Números (LGN) e do Teorema Central do Limite (TCL)
* **Evidência Probabilística:** 
  1. No módulo de simulação de Monte Carlo, observou-se a rápida convergência da média amostral $\bar{X}_n$ em direção ao valor esperado $E[X] = \mu$ à medida que o número de ensaios $n$ superou 500 iterações (LGN).
  2. Mesmo ao extrair amostras de populações **severamente assimétricas** (Exponencial) ou **bimodais**, a distribuição de frequências das médias amostrais $(\bar{X})$ assumiu formato campanular simétrico e contínuo (Normal) para amostras de tamanho $n \ge 30$ (TCL).
* **Interpretação Teórica:** O desvio padrão amostral das médias convergiu rigorosamente para o **Erro Padrão Teórico** dado por:
  $$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$
* **Impacto Metodológico:** O Teorema Central do Limite legitima a inferência estatística, permitindo o cálculo de intervalos de confiança e testes de hipóteses paramétricos mesmo quando a distribuição dos dados brutos populacionais é desconhecida ou não-normal.

---

### 📌 Descoberta 3: Relação Linear por MQO, Poder Explicativo ($R^2$) e o Cuidado com a Causalidade
* **Evidência da Regressão:** O modelo bivariado entre *Capital Social* ($X$) e *Faturamento Estimado* ($Y$) ajustado por Mínimos Quadrados Ordinários (MQO) apresentou coeficiente de correlação de Pearson positivo e estatisticamente relevante ($r > 0.60$), gerando uma reta da forma $\hat{Y} = \beta_0 + \beta_1 X$.
* **Poder Explicativo ($R^2$):** O coeficiente de determinação obtido quantifica qual parcela da dispersão do faturamento pode ser explicada unicamente pelo capital social investido.
* **Alerta Crítico de Causalidade:** É fundamental destacar o princípio estatístico de que **correlação não implica causalidade**. Um valor elevado de $r$ ou $R^2$ reflete apenas uma associação linear simultânea entre as variáveis. Fatores ocultos (variáveis de confusão, tais como setor econômico, localização geográfica e tempo de mercado) exercem influência crucial na determinação do faturamento real.

---

## 3. 🛠️ Arquitetura e Estrutura dos Módulos

| Módulo | Função no Sistema |
| :--- | :--- |
| **`src/core/pystatistics.py`** | Núcleo autoral contendo todas as fórmulas de tendência central, dispersão, separatrizes, Pearson, MQO e distribuições teóricas. |
| **`src/modules/modulo0_dados.py`** | Carga de arquivos CSV locais (`data/`), upload customizado ou geração de dataset sintético representativo com métricas de completude. |
| **`src/modules/modulo2_descritiva.py`** | Painel interativo com média, mediana, moda, variância, desvio padrão, CV, quartis, detecção de outliers (IQR) e gráficos interativos (Plotly). |
| **`src/modules/modulo3_simulacao.py`** | Simulações de Monte Carlo demonstrando a convergência da LGN e a normalização assintótica do TCL com parâmetros interativos. |
| **`src/modules/modulo4_distribuicoes.py`** | Ajuste e sobreposição de curvas de densidade teóricas (Normal, Exponencial e Uniforme) sobre os histogramas das variáveis. |
| **`src/modules/modulo5_regressao.py`** | Correlação de Pearson, reta de ajuste MQO, equações em LaTeX, coeficiente $R^2$, simulador de predição interativa ($\hat{Y}$) e alerta de causalidade. |
| **`src/modules/modulo6_relatorio.py`** | Visualização integrada do presente relatório analítico diretamente na interface do usuário. |

---

## 4. ✅ Conclusão

O **Laboratório Estatístico Interativo** cumpre integralmente os requisitos pedagógicos e técnicos da disciplina, fornecendo um ambiente modular, escalável, visualmente rico e matematicamente transparente para o ensino e prática da Estatística Computacional.
