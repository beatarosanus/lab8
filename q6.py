import random
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    def tomar_dano(self, valor):
        self.vida -= valor

class Mago(Personagem):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana
    def __str__(self):
        return f"Mago: {self.nome} | Vida: {self.vida} | Mana: {self.mana}"
    def __add__(self, valor):
        self.mana += valor
        return self.mana
    def __sub__(self, valor):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana
    def __mul__(self, fator):
        self.mana *= fator
        return self.mana
    def __truediv__(self, valor):
        self.mana /= valor
        return self.mana

class Barbaro(Personagem):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.stamina = stamina
        self.furia = False
    def __str__(self):
        return f"Bárbaro: {self.nome} | Vida: {self.vida} | Stamina: {self.stamina} | Fúria: {self.furia}"
    def __add__(self, valor):
        if self.furia:
            self.stamina += valor * 1.5
        else:
            self.stamina += valor
        return self.stamina
    def __sub__(self, valor):
        self.stamina -= valor
        if self.stamina <= 0:
            self.stamina = 0
            if self.furia == False:
                self.furia = True
                self.stamina = 5
        return self.stamina
    def __mul__(self, fator):
        self.stamina *= fator
        if self.furia:
            self.vida += 5
        return self.stamina
    def __truediv__(self, valor):
        self.stamina /= valor
        return self.stamina

print("=== CRIAÇÃO DO PERSONAGEM ===")
nome = input("Digite o nome: ")
vida = int(input("Digite a vida: "))
tipo = input("Escolha o tipo (Mago ou Bárbaro): ")

if tipo.lower() == "mago":
    mana = float(input("Digite a mana: "))
    personagem = Mago(nome, vida, mana)
elif tipo.lower() == "bárbaro":
    stamina = float(input("Digite a stamina: "))
    personagem = Barbaro(nome, vida, stamina)
else:
    print("Tipo inválido!")
    exit()

while personagem.vida > 0:
    print(personagem)
    print("=== MENU ===")
    print("1 - Tomar poção simples")
    print("2 - Tomar poção especial")
    print("3 - Ataque básico")
    print("4 - Ataque especial")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        personagem + 5
    elif opcao == 2:
        personagem * 1.5
    elif opcao == 3:
        personagem - 2
    elif opcao == 4:
        personagem / 2
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
        continue

    dano = random.randint(1, 10)
    personagem.tomar_dano(dano)

    print(f"Você recebeu {dano} de dano!")

    if personagem.vida <= 0:
        print("Seu personagem morreu!")
    else:
        print(personagem)
