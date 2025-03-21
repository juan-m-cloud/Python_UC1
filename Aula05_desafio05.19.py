idade = int (input("Digite sua idade: "))
if 18 <= idade <= 69:
    print("É obrigatório votar!")
elif 16 <= idade <= 17 or idade >70:
    print("Não é obrigatório votar!")
else:
    print("Você não pode votar!")