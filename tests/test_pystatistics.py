import math
import numpy as np
from scipy import stats


from src.core.pystatistics import (
    media, 
    desvio_padrao, 
    correlacao_pearson, 
    pdf_normal
)

dados = [10, 12, 23, 23, 16, 23, 21, 16]

def test_media():
    assert math.isclose(media(dados), np.mean(dados), rel_tol=1e-5)

def test_desvio_padrao():
    assert math.isclose(desvio_padrao(dados, amostral=True), np.std(dados, ddof=1), rel_tol=1e-5)

def test_correlacao():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    r_proprio = correlacao_pearson(x, y)
    r_np = np.corrcoef(x, y)[0, 1]
    assert math.isclose(r_proprio, r_np, rel_tol=1e-5)


def test_pdf_normal():
    x_teste = 10.0
    media_teste = 12.0
    desvio_teste = 2.5
    
    val_nosso = pdf_normal(x_teste, media_teste, desvio_teste)
    val_oficial = stats.norm.pdf(x_teste, loc=media_teste, scale=desvio_teste)
    
    assert math.isclose(val_nosso, val_oficial, rel_tol=1e-5)