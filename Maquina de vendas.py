matrizInfoProdutos = [["Coca-Cola", "Pepsi", "Monster", "Café", "Redbull"],
                      [1, 2, 3, 4, 5],
                      [3.75, 3.67, 9.96, 1.25, 13.99],
                      [2, 5, 1, 100, 2]]

# estoque de notas e moedas (em centavos para facilitar os cálculos)
estoqueTroco = {
    20000: 5,  # R$200
    10000: 10,  # R$100
    5000: 10,  # R$50
    2000: 20,  # R$20
    1000: 20,  # R$10
    500: 30,  # R$5
    200: 50,  # R$2
    100: 100,  # R$1
    50: 100,  # 50 centavos
    25: 100,  # 25 centavos
    10: 100,  # 10 centavos
    5: 100,  # 5 centavos
    1: 100  # 1 centavo
}


# função para exibir os produtos da máquina de bebidas
def exibir_produtos():
    print("\nPRODUTOS DISPONÍVEIS:")
    for i in range(len(matrizInfoProdutos[0])):
        # imprimindo cada bebida e suas respectias informações (retiradas da matriz)
        print(
            f"{matrizInfoProdutos[0][i]} - R${matrizInfoProdutos[2][i]:.2f} - Estoque: {matrizInfoProdutos[3][i]} - ID: {matrizInfoProdutos[1][i]}")


# função para verificar o código e o estoque simultaneamente
def verificar_codigo_e_estoque():
    while True:
        codigoBebida = int(input("Digite o código da bebida desejada: "))
        indice = codigoBebida - 1
        if codigoBebida in matrizInfoProdutos[1]:  # verificação do código (ID)
            print(f"Bebida escolhida: {matrizInfoProdutos[0][indice]}")
            if matrizInfoProdutos[3][indice] > 0:  # verificação de estoque
                return codigoBebida
            else:
                print("Não há mais estoque dessa bebida! Escolha outra bebida.")
        else:
            print("Código inexistente! Digite novamente.")


