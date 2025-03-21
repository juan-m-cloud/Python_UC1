lista_negra = ["admin1"]
ip_banido =["192.168.1.1"]
usuario = str(input("Digite o nome de usúario : "))
senha = str(input("Digite sua senha :")) 
ip = str(input("Digite o seu ip : "))
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
elif usuario in lista_negra:
    print("Você está banido.")
elif ip in ip_banido:
    print("Ip bloqueado.")
else:
    print("Acesso negado")