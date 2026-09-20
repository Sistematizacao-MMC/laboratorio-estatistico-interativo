import math
import numpy as np
import pytest
from scipy import stats

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
    correlacao_pearson,
    regressao_linear_simples,
    pdf_normal,
    pdf_exponencial,
    pdf_poisson,
    pdf_uniforme
)

dados = [10.0, 12.0, 23.0, 23.0, 16.0, 23.0, 21.0, 16.0]


def test_media():
    assert math.isclose(media(dados), np.mean(dados), rel_tol=1e-5)


def test_mediana():
    assert math.isclose(mediana(dados), np.median(dados), rel_tol=1e-5)


def test_moda():
    assert moda(dados) == [23.0]
    # Teste amodal
    assert moda([1.0, 2.0, 3.0, 4.0]) == []


def test_amplitude():
    assert math.isclose(amplitude(dados), np.ptp(dados), rel_tol=1e-5)


def test_variancia():
    assert math.isclose(variancia(dados, amostral=True), np.var(dados, ddof=1), rel_tol=1e-5)
    assert math.isclose(variancia(dados, amostral=False), np.var(dados, ddof=0), rel_tol=1e-5)


def test_desvio_padrao():
    assert math.isclose(desvio_padrao(dados, amostral=True), np.std(dados, ddof=1), rel_tol=1e-5)
    assert math.isclose(desvio_padrao(dados, amostral=False), np.std(dados, ddof=0), rel_tol=1e-5)


def test_coeficiente_variacao():
    cv_esperado = (np.std(dados, ddof=1) / np.mean(dados)) * 100.0
    assert math.isclose(coeficiente_variacao(dados, amostral=True), cv_esperado, rel_tol=1e-5)


def test_percentil():
    for p in [0, 25, 50, 75, 100]:
        val_autoral = percentil(dados, p)
        val_np = np.percentile(dados, p)
        assert math.isclose(val_autoral, val_np, rel_tol=1e-5)


def test_quartis_e_outliers():
    q1, q2, q3, iqr = quartis(dados)
    assert math.isclose(q1, np.percentile(dados, 25), rel_tol=1e-5)
    assert math.isclose(q2, np.percentile(dados, 50), rel_tol=1e-5)
    assert math.isclose(q3, np.percentile(dados, 75), rel_tol=1e-5)
    assert math.isclose(iqr, q3 - q1, rel_tol=1e-5)

    dados_com_outlier = dados + [1000.0]
    outliers, lim_inf, lim_sup = detectar_outliers_iqr(dados_com_outlier)
    assert 1000.0 in outliers


def test_covariancia_e_correlacao():
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.0, 4.0, 5.0, 4.0, 5.0]

    cov_autoral = covariancia(x, y, amostral=True)
    cov_np = np.cov(x, y, ddof=1)[0, 1]
    assert math.isclose(cov_autoral, cov_np, rel_tol=1e-5)

    r_proprio = correlacao_pearson(x, y)
    r_np = np.corrcoef(x, y)[0, 1]
    assert math.isclose(r_proprio, r_np, rel_tol=1e-5)


def test_regressao_linear_simples():
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [3.0, 5.0, 7.0, 9.0, 11.0]

    b0, b1, r2 = regressao_linear_simples(x, y)
    assert math.isclose(b0, 1.0, rel_tol=1e-5)
    assert math.isclose(b1, 2.0, rel_tol=1e-5)
    assert math.isclose(r2, 1.0, rel_tol=1e-5)


def test_pdf_normal():
    x_teste = 10.0
    media_teste = 12.0
    desvio_teste = 2.5

    val_nosso = pdf_normal(x_teste, media_teste, desvio_teste)
    val_oficial = stats.norm.pdf(x_teste, loc=media_teste, scale=desvio_teste)
    assert math.isclose(val_nosso, val_oficial, rel_tol=1e-5)


def test_pdf_exponencial():
    x_teste = 3.0
    lambd_teste = 0.5

    val_nosso = pdf_exponencial(x_teste, lambd_teste)
    val_oficial = stats.expon.pdf(x_teste, scale=1.0 / lambd_teste)
    assert math.isclose(val_nosso, val_oficial, rel_tol=1e-5)


def test_pdf_poisson():
    k = 3
    lambd = 2.0
    val_nosso = pdf_poisson(k, lambd)
    val_oficial = stats.poisson.pmf(k, mu=lambd)
    assert math.isclose(val_nosso, val_oficial, rel_tol=1e-5)


def test_pdf_uniforme():
    val_nosso = pdf_uniforme(5.0, 0.0, 10.0)
    assert math.isclose(val_nosso, 0.1, rel_tol=1e-5)
    assert pdf_uniforme(15.0, 0.0, 10.0) == 0.0
