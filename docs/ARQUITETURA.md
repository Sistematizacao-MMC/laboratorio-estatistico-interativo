# 🏛️ Arquitetura do Projeto

O **Laboratório Estatístico Interativo** é estruturado em camadas desacopladas seguindo os padrões de boas práticas em Python:

```
laboratorio-estatistico-interativo/
├── app.py                          # Ponto de entrada (Interface Streamlit principal)
├── conftest.py                     # Configuração global de importações de teste
├── pytest.ini                      # Configuração do executor pytest
├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação geral e guia de início
├── RELATORIO.md                    # Relatório acadêmico de descobertas estatísticas
│
├── data/                           # Gestão de dados
│   ├── cnpj-metadados.pdf          # Metadados e dicionário das tabelas do CNPJ
│   └── download_dataset.py         # Script autônomo de download e descompactação
│
├── docs/                           # Documentação arquitetural
│   └── ARQUITETURA.md
│
├── src/                            # Código-fonte principal
│   ├── __init__.py
│   ├── core/                       # Núcleo Estatístico Autoral ("na unha")
│   │   ├── __init__.py
│   │   └── pystatistics.py         # Implementação de medidas, separatrizes e distribuições
│   └── modules/                    # Camada de Apresentação e Visualização (Streamlit)
│       ├── __init__.py
│       ├── modulo0_dados.py        # Carga, upload e amostragem
│       ├── modulo2_descritiva.py   # Estatística descritiva e detecção de outliers (IQR)
│       ├── modulo3_simulacao.py    # Simulações de Monte Carlo (LGN e TCL)
│       ├── modulo4_distribuicoes.py# Ajuste de curvas teóricas (Normal, Exponencial, Uniforme)
│       ├── modulo5_regressao.py    # Correlação de Pearson e Regressão Linear Simples MQO
│       └── modulo6_relatorio.py    # Síntese e visualização das conclusões
│
└── tests/                          # Suíte de Testes Automatizados
    ├── __init__.py
    ├── test_modulo5.py             # Testes de regressão e correlação
    └── test_pystatistics.py        # Testes comparativos de validação (autoral vs NumPy/SciPy)
```

---

## 📐 Princípios de Design Adotados
1. **Separação de Responsabilidades (SoC):** O núcleo de cálculo (`src/core`) é 100% agnóstico de interface gráfica, permitindo que seja reutilizado em CLI, Jupyter Notebooks ou APIs.
2. **Modularidade:** Cada aba ou módulo do sistema Streamlit reside em um arquivo isolado em `src/modules/`.
3. **Transparência e Validação:** Todos os cálculos estatísticos são implementados de forma autoral e validados sistematicamente contra bibliotecas consolidadas da indústria (*NumPy* e *SciPy*) via `pytest`.
