def calcular_desconto (
        valor: float,
        percentual: float,
) -> float:
    """Aplica desconto sobre um valor

    Args: valor: preço base em R$, 
    percentual: fração (0.1 = 10%).
    Retorno:
    Preço final já com desconto """

    return round (valor * (1 - percentual), 2)