idade = int(input("Digite sua idade: "))
usuario = str(input("Digite seu usúario: "))
senha = str(input("Digite sua senha: "))
if idade >= 18 and usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")