n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
ent = str(input("Entregou o trabalho extra? ")).lower()
media = (n1 + n2 + n3) / 3
if media >= 7 or ent == "sim":
    print("Aprovado")
else:
    print("Reprovado")