#4.	Faça uma função que receba a data de nascimento (dd/mm/aaaa) do usuário, 
# e imprima a data com o nome do mês por extenso. O programa deve chamar uma 
# função que retorna o mês convertido. Exemplo:
#– Entrada - Data de Nascimento: 29/10/1973
#– Saída - Você nasceu em 29 de Outubro de 1973.
def dataPorExtenso(d, m, a):
    if (m == 1 ):
        mesExtenso = "janeiro"
    elif (m == 2):
        mesExtenso = "fevereiro"
    elif (m == 3):
        mesExtenso = "março"
    elif (m == 4):
        mesExtenso = "abril"
    elif (m == 5):
        mesExtenso = "maio"
    elif (m == 6):
        mesExtenso = "junho"
    elif (m == 7):
        mesExtenso = "julho"
    elif (m == 8):
        mesExtenso = "agosto"
    elif (m == 9):
        mesExtenso = "setembro"
    elif (m == 10):
        mesExtenso = "outubro"
    elif (m == 11):
        mesExtenso = "novembro"
    elif (m == 12):
        mesExtenso = "dezembro"
    print("Você nasceu em "+str(d)+" de "+mesExtenso+" de "+str(a))

def main():
    pedirDataNovamente = True
    while (pedirDataNovamente):
        data = input("Informe a data no formato DDMMAAAA:")
        dia = int(data[0:2])
        mes = int(data[2:4])
        ano = int(data[4:8])
       
        if not ((dia >= 1) and (dia <= 31)):
            print("Dia inválido")
            pedirDataNovamente = True
        else:    
            pedirDataNovamente = False
        
        if not ((mes >=1) and (mes <= 12)):
            print("Mês inválido")
            pedirDataNovamente = True
        else:
            pedirDataNovamente = False   

    dataPorExtenso(dia,mes,ano)

main()