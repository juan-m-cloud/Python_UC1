banidos = ["João", "Maria", "Carlos"]  
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
acomp = str(input("(Apenas para menores): Está acompanhado dos pais?: ")) .lower()
if nome in banidos:
    print("Acesso negado! Você está na lista de banidos.")
elif idade >= 18 or acomp == "sim":
    print("Bem-vindo à nossa festa!")
else:
    print("Acesso negado!")
