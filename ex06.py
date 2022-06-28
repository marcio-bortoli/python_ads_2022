#6.	Implementar algoritmo usando função para calcular o fatorial de um número. 
# Para quem não sabe, fatorial é a multiplicação de todos os números de 1 até 
# ao número que se está calculando. Por exemplo: Fatorial de 5 (5!) = 1 * 2 * 3 * 4 * 5 = 120.
# Leia um número positivo e maior que zero, e imprima o fatorial do número. Apresentar o teste de mesa na solução do exercício.
def calculaFatorial(n):
    r = 1
    for i in range(1,n+1):
        r = r * i
    return r

def main():
    numero = 0
    while (numero <= 0):
        numero = int(input("Informe o número:"))
    
    resultado = calculaFatorial(numero)

    print("O resultado do fatorial é ",resultado)

main()