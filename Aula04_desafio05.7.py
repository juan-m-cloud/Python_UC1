idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Pode viajar sozinho")
elif 16 <= idade <= 17:
    print("Pode viajar com autorização dos pais")
else:
    print("Não pode viajar sozinho")