class Funcionario():

    def __init__(self,nome,salario,porcentagem):
        self.nome = nome
        self.salario = salario
        self.porcentagem = porcentagem
    
    def aumentar_salario(self):
        porc = self.salario + ((self.salario * self.porcentagem) /100)
        return porc
