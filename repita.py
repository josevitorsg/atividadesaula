# Estrutura que simula "repita ate que"
opcao = -1 # variavel que armazena a opcao do usuario

while True:
    print("""
          ------------------
          1 - Dizer olá! Mundo!
          2 - Dizer oi! Mundo!
          0 - Sair do programa!

          """)
    #lê a entrada do usuário:
    try:
        opcao = int(input("Escolha uma opção: "))
        # Trata a entrada do usuario e retorna um erro caso a opcao selecionada seja invalida
    except ValueError:
        print("ERROR@!")
    else:
        if opcao == 1:
            print("Olá! Mundo!")
        elif opcao == 2:
            print("Oi! Mundo!")
        elif opcao == 0:
            print("Saindo do programa...")
        else:
            print("Selecione uma opção valida: ")
        
    if opcao == 0:
        break

