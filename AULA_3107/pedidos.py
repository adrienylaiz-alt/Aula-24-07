def processar_pedido(dados):
    if not dados ["cpf"]: return False
    total = 0
    for i in dados["itens"]:
        total += i ["preco"] * i["qtd"]
        imposto = total *0.18
        db. execute ("INSERT ...")
        smtp.send(dados["email"])
        print ("ok")
        return total + imposto

    #problema está na função fazer mais de uma coisa no mesmo codigo, ao inves de fazer em partes menores uma função para cada coisa
    