#iniciamos com os conceitos iniciais de programação orientada a objetos 

# definindo uma classe (é uma estrutura que define atributos(dados) e métodos(funções) que os objetos baseados nela terão): 
 
class Dog: # exemplo 1 
    species ="canis familiaris" # exemplo de atributo de calsse 
    
    def __init__(self, nome, idade): # exemplo de atributo de instância
        self.nome = nome
        self.idade = idade

# ATIVIDADE: 
#Crie uma classe produto com os atributos nome, categoria, preço e quantidade. A seguir, implemente os métodos get e set de cada atributo. Teste a classe criando dois objetos e sugira um novo método que seja útil para a classe.
class Produto(): 
    def __init__(self, nome, categoria, preco, quantidade): 
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade
        
    def getNome(self):
        return self.nome
    def getCategoria(self):
        return self.categoria
    def getPreco(self):
        return self.preco
    def getQuantidade(self):
        return self.quantidade
    def setNome(self, nome):
        self.nome = nome
    def setCategoria(self, categoria):
        self.categoria = categoria
    def setPreco(self, preco):
        self.preco = preco
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade
    def calcularPrecoTotal(self):
        return self.getPreco() * self.getQuantidade()
    
biscoito = Produto('treloso','alimento', 1.60 , 2)
refrigerante = Produto('coca_zero', 'bebida', 6 , 1)
    
print(f'A categoria é {biscoito.getCategoria()}')
print(f'o preço total é {biscoito.calcularPrecoTotal()}')
    
# Crie a classe Veículo com os atributos cor, marca, número da placa e os métodos get e set de cada um. A seguir, teste sua classe.

class Veiculo:
    def __init__(self, cor, marca, placa):
        self.cor = cor
        self.marca = marca
        self.placa = placa
    
    def getCor(self):
        return self.cor
    def getMarca(self):
        return self.marca
    def getPlaca(self):
        return self.placa
    def setCor(self, cor):
        self.cor = cor
    def setMarca(self, marca):
        self.marca = marca
    def setPlaca(self, placa):
        self.placa = placa

civic = Veiculo('preto','honda', 'mcf2f86')
print(f'a cor do civic é {civic.getCor()}')
