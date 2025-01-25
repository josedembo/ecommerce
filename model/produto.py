class Produto:
    def __init__(self, nome:str, quantidade:int, id_categoria:int, preco:float, descricao:str, foto=None, id=None):
        self.nome = nome
        self.quatidade = quantidade
        self.id_categoria = id_categoria
        self.preco = preco
        self.descricao = descricao
        self.foto = foto
        self.id = id

    def __repr__(self):
        return f"Produto<< id: {self.id}, nome: {self.nome}, quantidade: {self.quatidade}, preco: {self.preco}, descricao: {self.descricao}, foto: {self.foto} >>"