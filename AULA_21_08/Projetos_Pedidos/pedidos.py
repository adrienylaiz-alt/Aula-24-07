def cadastrar_clientes():
    nome = input("insira o nome do cliente: ")
    telefone = input("Insira o telefone do cliente: ")
    endereço = input("Insira o endereço do cliente: ")
    return{"nome":nome, "telefone":telefone, "endereço":endereço}

def cadastrar_produtos():
    produtos = []
    while True:
        produto = input("Nome do produto (ou digite 'fim' para encerrar): ")
        if produto == "fim":
            break
        valor = float(input(f"Valor de {produto}: "))
        produtos.append({"nome": produto, "valor": valor})
    return produtos

def calcular_total(valores):
    subtotal = sum(valores)
    taxa_entrega = 5.0
    total = subtotal + taxa_entrega
    return subtotal, total


def emitir_recibo(cliente, produtos, subtotal, total):
    print("=== Recibo ====")
    print(f"Cliente: {cliente['nome']} - telefone: {cliente['telefone']}")
    print(f"Endereço: {cliente['endereço']}")
    for p in produtos:
        print(f" -{p['nome']}: R$ {p['valor']:.2f}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

cliente = cadastrar_clientes()
produtos = cadastrar_produtos()
valores = [p['valor'] for p in produtos]
subtotal, total = calcular_total(valores)
emitir_recibo(cliente, produtos, subtotal, total)