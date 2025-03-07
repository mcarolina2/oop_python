# Nessa aula estudamos sobre o conceito de polimorfismo:

#relembrando a criação/declaração de objetos :
class Animal:
    def __init__(self,nome, som):
        self.nome = nome 
        self.som = som
        
    def faca_som(self): 
        print(f'{self.som} está fazendo o som')

#declaração e instanciação:
animal1 =Animal("cachorro", "au au")
animal2 =Animal("gato", "miau miau")

#Acesso a atributos e métodos:
print(animal1.nome)
animal2.faca_som()



#Testando o duck typing:
class Pato:
    def fazer_som(self):
        return "Quack!"

class Carro:
    def fazer_som(self):
        return "Vrum vrum!"

def executar_som(obj):
    print(obj.fazer_som())

# Uso
p = Pato()
c = Carro()

executar_som(p)  # Saída: Quack!
executar_som(c)  # Saída: Vrum vrum!