# função para cálculo do troco
def calcular_troco(valor_devido):
    valorPago = float(input("Insira o valor pago: "))
    while valorPago < valor_devido:  # verificação do valor pago
        print("Valor pago insuficiente.")
        valorPago = float(input("Digite o valor pago: "))

    troco = int(round((valorPago - valor_devido) * 100))  # convertendo troco para inteiro e arredondando
    print(f"Troco a ser dado: R${troco / 100:.2f}")

    # uma cópia do estoque para trabalhar sem alterar o estoque de troco original até confirmar
    estoque_temp = estoqueTroco.copy()
    troco_temp = troco  # cópia da variável "troco" para preservar o valor inicial
    resultado = {}  # dicionário vazio para armazenar as notas/moedas que serão utilizadas no troco

    # ordenando a cópia do estoque de troco para ordem decrescente, com sorted e reverse
    denominacoes = sorted(estoque_temp.keys(), reverse=True)

    # percorrendo todas as denominações de notas e moedas
    for valor in denominacoes:
        if troco_temp >= valor and estoque_temp[valor] > 0:  # verificação de valor e estoque da nota/moeda para troco
            quantidade_possivel = min(estoque_temp[valor],
                                      troco_temp // valor)  # não pegamos mais notas/moedas do que temos no estoque
            if quantidade_possivel > 0:
                resultado[valor] = quantidade_possivel
                troco_temp -= quantidade_possivel * valor  # reduzimos o troco_temp, subtraindo o valor total das notas/moedas que acabamos de usar.
                estoque_temp[valor] -= quantidade_possivel
                # atualizamos "estoque_temp", reduzindo a quantidade disponível dessa denominação

    # se ao final de todo o processo o troco restante ainda ser maior que 0, logo não há notas/moedas necessárias para finalizar a operação
    if troco_temp > 0:
        print("Não há notas/moedas suficientes para dar o troco exato. Compra cancelada.")
        return False

    # método "items()" para retornar uma lista de tuplas de "resultado". Ex: [(chave, valor), ...]
    for item in resultado.items():  # percorrendo cada tupla
        valor = item[0]  # índice 0 de cada tupla associando ao valor da nota/moeda
        quantidade = item[1]  # índice 1 de cada tupla associando ao valor da quantidade utilizada
        # se chegou aqui, podemos confirmar o troco e atualizar o estoque real
        estoqueTroco[valor] -= quantidade

        # realizando verificações para distinguir nota(s) e moeda(s) e imprimindo na tela
        if valor > 100:
            if quantidade > 1:
                print(f"{quantidade} notas de R${(valor / 100):.0f} reais.")
            else:
                print(f"{quantidade} nota de R${(valor / 100):.0f} reais.")
        elif valor == 100 and quantidade == 1:
            print(f"{quantidade} moeda de {(valor / 100):.0f} real.")
        elif valor == 1:
            print(f"{quantidade} moedas de {valor} centavo.")
        else:
            if quantidade > 1:
                print(f"{quantidade} moedas de {valor} centavos.")
            else:
                print(f"{quantidade} moeda de {valor} centavos.")

    # retorna True confirmando que o cálculo do troco funcionou corretamente
    return True


# função com as configurações do modo administrador (admin)
def modo_admin():
    senha = "admin123"
    tentativa = input("Digite a senha de administrador ou 'sair' para voltar: ")

    if tentativa.strip().lower() == 'sair':
        return
    while tentativa != senha:
        print("Comando inválido!")
        tentativa = input("Digite a senha de administrador ou 'sair' para voltar: ")
        if tentativa.lower() == 'sair':
            return

    while True:
        print("\nMODO ADMINISTRADOR")
        print("1 - Cadastrar novo produto")
        print("2 - Editar produto existente")
        print("3 - Remover produto")
        print("4 - Visualizar todos os produtos")
        print("5 - Gerenciar estoque de troco")
        print("6 - Sair do modo administrador")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nomeNovaBebida = input("Nome do novo produto: ")
            novo_id = max(matrizInfoProdutos[1]) + 1
            preco = float(input("Preço do produto: "))
            estoque = int(input("Quantidade em estoque: "))

            matrizInfoProdutos[0].append(nome)
            matrizInfoProdutos[1].append(novo_id)
            matrizInfoProdutos[2].append(preco)
            matrizInfoProdutos[3].append(estoque)

            print(f"Produto '{nomeNovaBebida}' cadastrado com sucesso! ID: {novo_id}")

        elif opcao == '2':
            exibir_produtos()
            id_editar = int(input("Digite o ID do produto que deseja editar: "))

            if id_editar in matrizInfoProdutos[1]:
                indice = id_editar - 1

                print("\nDeixe em branco para manter o valor atual")
                novo_nome = input(f"Nome atual: {matrizInfoProdutos[0][indice]} - Novo nome: ")
                novo_preco = input(f"Preço atual: {matrizInfoProdutos[2][indice]} - Novo preço: ")
                novo_estoque = input(f"Estoque atual: {matrizInfoProdutos[3][indice]} - Novo estoque: ")

                if novo_nome:
                    matrizInfoProdutos[0][indice] = novo_nome
                if novo_preco:
                    matrizInfoProdutos[2][indice] = float(novo_preco)
                if novo_estoque:
                    matrizInfoProdutos[3][indice] = int(novo_estoque)
                print("Produto atualizado com sucesso!")
            else:
                print("ID inválido!")

        elif opcao == '3':
            exibir_produtos()
            id_remover = int(input("Digite o ID do produto que deseja remover: "))

            if id_remover in matrizInfoProdutos[1]:
                indice = id_remover - 1
                nome_removido = matrizInfoProdutos[0].pop(indice)
                matrizInfoProdutos[1].pop(indice)
                matrizInfoProdutos[2].pop(indice)
                matrizInfoProdutos[3].pop(indice)

                print(f"Produto '{nome_removido}' removido com sucesso!")
            else:
                print("ID inválido!")

        elif opcao == '4':
            exibir_produtos()

        elif opcao == '5':
            print("\nESTOQUE DE TROCO:")

            for valores in sorted(estoqueTroco.items(), reverse=True):
                valor = valores[0]
                quantidade = valores[1]
                if valor > 100:
                    print(f"Notas de R${valor / 100:.2f}: {quantidade}")
                else:
                    print(f"Moedas de R${valor / 100:.2f}: {quantidade}")

            print("\n1 - Adicionar notas/moedas")
            print("2 - Remover notas/moedas")
            print("3 - Voltar")
            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == '1':
                valor = int(float(input("Valor (em R$): ")) * 100)
                if valor in estoqueTroco:
                    quantidade = int(input("Quantidade a adicionar: "))
                    estoqueTroco[valor] += quantidade
                    print("Estoque atualizado!")
                else:
                    print("Valor inválido!")

            elif sub_opcao == '2':
                valor = int(float(input("Valor (em R$): ")) * 100)
                if valor in estoqueTroco:
                    quantidade = int(input("Quantidade a remover: "))
                    if estoqueTroco[valor] >= quantidade:
                        estoqueTroco[valor] -= quantidade
                        print("Estoque atualizado!")
                    else:
                        print("Quantidade indisponível!")
                else:
                    print("Valor inválido!")

        elif opcao == '6':
            print("Saindo do modo administrador...")
            break

        else:
            print("Opção inválida!")


# loop principal
while True:
    print("\nMÁQUINA DE BEBIDAS")
    print("1 - Modo Cliente")
    print("2 - Modo Administrador (senha: admin123)")
    print("3 - Sair")

    modo = input("Escolha o modo de operação: ")

    if modo == '1':
        exibir_produtos()
        codigoValido = verificar_codigo_e_estoque()
        indice = codigoValido - 1
        valor_devido = matrizInfoProdutos[2][indice]

        '''aqui usamos uma condição "if" na função "calcular_troco" pois ela retorna True ou False
        dependendo se a operação do troco funcionou
        '''
        if calcular_troco(valor_devido):
            matrizInfoProdutos[3][indice] -= 1  # reduzindo o estoque da bebida
            print("Compra realizada com sucesso!")
        else:
            print("Compra cancelada.")

        print("Volte sempre!\n")

    elif modo == '2':
        modo_admin()

    elif modo == '3':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida!")