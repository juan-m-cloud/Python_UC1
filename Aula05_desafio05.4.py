
import random

numero_secreto = random.randint(1, 10) 
tentativas = 3 

print("Adivinhe o número entre 1 e 10. Você tem 3 tentativas!")

for tentativa in range(tentativas):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break  # Sai do loop se acertar
    else:
        print("Errado!")
        if tentativa < tentativas - 1:
            print(f"Você tem mais {tentativas - 1 - tentativa} tentativas.")
        else:
            print(f"Fim do jogo! O número era {numero_secreto}.")