from cadastro  import normalizar_cpf

print(normalizar_cpf(cpf))
try:
    cpf= "01234586798"
    print(normalizar_cpf(cpf))

except(ValueError, TypeError) as e:
    print("Erro de processamento", e)