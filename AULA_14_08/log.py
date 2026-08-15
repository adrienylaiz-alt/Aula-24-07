import functools
from venv import logger
def log_execucao(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("início: %s", func._name_)
        resultado = func(*args, **kwargs)
        logger.info("fim: %s", func._name_)
        return resultado
    return wrapper           #closure: lembra func

@log_execucao
def processar_pedido(pedido: Pedido) -> Recibo:
    ...