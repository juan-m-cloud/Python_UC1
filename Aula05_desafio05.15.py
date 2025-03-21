lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 == lado2 == lado3:
    print("O triângulo é Equilátero (todos os lados são iguais).")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles (dois lados são iguais).")
else:
    print("O triângulo é Escaleno (todos os lados são diferentes).")
