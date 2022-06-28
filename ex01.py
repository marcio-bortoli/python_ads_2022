#1.	Faça uma função que calcula a potência A elevado a B. 
# Informe os valores para valores A e B, considere valores 
# inteiros (não use o operador **).
def potencia(b,e):
    r = 1
    for i in range(1,e+1):
        r = r * b
    return r

def main():
    base = 0
    while (base <= 0):
        base = int(input("Informe a base: "))

    expoente = 0
    while (expoente <=0):
        expoente = int(input("Informe o expoente:"))

    resultado = potencia(base, expoente)
    print("Resultado:", resultado)

main()