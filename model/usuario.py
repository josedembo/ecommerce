class Usuario:
    def __init__(self, nome:str, email:str , senha:str, nome_de_usuario:str, endereco:str, id=None):
        self.nome = nome
        self.email = email
        self. senha = senha
        self.nome_de_usuario = nome_de_usuario
        self.endereco = endereco
        self.id = id
        

    def __repr__(self):
        return f"Usuario << id {self.id}, Nome: {self.nome}, email: {self.email}, nome_de_usuario: {self.nome_de_usuraio}, endereco: {self.endereco} >>"
    
        