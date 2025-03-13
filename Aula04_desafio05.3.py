nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
acomp = str(input("(Apenas para menores): Está acompanhado dos pais?: "))
if idade >= 18 or acomp == "sim": 
    print ("Bem-vindo a nossa festa!")
else:
    print("Acesso negado!")