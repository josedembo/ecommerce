class Venda:
    def __init__(self, id_usuario:int, data_hora:str, id=None ):
        self.id = id
        self.id_usuario = id_usuario
        self.data_hora = data_hora

    def __repr__(self):
        return f"Venda<< id: {self.id}, id_usuario: {self.id_usuario}, data_hora: {self.data_hora}"