def somar(n1,n2):
    r = n1 + n2
    return r

def subtrair(n1, n2):
    r = n1 - n2
    return r

def dividir(n1,n2):
    r = n1 / n2
    return r

def multiplicar(n1,n2):
    r = n1 * n2
    return r

x = int(input("Informe o valor 1: "))
op = input("Informe o operador [+,-,/,*]: ")
y = int(input("Informe o valor 2: "))
if (op == '+'):
    resultado = somar(x,y)
elif (op == '-'):
    resultado = subtrair(x,y)
elif (op == '/'):
    resultado = dividir(x,y)
elif (op == "*"):
    resultado = multiplicar(x,y)

print("Resultado da operacao", format(resultado,".2f"))
