idade = int(input("Digite sua idade: "))
tem_carteira = str(input("Tem carteira de habilitação?: ")).lower()
if idade >= 18 and tem_carteira == "sim":
    print("Você pode dirigir!")
else:
    print("Sem carteira não dá!")