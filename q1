class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def __add__(self, valor_yuan):
        self.saldo += valor_yuan
        print("Novo saldo:", self.saldo)

    def __sub__(self, valor_yuan):
        self.saldo -= valor_yuan
        print("Novo saldo:", self.saldo)


print("**** OPÇÕES DE MOEDA ****")
print("1 - USD")
print("2 - BRL")

opcao = int(input("Escolha uma moeda: "))

if opcao == 1:
    valor = float(input("Digite o saldo: "))
    carteira = Carteira("USD", valor * 0.14)

elif opcao == 2:
    valor = float(input("Digite o saldo: "))
    carteira = Carteira("BRL", valor * 0.85)

else:
    print("Opção inválida!")
    exit()

print("**** OPERAÇÕES ****")
print("1 - Adicionar")
print("2 - Retirar")
print("3 - Sair")

while True:
    operadores = int(input("Escolha uma operação: "))

    if operadores == 1:
        valor_yuan = float(input("Digite o valor: "))
        carteira.__add__(valor_yuan)

    elif operadores == 2:
        valor_yuan = float(input("Digite o valor: "))
        carteira.__sub__(valor_yuan)

    elif operadores == 3:
        print("Programa encerrado.")
        break

    else:
        print("Operação inválida!")
