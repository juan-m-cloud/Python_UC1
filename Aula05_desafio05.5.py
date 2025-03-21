senhas_fracas = ["123456", "senha"]
nome = str(input("Digite seu nome: "))
senha = str(input("Digite sua senha: "))
if len(nome) < 3:
    print("Erro: O nome deve ter pelo menos 3 letras.")
elif len(senha) < 6:
    print("Erro: A senha deve ter pelo menos 6 caracteres.")
elif senha in senhas_fracas:
    print("A senha é muito fraca. Escolha outra!")
else:
    print("Bem-vindo, " + nome + "!")