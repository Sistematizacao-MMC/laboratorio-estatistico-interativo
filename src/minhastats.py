
import math


def media(dados):
    """Calcula a média aritmética."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")
    return sum(dados) / len(dados)


def mediana(dados):
    """Calcula a mediana."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")

    valores = sorted(dados)
    n = len(valores)
    meio = n // 2

    if n % 2 == 0:
        return (valores[meio - 1] + valores[meio]) / 2

    return valores[meio]


def variancia(dados, amostral=False):
    """Calcula a variância populacional ou amostral."""
    if not dados:
        raise ValueError("A lista de dados não pode estar vazia.")

    if amostral and len(dados) < 2:
        raise ValueError(
            "São necessários pelo menos dois valores para a variância amostral."
        )

    media_valor = media(dados)
    soma_quadrados = sum((x - media_valor) ** 2 for x in dados)

    divisor = len(dados) - 1 if amostral else len(dados)

    return soma_quadrados / divisor


def desvio_padrao(dados, amostral=False):
    """Calcula o desvio padrão populacional ou amostral."""
    return math.sqrt(variancia(dados, amostral=amostral))


def correlacao_pearson(x, y):
    """Calcula o coeficiente de correlação de Pearson."""
    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho.")

    if len(x) < 2:
        raise ValueError("São necessários pelo menos dois pares de dados.")

    media_x = media(x)
    media_y = media(y)

    numerador = sum(
        (xi - media_x) * (yi - media_y)
        for xi, yi in zip(x, y)
    )

    soma_x = sum((xi - media_x) ** 2 for xi in x)
    soma_y = sum((yi - media_y) ** 2 for yi in y)

    denominador = math.sqrt(soma_x * soma_y)

    if denominador == 0:
        return float("nan")

    return numerador / denominador
