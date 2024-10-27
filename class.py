class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(f'O vendedor {self.nome} bateu a meta')
        else:
            print(f'O vendedor {self.nome} não bateu a meta.')



vendedor1 = Vendedor('Henry')
vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)

