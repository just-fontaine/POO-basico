

class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


    def exibir(self):
        print(self.nome, self.email)


    def chamar_exibir(self):
        self.exibir()



guilherme = Cliente('Guilherme', '@gmail.com')

guilherme.chamar_exibir()
