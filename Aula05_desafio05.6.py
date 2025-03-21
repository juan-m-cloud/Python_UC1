valor_compra = float(input("Digite o valor da compra: R$ "))
quantidade = int(input("Digite a quantidade de produtos: "))
cupom = str(input("Usou cupom na última compra? ")).lower()
if cupom == "sim":
    print("Não tem direito a cupom, já usou na última compra!")
elif valor_compra >= 100 or quantidade >= 5:
    print("Você tem direito a 10% de desconto!")
else:
    print("Não atingiu o valor/quantidade mínima para obter desconto!")
