#5.	Desenvolva uma função que gere a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada.
def imprimeTabuada(n):
    for i in range(1,11):
        print(str(i)+" X "+str(n)+" = "+str(i*n))

def main():
    numero = 0
    while (numero <= 0):
        numero = int(input("Informe o número:"))
    
    imprimeTabuada(numero)

main()