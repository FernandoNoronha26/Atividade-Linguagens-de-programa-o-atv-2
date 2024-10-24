def menor_numero(a, b, c):
    return min(a, b, c)
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

menor = menor_numero(a, b, c)

print(f"O menor numero digitado é: {menor}")
