
print ("DIGITE UM MÊS PARA SELECIONAR")
print ("""
1 - JANEIRO
2 - FEVEREIRO
3 - MARÇO 
4 - ABRIL
5 - MAIO 
6 - JUNHO
7 - JULHO
8 - AGOSTO
9 - SETEMBRO
10 - OUTUBRO
11 - NOVEMBRO 
 12 - DEZEMBRO

 """)

while True:
    try: 
        numero = int(input("Escolha uma opção: "))

        match numero:
                case 1:
                    escolhido = "JANEIRO"
                case 2:
                    escolhido = "FEVEREIRO"
                case 3: 
                    escolhido = "MARÇO"
                case 4: 
                    escolhido = "ABRIL"
                case 5:
                    escolhido = "MAIO"
                case 6:
                    escolhido = "JUNHO"
                case 7:
                    escolhido= "JULHO"
                case 8:
                    ecolhido = "AGOSTO"
                case 9:
                    escolhido = "SETEMBRO"
                case 10:
                    escolhido = "OUTUBRO"
                case 11: 
                    escolhido = "NOVEMBRO"
                case 12:
                    escolhido = "DEZEMBRO"


    except ValueError ():
            escolhido = "NÚMERO INVALIDO"

print(f"O mês escolhido é {escolhido}")
