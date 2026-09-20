"""
Módulo core: Contém o núcleo de cálculos estatísticos e probabilísticos autorais.
"""

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
    detectar_outliers_iqr,
    covariancia,
    covariavel,
    correlacao_pearson,
    regressao_linear_simples,
    regrecao_linear_simples,
    pdf_normal,
    pdf_exponencial,
    pdf_poisson,
    pdf_uniforme,
)

__all__ = [
    "media",
    "mediana",
    "moda",
    "amplitude",
    "variancia",
    "desvio_padrao",
    "coeficiente_variacao",
    "percentil",
    "quartis",
    "detectar_outliers_iqr",
    "covariancia",
    "covariavel",
    "correlacao_pearson",
    "regressao_linear_simples",
    "regrecao_linear_simples",
    "pdf_normal",
    "pdf_exponencial",
    "pdf_poisson",
    "pdf_uniforme",
]
