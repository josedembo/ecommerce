class Categoria:
    def __init__(self, nome:str, id=None):
        self.nome = nome
        self.id = id

    def __repr__(self):
        return f"Categoria<< id: {self.id}, nome: {self.nome}>>"