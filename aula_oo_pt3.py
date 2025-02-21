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

print(Exemplo.somar(5, 3))#chamando o método estático sem precisar de uma instância







# 2 - pacotes:
# 3 - modelagem oo: