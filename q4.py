class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome} | Altura: {self.altura}"

    def __gt__(self, other):
        return self.altura > other.altura

    def __lt__(self, other):
        return self.altura < other.altura


nome = input("Digite o nome da primeira pessoa: ")
altura = float(input("Digite a altura da primeira pessoa: "))

pessoinha = Pessoa(nome, altura)

other_name = input("Digite o nome da segunda pessoa: ")
other_high = float(input("Digite a altura da segunda pessoa: "))

other_people = Pessoa(other_name, other_high)

print(pessoinha)
print(other_people)

print("A primeira pessoa é mais alta:", pessoinha > other_people)
print("A primeira pessoa é mais baixa:", pessoinha < other_people)
