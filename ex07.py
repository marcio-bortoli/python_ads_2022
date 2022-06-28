#7.	Faça um algoritmo usando função, onde informado três valores numérico (a, b e c), 
# identifique se os valores formam um triângulo. Considerar as regras:
#Se o comprimento do lado A for menor que a soma dos comprimentos dos lados B e C;
#Se o comprimento do lado B for menor que a soma dos comprimentos dos lados A e C;
#Se o comprimento do lado C for menor que a soma dos comprimentos dos lados A e B.
#A<(B+C) e B<(A+C) e C<(A+B)
#E imprima se o triângulo é:
#- Equilátero: os três lados com comprimentos iguais.
#- Isósceles: dois lados com comprimentos iguais.
#- Escaleno: Três lados com comprimentos diferentes.
def identificaTriangulo(A,B,C):
    if (A == B) and (B == C):
        print("Triangulo Equilátero")
    elif (A == B) or (B == C) or (A == C):
        print("Triangulo Isóscles")
    else:
        print("Triangulo Escaleno")

def main():
    ladoA = 0
    ladoB = 0
    ladoC = 0
    while not ((ladoA < (ladoB+ladoC)) and (ladoB < (ladoA+ladoC)) and (ladoC < (ladoA+ladoB))):
        ladoA = int(input("Informe o lado A:"))
        ladoB = int(input("Informe o lado B:"))
        ladoC = int(input("Informe o lado C:"))

    identificaTriangulo(ladoA, ladoB, ladoC)    

main()