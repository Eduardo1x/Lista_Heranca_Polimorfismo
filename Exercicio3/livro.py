from main import *

livro = Livro(input('Qual o nome do livro? :'),

int(input("Qual a quantidade de paginas desse livro? :")),

input("Qual o autor desse livro?"),

int(input("Qual o preco desse livro? ")))

print("O preço é R${}" .format(livro.get_preco()))

livro.set_preco(int(input("Quer mudar o preco ? Digite o novo:")))

print("O novo preço é R${}" .format(livro.get_preco()))

