import math

def forma_triangulo(a, b, c):
    if a < b + c and b< a + c and c < a + b:
        return True
    return False

def calcular_area(a, b, c):
    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if forma_triangulo(a, b, c):
    area = calcular_area(a, b, c)
    print(f"Os valores informados formam um triângulo e a área é: {area:.2f}")
else:
    print(f"Os valores informados {a}, {b}, {c} não formam um triãngulo.")


