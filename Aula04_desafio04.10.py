vcom = float(input("Digite o valor da compra : "))
if vcom >= 501:
    desconto = vcom * 0.15

elif 200 >= vcom >= 500: 
    desconto = vcom * 0.10

else: 
   desconto = vcom * 0.05
valor_final = vcom - desconto

print("-" * 30)
print(f"Valor com desconto: {valor_final:.2f}")
print("-" * 30)
