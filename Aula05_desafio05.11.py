valor_compra = float(input("Digite o valor da compra: R$ "))
quantidade = int(input("Digite a quantidade de produtos: "))
if valor_compra >= 100 or quantidade >= 5:
    print("Você tem direito a 10% de desconto!")
else:
    print("Não atingiu o valor/quantidade mínima para obter desconto!")
