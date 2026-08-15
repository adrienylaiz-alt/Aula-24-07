def processar_pagamento(pedido: Pedido) -> Recibo:
    try:
        recibo = gateway.cobrar(pedido)

    except CartaoRecusadoError:
        # erro ESPERADO: regra de negócio
        raise

    except TimeoutError as exc:
        # erro INESPERADO: infraestrutura
        logger.error("gateway fora: %s", exc)
        raise

    else:
        registrar_sucesso(recibo)  # só sem erro
        return recibo

    finally:
        fechar_conexao()  # sempre roda