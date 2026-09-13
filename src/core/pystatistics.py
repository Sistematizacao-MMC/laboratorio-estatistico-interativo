import math


def media(dados):
    return sum(dados) / len(dados)


def mediana(dados):
    s = sorted(dados)
    n = len(s)
    meio = n // 2

    if n % 2 == 0:
        return (s[meio - 1] + s[meio]) / 2.0

    return float(s[meio])


def variancia(dados, amostral=True):
    m = media(dados)

    diferencas_quadradas = [
        (x - m) ** 2
        for x in dados
    ]

    divisor = (
        len(dados) - 1
        if amostral
        else len(dados)
    )

    return sum(diferencas_quadradas) / divisor


def desvio_padrao(dados, amostral=True):
    return math.sqrt(
        variancia(dados, amostral)
    )


def percentil(dados, p):
    s = sorted(dados)

    k = (len(s) - 1) * (p / 100.0)

    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return float(s[int(k)])

    d0 = s[int(f)] * (c - k)
    d1 = s[int(c)] * (k - f)

    return d0 + d1


def covariavel(x, y, amostral=True):
    if len(x) != len(y):
        raise ValueError(
            "As listas x e y devem possuir o mesmo tamanho."
        )

    if len(x) < 2:
        raise ValueError(
            "São necessários pelo menos dois valores."
        )

    mx = media(x)
    my = media(y)

    n = len(x)

    divisor = (
        n - 1
        if amostral
        else n
    )

    return sum(
        (x[i] - mx) * (y[i] - my)
        for i in range(n)
    ) / divisor


def correlacao_pearson(x, y):
    if len(x) != len(y):
        raise ValueError(
            "As listas x e y devem possuir o mesmo tamanho."
        )

    if len(x) < 2:
        raise ValueError(
            "São necessários pelo menos dois valores."
        )

    sx = desvio_padrao(x)
    sy = desvio_padrao(y)

    if sx == 0 or sy == 0:
        raise ValueError(
            "A correlação não pode ser calculada quando "
            "uma das variáveis possui variância zero."
        )

    cov = covariavel(
        x,
        y,
        amostral=True
    )

    return cov / (sx * sy)


def regrecao_linear_simples(x, y):
    """
    Regressão linear simples pelo método
    dos Mínimos Quadrados Ordinários (MQO).

    Modelo:

        Y_hat = beta_0 + beta_1 * X

    Retorna:

        beta_0 -> intercepto
        beta_1 -> coeficiente angular
        r2     -> coeficiente de determinação
    """

    if len(x) != len(y):
        raise ValueError(
            "As listas x e y devem possuir o mesmo tamanho."
        )

    if len(x) < 2:
        raise ValueError(
            "São necessários pelo menos dois valores."
        )

    mx = media(x)
    my = media(y)

    numerador = sum(
        (x[i] - mx) * (y[i] - my)
        for i in range(len(x))
    )

    denominador = sum(
        (x[i] - mx) ** 2
        for i in range(len(x))
    )

    if denominador == 0:
        raise ValueError(
            "A regressão não pode ser calculada quando "
            "X possui variância zero."
        )

    # Coeficiente angular pelo MQO
    beta_1 = numerador / denominador

    # Intercepto
    beta_0 = my - beta_1 * mx

    # Correlação e R²
    r = correlacao_pearson(x, y)

    r2 = r ** 2

    return beta_0, beta_1, r2
