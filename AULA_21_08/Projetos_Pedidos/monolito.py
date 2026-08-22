print("=== Cadastro de Cliente ===")
nome = input("insira o nome do cliente: ")
telefone = input("Insira o telefone do cliente: ")
endereço = input("Insira o endereço do cliente: ")

print("=== Produtos do pedido ===")
produtos = []
valores = []

while True:
     produto =input("Nome do produto (ou digite'fim' para encerrar):")
     if produto =="fim":
          break
     valor = float(input(f"Valor de {produto}:"))
     produtos.append(produto)
     valores.append(valor)

     subtotal = 0.0
     for v in valores: 
        subtotal = subtotal + v

desconto = float(input("Digite o valor do desconto em %: "))
subtotal_com_desconto = subtotal - (subtotal * desconto / 100)
total = subtotal_com_desconto + 10.0  # Adiciona o valor do frete

print("=== Recibo ====")
print(f"Cliente: {nome} / telefone: {telefone} ")
print(f"Endereço: {endereço}")

for i in range(len(produtos)):
        print(f"Produto: {produtos[i]} - R$ {valores[i]:}")
print(f"Subtotal: R$ {round(subtotal, 2)}")
print(f"Desconto: {desconto}%")
print(f"Total a pagar: R$ {round(total, 2)}")
