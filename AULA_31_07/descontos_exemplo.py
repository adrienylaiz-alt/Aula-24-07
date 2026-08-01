def criar_desconto(percentual: float):
    """Fábrica de funções de desconto."""
    def aplicar(preco: float) ->float:
        # 'percentual' vem do encloning
        return preco * (1 - percentual)
    return aplicar
black_friday = criar_desconto(0.30)
cliente_vip = criar_desconto(0.15)

black_friday(200) # 140.0
cliente_vip(200) # 170.0