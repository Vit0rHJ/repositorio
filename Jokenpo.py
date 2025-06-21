import random  #importar a biblioteca para fazer jogadas rândomicas

print("Seja bem vindo(a) ao jogo de Jokenpo (Pedra, Papel e Tesoura)! \nRegras: \nEscolha Pedra, Papel ou Tesoura.\nPedra vence Tesoura \nTesoura vence Papel \nPapel vence Pedra \nEmpates NÃO somam pontos \nBom jogo!") # informam as regras do jogo
nome = input("Digite seu nome, por favor:").strip()  # .strip é usado para ignorar os espaços antes da resposta

listaModalidades = ["1", "2", "3"]  # Lista de modalidades disponiveis
print("Modalidades de jogo: \n1: Humano x Humano \n2: Humano x Computador \n3: Computador x Computador") #mostra as modalidades

modalidade = input(f"Escolha uma modalidade, {nome}, por gentileza: ")
while modalidade not in listaModalidades:  # se não for escolhido 1,2 ou 3 mostra na tela escolha inválida
    print("Escolha inválida!")
    modalidade = input("Escolha uma modalidade (1, 2 ou 3), por gentileza:")  # escolhe a modalidade
if modalidade == "1":  # se a modalidade 1 for escolhida é pedida o nome do segundo jogador
    nome2 = input("Digite seu nome, jogador 2:")

continuar = True
placar1 = 0  # iniciar o placar em zero
placar2 = 0  # iniciar o placar em zero
escolhas = ["pedra", "papel", "tesoura"]  # listando as jogadas possíveis

while continuar:
    if modalidade == "1": #se a modadalidade escolhida for 1
        jogada1 = input(f"Faça sua jogada, {nome}:").strip().lower()
        while jogada1 not in escolhas: #se a jogada escolhida não tiver dentro das escolhas possiveis, mostrar jogada inválida
            print("Jogada inválida")
            jogada1 = input(f"Faça sua jogada, {nome} (Pedra, Papel ou Tesoura):").strip().lower() #.strip para ignorar os espaços e .lower para deixar o texto em lowercase
        jogada2 = input(f"Faça sua jogada, {nome2}:").strip().lower()
        while jogada2 not in escolhas: #se a jogada escolhida não tiver dentro das escolhas possiveis, mostrar jogada inválida
            print("Jogada inválida")
            jogada2 = input(f"Faça sua jogada, {nome2} (Pedra, Papel ou Tesoura):").strip().lower() #pede para o jogador dois informar a sua jogada
        possibilidade1 = (jogada1 == "pedra") and (jogada2 == "papel")
        possibilidade2 = (jogada1 == "papel") and (jogada2 == "tesoura")
        possibilidade3 = (jogada1 == "tesoura") and (jogada2 == "pedra") #aqui são listados a possibilidades das jogadas, nesssas possibilidades a jogada2 vencem em todas
        if possibilidade1:
            placar2 += 1
            print(f"{nome2} venceu!")
        elif possibilidade2:
            placar2 += 1
            print(f"{nome2} venceu!")
        elif possibilidade3:
            placar2 += 1
            print(f"{nome2} venceu!")
        elif jogada1 == jogada2: #empate não soma pontos no placar
            print("Empate!")
        else:
            print(f"{nome} venceu!")
            placar1 += 1
    elif modalidade == "2": #caso a modalidade 2 seja escolhido
        jogada1 = input(f"Faça sua jogada, {nome}:").strip().lower()
        while jogada1 not in escolhas: #se a jogada escolhida não tiver dentro das escolhas possiveis, mostrar jogada inválida
            print("Jogada inválida")
            jogada1 = input(f"Faça sua jogada (Pedra, Papel ou Tesoura):").strip().lower() #Pede para o jogador 1 escolher sua jogada
        jogada2 = random.choice(escolhas) #chamando a função para a jogada aleátoria do segundo jogador
        print("Jogada do computador 2:", jogada2)
        possibilidade1 = (jogada1 == "pedra") and (jogada2 == "papel")
        possibilidade2 = (jogada1 == "papel") and (jogada2 == "tesoura")
        possibilidade3 = (jogada1 == "tesoura") and (jogada2 == "pedra") #são mostradas as possibilidades das jogadas
        if possibilidade1:
            print("Computador venceu!")
            placar2 += 1
        elif possibilidade2:
            print("Computador venceu!")
            placar2 += 1
        elif possibilidade3:
            print("Computador venceu!")
            placar2 += 1
        elif jogada1 == jogada2: #empates não somam pontos
            print("Empate!")
        else:
            print("Você venceu!")
            placar1 += 1
    elif modalidade == "3": #Caso a modalidade 3 seja escolhida
        jogada1 = random.choice(escolhas) #chamando a função para a jogada aleátoria do primeiro jogador
        print("Jogada do computador 1:", jogada1)
        jogada2 = random.choice(escolhas) #chamando a função para a jogada aleátoria do segundo jogador
        print("Jogada do computador 2:", jogada2)
        possibilidade1 = (jogada1 == "pedra") and (jogada2 == "papel")
        possibilidade2 = (jogada1 == "papel") and (jogada2 == "tesoura")
        possibilidade3 = (jogada1 == "tesoura") and (jogada2 == "pedra")
        if possibilidade1:
            print("Computador 2 venceu!")
            placar2 += 1
        elif possibilidade2:
            print("Computador 2 venceu!")
            placar2 += 1
        elif possibilidade3:
            print("Computador 2 venceu!")
            placar2 += 1
        elif jogada1 == jogada2:
            print("Empate!")
        else:
            print("Computador 1 venceu!")
            placar1 += 1
    respostaContinuar = input("Deseja continuar com o jogo (Sim ou Não)?:").strip().lower()
    while respostaContinuar not in ["sim", "s", "não", "nao", "n"]:
        print("Resposta inválida! Por favor, responda com 'Sim' ou 'Não'.")
        respostaContinuar = input("Deseja continuar com o jogo (Sim ou Não)?:").strip().lower()
    if respostaContinuar in ["n", "não", "nao"]:
        continuar = False
        print("Placar final:", placar1, "a", placar2)
        print("Obrigado por jogar!")
    elif respostaContinuar in ["sim", "s"]:
        respostaModalidade = input("Deseja trocar de modalidade (Sim ou Não)?").strip().lower()
        while respostaModalidade not in ["sim", "s", "não", "nao", "n"]:
            print("Resposta inválida")
            respostaModalidade = input("Deseja trocar de modalidade (Sim ou Não)?").strip().lower()
        if respostaModalidade in ["sim", "s"]:
            novaModalidade = input("Escolha uma modalidade, por gentileza: ")
            while novaModalidade not in listaModalidades:
                print("Escolha inválida!")
                novaModalidade = input("Escolha uma modalidade, por gentileza: ")
            while novaModalidade == modalidade:
                print("Você já está nesta modalidade!")
                novaModalidade = input("Escolha uma modalidade diferente, por gentileza: ")
            modalidade = novaModalidade
            if modalidade == "1":
                print("Novo modo selecionado: Humano x Humano")
                nome2 = input("Digite seu nome, jogador 2:")
            elif modalidade == "2":
                print("Novo modo selecionado: Humano x Computador")
            elif modalidade == "3":
                print("Novo modo selecionado: Computador x Computador")
        continuar = True