#8.	O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa.
#De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas, como:
#- abaixo de 18.5: Abaixo do peso
#- entre 18.5 e 25: Peso ideal
#- entre 25 e 30: Sobrepeso
#- entre 30 e 40: Obesidade
#- acima de 40: Obesidade mórbida
#Observação: O IMC é calculado pela expressão peso/altura² (peso dividido pelo
#quadrado da altura). Faça um algoritmo que leia a altura e o peso, e imprima a classificação da 
# pessoa conforme a tabela acima – usar função.
def classificaIMC(p, a):
    valorIMC = p/(a**2)
    if (valorIMC < 18.5):
        print("Abaixo do peso")
    elif (valorIMC >= 18.5) and (valorIMC < 25):
        print("Peso ideal")
    elif (valorIMC >= 25) and (valorIMC < 30):
        print("Sobrepeso")
    elif (valorIMC >= 30) and (valorIMC < 40):
        print("Obsidade")
    else:
        print("Obesidade mórbida")    

def main():
    peso = 0
    while (peso <= 0):
        peso = float(input("Informe o peso:"))

    altura = 0
    while (altura <= 0):
        altura = float(input("Informe a altura:"))    

    classificaIMC(peso, altura)

main()