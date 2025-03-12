a = float(input("Digite sua altura(em metros)"))
b = float(input("Digite seu peso(em KG)"))
IMC = b / (a ** 2)
if IMC < 18.5:
    print("Você está abaixo do peso:")
elif 18.5 <= IMC <= 24.9:
    print("Você está no peso ideal")
else:
    print("Obesidade.")