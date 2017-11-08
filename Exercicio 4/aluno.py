class Alunos:

    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    
    def Estudar(self,estudo):
        self.tempoSemDormir = estudo+(self.tempoSemDormir)
        return self.tempoSemDormir


    def Dormir(self,dormir):
        self.tempoSemDormir = dormir-(self.tempoSemDormir)
        return self.tempoSemDormir

