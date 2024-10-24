def converter_para_meses_dias( anos ):
    meses = anos * 12
    dias = anos * 365
    return meses, dias
anos = int(input("Digite sua idade em anos:"))

meses, dias = converter_para_meses_dias(anos)

print(f"Você tem aproximadamente {meses} meses ou {dias} dias.")
