class Onibus:

    def __init__(self, placa, nome_motorista, num_assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        self.assentos = [False for i in range(num_assentos)]

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self, indice):
        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")

        return self.assentos[indice]

    def __setitem__(self, indice, valor):
        if indice < 0 or indice >= len(self.assentos):
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")

        if isinstance(valor, bool) == False:
            raise TypeError("Valor deve ser booleano (True/False)")

        self.assentos[indice] = valor

    def __str__(self):
        total = len(self.assentos)
        ocupados = self.assentos.count(True)
        livres = total - ocupados

        return (
            f"Ônibus (Placa: {self.placa}) - Motorista: {self.nome_motorista}\n"
            f"Assentos totais: {total}\n"
            f"Assentos ocupados: {ocupados}\n"
            f"Assentos livres: {livres}"
        )


onibus = Onibus("ABC-1234", "João Silva", 10)

print(len(onibus))

onibus[0] = True

print(onibus)
