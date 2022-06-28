#2.	Escreva uma função que recebe dois valores e imprime 
# o menor dos dois. Se eles forem iguais, imprima que eles 
# são iguais.
def verificaValores(n1, n2):
    if (n1 < n2):
        msg = "O menor número é "+str(n1)
    elif (n2 < n1):
        msg = "O menor número é "+str(n2)
    else:
        msg = "Os números são iguais"
    return msg

def main():
    valor1 = int(input("Informe o valor 1:"))
    valor2 = int(input("Informe o valor 2:"))
    mensagem = verificaValores(valor1, valor2)
    print(mensagem)

main()