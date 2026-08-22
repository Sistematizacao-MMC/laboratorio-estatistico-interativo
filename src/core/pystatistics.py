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
    diferencas_quadradas = [(x - m) ** 2 for x in dados]
    divisor = (len(dados) - 1) if amostral else len(dados)
    return sum(diferencas_quadradas) / divisor

def desvio_padrao(dados, amostral=True):
    return math.sqrt(variancia(dados, amostral))

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
    mx, my = media(x), media(y)
    n = len(x)
    divisor = (n - 1) if amostral else n
    return sum((x[i] - mx) * (y[i] - my) for i in range(n)) / divisor

def correlacao_pearson(x, y):
    cov = covariavel(x, y)
    sx = desvio_padrao(x)
    sy = desvio_padrao(y)
    return cov / (sx * sy)

def regrecao_linear_simples(x, y):
    mx, my = media(x), media(y)
    b1 = covariavel(x, y, amostral=True) / variancia(x, amostral=True)
    b0 = my - b1 * mx

    r = correlacao_pearson(x, y)
    r2 = r ** 2
    return b0, b1, r2