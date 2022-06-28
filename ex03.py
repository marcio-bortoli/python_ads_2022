#3.	Faça um programa que peça um número inteiro positivo, 
# e em seguida mostre este número invertido.
def inverteNumero(n):
    r = ""
    for i in reversed(range(len(n))):
        r = r + n[i]
    return(r)

def main():
    numero = 0
    while (numero <= 0):
        numero = int(input("Informe o numero:"))   
    
    resultado = inverteNumero(str(numero))
    
    print(resultado)

main()