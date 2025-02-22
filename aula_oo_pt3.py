# Nessa aula estudamos sobre:
 
# 1 - atributos e métodos estáticos:
    #atributos estáticos: são como variaveis globais dentro da classe.
    
class Matematica:
    PI = 3.14159  # Atributo estático

    @staticmethod
    def calcular_area_circulo(raio):
        return Matematica.PI * (raio ** 2)

print(Matematica.PI) # Acessando sem instanciar a classe
print(Matematica.calcular_area_circulo(5))

    #métodos estáticos: são definidos com o decorador '@staticmethod' e são úteis para funções auxiliares.  
class Exemplo:
    @staticmethod
    def multiplicar(a, b):
        return a * b

print(Exemplo.multiplicar(5, 3))#chamando o método estático sem precisar de uma instância

# 2 - modelagem oo:
    # definição; é um modelo de representação de sistemas de ocdigo que são baseados em coceitos de poo.
    #diagrama de classes: descreve os tipos de objetos entre eles e os varios tipos de relacionamentos. 
    
#questão: Escreva um programa que implemente a classe Estudante, que tem os métodos getNome, getNota, mostraNota e calculaMedia. Escreva um programa para testar sua classe.
#R:
class Estudante:
    def __init__(self,nome, nota):
        self.nome = nome
        self.nota = nota
    
    def getNome(self):
        return self.nome
    
    def getNota(self):
        return self.nota
    
    def mostraNota(self):
        print(f"A nota de {self.nome} é {self.nota}")
        
    def calculaMedia(self,nota):
        if len(notas) == 0:
            return 0
        return sum(notas) / len(notas) 
    
estudante1 =Estudante("Carol", 9.0)
print(estudante1.getNome())
print(estudante1.getNota())
estudante1.mostraNota()

#testanto calcular a média;
notas = [10,9.0,8,0,7.0]
media = estudante1.calculaMedia(notas)
print(f"A média das notas é {media:.2f}")