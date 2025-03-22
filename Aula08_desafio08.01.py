
import sys

def realizar_operacao(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Erro: Operação inválida!"

def main():
    if len(sys.argv) != 4:
        print("Uso: python programa.py <número1> <operacao> <número2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[3])
        operacao = sys.argv[2]
    except ValueError:
        print("Erro: Números inválidos!")
        sys.exit(1)

    resultado = realizar_operacao(num1, num2, operacao)
    print(f"{num1} {operacao} {num2} = {resultado}")

if __name__ == "__main__":
    main()