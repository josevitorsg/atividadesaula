# Solicita ao usuário um número inicial e final

numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))

# Verifica se o número inicial é menor que o número final

if numero_inicial <= numero_final:
    for numero in range(numero_inicial, numero_final + 1):
        print(numero)
else:
    for numero in range(numero_inicial, numero_final - 1, -1): # menos 1 e define a ordem decrescente.
        print(numero)








