"""
Núcleo Estatístico Autoral (pystatistics)
Implementação de funções estatísticas e probabilísticas sem dependência
de bibliotecas estatísticas prontas para os cálculos.
"""

import math
from collections import Counter
from typing import List, Tuple, Union


def media(dados: List[Union[int, float]]) -> float:
    """Calcula a média aritmética dos dados."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    return sum(dados) / len(dados)


def mediana(dados: List[Union[int, float]]) -> float:
    """Calcula a mediana dos dados."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    s = sorted(dados)
    n = len(s)
    meio = n // 2

    if n % 2 == 0:
        return (s[meio - 1] + s[meio]) / 2.0
    return float(s[meio])


def moda(dados: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calcula a(s) moda(s) dos dados.
    Retorna uma lista com o(s) valor(es) mais frequente(s).
    Se todos os valores tiverem a mesma frequência, retorna lista vazia (amodal).
    """
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    contagem = Counter(dados)
    max_freq = max(contagem.values())

    if max_freq == 1 and len(dados) > 1:
        return []

    modas = [val for val, freq in contagem.items() if freq == max_freq]
    if len(modas) == len(contagem) and len(modas) > 1:
        return []
    return sorted(modas)


def amplitude(dados: List[Union[int, float]]) -> float:
    """Calcula a amplitude total dos dados (máximo - mínimo)."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    return float(max(dados) - min(dados))


def variancia(dados: List[Union[int, float]], amostral: bool = True) -> float:
    """Calcula a variância amostral (divisor n-1) ou populacional (divisor n)."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    if amostral and len(dados) < 2:
        raise ValueError("São necessários pelo menos dois valores para a variância amostral.")

    m = media(dados)
    diferencas_quadradas = [(x - m) ** 2 for x in dados]
    divisor = len(dados) - 1 if amostral else len(dados)
    return sum(diferencas_quadradas) / divisor


def desvio_padrao(dados: List[Union[int, float]], amostral: bool = True) -> float:
    """Calcula o desvio padrão amostral ou populacional."""
    return math.sqrt(variancia(dados, amostral=amostral))


def coeficiente_variacao(dados: List[Union[int, float]], amostral: bool = True) -> float:
    """
    Calcula o coeficiente de variação percentual: (desvio_padrao / media) * 100.
    """
    m = media(dados)
    if m == 0:
        raise ValueError("O coeficiente de variação não pode ser calculado para média zero.")
    dp = desvio_padrao(dados, amostral=amostral)
    return (dp / abs(m)) * 100.0


def percentil(dados: List[Union[int, float]], p: float) -> float:
    """
    Calcula o percentil 'p' (0 a 100) utilizando interpolação linear padrão.
    """
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    if p < 0 or p > 100:
        raise ValueError("O percentil deve estar entre 0 e 100.")

    s = sorted(dados)
    k = (len(s) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return float(s[int(k)])

    d0 = s[int(f)] * (c - k)
    d1 = s[int(c)] * (k - f)
    return float(d0 + d1)


def quartis(dados: List[Union[int, float]]) -> Tuple[float, float, float, float]:
    """
    Calcula os três quartis e a distância interquartílica (IQR).
    Retorna: (Q1, Q2, Q3, IQR)
    """
    q1 = percentil(dados, 25.0)
    q2 = percentil(dados, 50.0)
    q3 = percentil(dados, 75.0)
    iqr = q3 - q1
    return q1, q2, q3, iqr


def detectar_outliers_iqr(dados: List[Union[int, float]]) -> Tuple[List[Union[int, float]], float, float]:
    """
    Detecta outliers pelo método da Amplitude Interquartílica (IQR).
    Retorna: (lista_outliers, limite_inferior, limite_superior)
    """
    q1, _, q3, iqr = quartis(dados)
    limite_inf = q1 - 1.5 * iqr
    limite_sup = q3 + 1.5 * iqr
    outliers = [x for x in dados if x < limite_inf or x > limite_sup]
    return outliers, limite_inf, limite_sup


def covariancia(x: List[Union[int, float]], y: List[Union[int, float]], amostral: bool = True) -> float:
    """Calcula a covariância entre duas séries x e y."""
    if len(x) != len(y):
        raise ValueError("As listas x e y devem possuir o mesmo tamanho.")
    if len(x) < 2:
        raise ValueError("São necessários pelo menos dois valores para cálculo de covariância.")

    mx = media(x)
    my = media(y)
    n = len(x)
    divisor = n - 1 if amostral else n

    return sum((x[i] - mx) * (y[i] - my) for i in range(n)) / divisor


# Alias retrocompatível
covariavel = covariancia


def correlacao_pearson(x: List[Union[int, float]], y: List[Union[int, float]]) -> float:
    """Calcula o coeficiente de correlação de Pearson entre x e y."""
    if len(x) != len(y):
        raise ValueError("As listas x e y devem possuir o mesmo tamanho.")
    if len(x) < 2:
        raise ValueError("São necessários pelo menos dois valores para correlação.")

    sx = desvio_padrao(x, amostral=True)
    sy = desvio_padrao(y, amostral=True)

    if sx == 0 or sy == 0:
        raise ValueError("A correlação não pode ser calculada quando uma das variáveis possui variância zero.")

    cov = covariancia(x, y, amostral=True)
    r = cov / (sx * sy)
    # Limita numericamente entre -1.0 e 1.0 para mitigar precisão de ponto flutuante
    return max(-1.0, min(1.0, r))


def regressao_linear_simples(
    x: List[Union[int, float]], y: List[Union[int, float]]
) -> Tuple[float, float, float]:
    """
    Regressão linear simples pelo método dos Mínimos Quadrados Ordinários (MQO).
    Modelo: Y_hat = beta_0 + beta_1 * X

    Retorna:
        beta_0 -> Intercepto
        beta_1 -> Coeficiente angular
        r2     -> Coeficiente de determinação (R²)
    """
    if len(x) != len(y):
        raise ValueError("As listas x e y devem possuir o mesmo tamanho.")
    if len(x) < 2:
        raise ValueError("São necessários pelo menos dois valores para regressão.")

    mx = media(x)
    my = media(y)

    numerador = sum((x[i] - mx) * (y[i] - my) for i in range(len(x)))
    denominador = sum((x[i] - mx) ** 2 for i in range(len(x)))

    if denominador == 0:
        raise ValueError("A regressão não pode ser calculada quando X possui variância zero.")

    beta_1 = numerador / denominador
    beta_0 = my - beta_1 * mx
    r = correlacao_pearson(x, y)
    r2 = r ** 2

    return beta_0, beta_1, r2


# Alias retrocompatível
regrecao_linear_simples = regressao_linear_simples


# ==============================================================================
# Distribuições Teóricas
# ==============================================================================

def pdf_normal(x: float, mu: float, sigma: float) -> float:
    """Função densidade de probabilidade (PDF) da Distribuição Normal."""
    if sigma <= 0:
        return 0.0
    coef = 1.0 / (sigma * math.sqrt(2 * math.pi))
    expoente = -0.5 * ((x - mu) / sigma) ** 2
    return coef * math.exp(expoente)


def pdf_exponencial(x: float, lambd: float) -> float:
    """Função densidade de probabilidade (PDF) da Distribuição Exponencial."""
    if x < 0 or lambd <= 0:
        return 0.0
    return lambd * math.exp(-lambd * x)


def pdf_poisson(k: int, lambd: float) -> float:
    """Função de probabilidade de massa (PMF) da Distribuição de Poisson."""
    if k < 0 or lambd <= 0:
        return 0.0
    return (math.exp(-lambd) * (lambd ** k)) / math.factorial(k)


def pdf_uniforme(x: float, a: float, b: float) -> float:
    """Função densidade de probabilidade (PDF) da Distribuição Uniforme Contínua [a, b]."""
    if b <= a:
        return 0.0
    if a <= x <= b:
        return 1.0 / (b - a)
    return 0.0
