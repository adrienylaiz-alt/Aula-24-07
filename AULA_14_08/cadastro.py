import re
"""Função responsavel por normalizar o CPF e retorno o CPF
 limpo de caracteres que não são digitos, utilizando regex"""


def normalizar_cpf(cpf: str)  -> str:
    if not cpf ==str:
        tipo = type(cpf)
        raise TypeError("Erro de tipo: O tipo informado de CPF não corresponde com o esperado pela função. Tipo esperado")
    return re.sub(r"\D", "", cpf)

"""Essa função verifica primeiro se o CPF possui 11 caracteres. Depois, 
verifica se todos esses caracteres são números. Se as duas
verificações estiverem corretas, ela retorna se estão ou não corretas."""
def validar_cpf(cpf: str) -> bool:
    if not cpf ==str:
        tipo = type(cpf)
        raise TypeError("Erro de tipo: O tipo informado de CPF não corresponde com o esperado pela função. Tipo esperado")
    return len(cpf) == 11 and cpf.isdigit()

"""Essa função recebe o CPF do cliente, primeiro normaliza o CPF para deixar ele no formato correto. 
Depois, verifica se o CPF é válido. Se o CPF for inválido, ela mostra uma mensagem de erro. 
Se estiver tudo certo, ela salva o cliente e retorna os dados dele."""
def cadastrar_cliente(cpf: str):
    cpf = normalizar_cpf(cpf)
    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")
    return salvar_cliente(cpf)
