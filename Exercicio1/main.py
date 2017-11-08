from triangulos import Triangulo



lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

instancia_triangulo = Triangulo(lado1,lado2,lado3)

resultado1 = instancia_triangulo.calc_perimetro()
resultado2 = instancia_triangulo.get_maior()

print(resultado1)
print(resultado2)


