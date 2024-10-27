

class Caneca:
    def __init__(self, nome, logo, cor):
        self.nome = nome
        self.logo = logo
        self.cor = cor
        self.status = 'Cheia'
    
    def beber(self):
        self.status = 'Vazia'
        return f'É da {self.nome} que eu estou bebendo'

    def encher(self):
        self.status = 'Cheia'
        return f'Estou enchendo a {self.nome}'


class Caneca_Londrina(Caneca):
    def __init__(self):
        super().__init__('Caneca Londrina', 'Cidade de Londres', 'Branca')


caneca1 = Caneca_Londrina()
caneca2 = Caneca('Caneca de HOTD', 'Dragão Sunfyre', 'Azul Escuro')

'''
print(f'A {caneca1.nome} possui a logo do {caneca1.logo}')
print(f'A {caneca2.nome} possui a logo do {caneca2.logo}')
'''

print(caneca1.beber())
print(caneca1.encher())
print(f'{caneca1.nome} está: {caneca1.status}') # CHEIA

print()

print(caneca2.beber())
print(f'{caneca2.nome} está: {caneca2.status}') # VAZIA
