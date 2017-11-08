class Triangulo:

    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calc_perimetro(self):
        soma_perimetro = self.ladoA+self.ladoB+self.ladoC
        return soma_perimetro

    def get_maior(self):
        maior = 0
        if(self.ladoA >= self.ladoB) and (self.ladoA >= self.ladoC):
            maior = self.ladoA
        elif (self.ladoB >= self.ladoA) and (self.ladoB >= self.ladoC):
            maior = self.ladoB
        else:
            maior = self.ladoC
        return maior
    