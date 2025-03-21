from  abc import abstractmethod, ABC # iniciando importando o método abstrato

# Nessa aula estudamos sobre Classe abstrata : é uma classe que não pode ser instanciada diretamente , contém metodos abstratos que deve ser obrigatoriamente 

class Animal(ABC):
    def __init__(self, imagem, cor, alimentacao, apetite):
        self.__imagem = imagem
        self.__cor = cor
        self.__alimentacao = alimentacao
        self.__apetite = apetite
       
       
    @property
    def imagem(self): #getter imagem com property
        return self.__imagem
    @imagem.setter
    def imagem(self,imagem): #setter imagem com property
        self.__imagem = imagem
    
    @property
    def cor(self): #getter cor com property
        return self.__cor
    
    def cor(self, cor): #setter cor com property
        self.__cor = cor
        
    @property
    def alimentacao(self): #getter alimentacao com property
        return self.__alimentacao
    
    def alimentacao(self, alimentacao): #setter alimentacao com property
        self.__alimentacao = alimentacao
        
    @property
    def apetite(self): #getter apetitet com property
        return self.__apetite
    
    def apetite(self, apetite): #setter apetitet com property
        self.__apetite = apetite
        
    @abstractmethod
    def comer(self):
        pass 
    
    def fazerRuido(self):
        print(f'sou um animal e estou fazendo meu ruído')
        
    def dormir(self):
        print(f'sou um animal e estou drmindo')

    @abstractmethod
    def passear(self):
        pass
        
class Canino(Animal):
    # chamando o construtor da superclasse(Animal)
    
    def passear(self):
        print('Sou um animal passeando!')
    
    @abstractmethod
    def comer(self):
        pass
    
class Cachorro(Canino):
    # chamando o construtor da superclasse(Canino)
    def comer(self):
        print('Sou um cachorro comendo')
    def fazerRuido(self):
        print('au au!')

#   Questão 2 : implemente o lobo
class Lobo(Canino):
    def comer(self):
        print('Sou um lobo comendo')
        
    def fazerRuido(self):
        print( 'auu auu!')
        #return super().fazerRuido()
    def passear(self):
        super().passear()
        print('Sou um lobo passeando')

dog = Cachorro("cachorro.png", "marrom", "carnivoro", "medio")
dog.comer()
dog.fazerRuido()

wolf = Lobo("lobo.png", "marrom", "carnivoro", "medio")
wolf.comer()
wolf.fazerRuido()
wolf.dormir() # um exemplo de herança
wolf.passear()


#   Questão 3 : 
class Veiculo(ABC):
    def __init__(self, placa, ano):
        self.__placa = placa
        self.__ano = ano

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    
    @property
    def ano(self):
       return self.__ano
        
    @ano.setter
    def ano(self, ano):
        self.__ano = ano
    
    @abstractmethod
    def exibirDados():
        pass 

class Caminhao(Veiculo):# classe concreta caminhão
    def __init__(self, placa ,ano ,eixos):
        super().__init__(placa, ano)
        self.__eixos = eixos
        
    @property
    def eixos(self):
        return self.__eixos

    def eixos(self, eixos):
        self.__eixos= eixos
    
    
    def exibirDados(self):
        print(f'Placa: {self.placa}\nAno: {self.ano}\nEixos: {self.__eixos}')

truck = Caminhao("ASX-2589", 2023, "9")
truck.exibirDados()

class Onibus(Veiculo):
    def __init__(self, placa, ano, assentos):
        super().__init__(placa, ano)
        self.assentos = assentos
        
    @property
    def assentos(self):
        return self.__assentos

    def assentos(self, assentos):
        self.__assentos= assentos
    
    def exibirDados(self):
        print(f'Placa: {self.placa}\nAno: {self.ano}\nAssentos: {self.assentos}')
        
bus= Onibus("A34JK", 2018, 40)
bus.exibirDados()
