class VendaProduto:
    def __init__(self, quantidade:int, preco: float, id_venda:int, id_produto:int):
        self.quantidade = quantidade
        self.preco = preco
        self.id_venda = id_venda
        self.id_produto = id_produto


    def __repr__(self):
        return f"VendaProduto<< quantidade: {self.quantidade}, preco: {self.preco}, id_venda: {self.id_venda}, id_produto: {self.id_produto}"