idade = int (input("Digite sua idade: "))
renda = float (input("Digite sua renda mensal R$: "))
restr = str (input("Você tem algum tipo de restrição no SPC/SERASA? ")).lower()
if idade >= 21 and renda >= 2000 and restr == "não":
    print("Você pode solicitar empréstimo!")
else:
    print("Você não pode solicitar empréstimo!")