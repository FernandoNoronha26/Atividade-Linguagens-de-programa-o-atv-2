def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    nova_frase = ' '.join(palavras_invertidas)
    return nova_frase
frase = input("Digite uma frase: ")
frase_invertida = inverter_palavras(frase)
print("Frase com palavras invertidas: ", frase_invertida)