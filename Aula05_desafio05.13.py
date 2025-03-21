idade = int (input("Digite sua idade: "))
acomp = str (input("(Apenas para maiores de 16): Você está acompanhado de um responsável? ")).lower()
if idade >= 18:
    print("Seja bem-vindo")
elif 16 <= idade <= 17 and acomp == "sim":
    print("Seja bem-vindo")
else:
    print("Desculpe, você não pode entrar")
