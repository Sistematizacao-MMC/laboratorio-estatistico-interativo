import math
import numpy as np

from src.core.pystatistics import (
    media,
    mediana,
    variancia,
    desvio_padrao,
    correlacao_pearson
)


dados = [10, 12, 23, 23, 16, 23, 21, 16]


def test_media():
    assert math.isclose(
        media(dados),
        np.mean(dados),
        rel_tol=1e-5
    )


def test_mediana():
    assert math.isclose(
        mediana(dados),
        np.median(dados),
        rel_tol=1e-5
    )


def test_variancia():
    assert math.isclose(
        variancia(dados, amostral=True),
        np.var(dados, ddof=1),
        rel_tol=1e-5
    )


def test_desvio_padrao():
    assert math.isclose(
        desvio_padrao(dados, amostral=True),
        np.std(dados, ddof=1),
        rel_tol=1e-5
    )


def test_correlacao():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    r_proprio = correlacao_pearson(x, y)
    r_np = np.corrcoef(x, y)[0, 1]

    assert math.isclose(
        r_proprio,
        r_np,
        rel_tol=1e-5
    )
