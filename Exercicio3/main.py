class Livro():
    
    def __init__(self, nome, qtd_pag,autor,preco):
        self.nome = nome
        self.qtd_pag = nome
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco
        return novo_preco