num1 = int(input("Digite o valor do primeiro número"))
num2 = int(input("Digite o valor do segundo número"))
num3 = int(input("Digite o valor do terceiro número"))
if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    print("Os valores formam um triângulo")
else:
    print("Não pode formar um triangulo")