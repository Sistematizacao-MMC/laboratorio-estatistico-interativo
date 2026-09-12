import pytest

from src.essencial.pystatistics import (
    correlacao_pearson,
    regrecao_linear_simples
)


def test_correlacao_pearson():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    r = correlacao_pearson(x, y)

    assert r == pytest.approx(1.0)


def test_regressao_linear_simples():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    b0, b1, r2 = regrecao_linear_simples(x, y)

    assert b0 == pytest.approx(0.0)
    assert b1 == pytest.approx(2.0)
    assert r2 == pytest.approx(1.0)


def test_correlacao_negativa():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]

    r = correlacao_pearson(x, y)

    assert r == pytest.approx(-1.0)
