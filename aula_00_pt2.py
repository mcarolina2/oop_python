# Nessa aula estudados sobre os conceitos de construtores, destrutores e encapsulamento:

# construtores:é o método utilizado no momento da construção de objetos/instâncias : 
class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

pessoa1= Pessoa('carol', 21)
print(pessoa1.nome)
print(pessoa1.idade)

#Destruidores: método chamado quando um objeto está preste a ser destruido:
class MeuArquivo:
    def __init__(self, nomedoarquivo, modo):
        # Inicializa o objeto e tenta abrir o arquivo
        try:
            self.nomedoarquivo = nomedoarquivo
            self.modo = modo
            self.arquivo = open(nomedoarquivo, modo)  # Define o atributo corretamente
            print(f'Arquivo {nomedoarquivo} aberto em modo {modo}')
        except FileNotFoundError:
            print(f"Erro: O arquivo '{nomedoarquivo}' não foi encontrado.")
            self.arquivo = None  # Para evitar erros posteriores

    def read(self):
        # Lê o arquivo se ele estiver no modo de leitura
        if self.arquivo and 'r' in self.modo:
            return self.arquivo.read()
        else:
            print('Erro: O arquivo não está em modo de leitura ou não foi aberto.')

    def __del__(self):
        # Fecha o arquivo se ele foi aberto corretamente
        if self.arquivo:
            self.arquivo.close()
            print(f"Arquivo '{self.nomedoarquivo}' fechado automaticamente.")
        else:
            print(f"Nenhum arquivo para fechar.")

arquivo1 = MeuArquivo('meu_exemplo.txt', 'r')  
print(arquivo1.read())  

#Encapsulamento: permite que você agrupe dados (atributos) e comportamntos(métodos) dentro de uma classe para criar uma unidade coesa com metodo sque operam nesses dados.
class Thing:
    def __init__(self, public: str, *, protected: str = "protected", private: str = "private"):
        self.public = public         # Atributo público
        self._protected = protected # Atributo protegido (uso interno)
        self.__private = private    # Atributo privado (restrito)

    # Método público: Acessível de qualquer lugar
    def public_method(self):
        print(f"Public attribute: {self.public}")
        self._protected_method()  # Chamando um método protegido
        self.__private_method()   # Chamando um método privado

    # Método protegido: Convenção para uso interno ou subclasses
    def _protected_method(self):
        print(f"Protected attribute: {self._protected}")

    # Método privado: Restrito à própria classe
    def __private_method(self):
        print(f"Private attribute: {self.__private}")

# Instanciando a classe
thing = Thing(public="I'm public")
print(thing.public)  # Saída: I'm public # Acessando o atributo público
# Tentando acessar os atributos protegido e privado
print(thing._protected)  # Funciona, mas não é recomendado. Saída: protected

thing.public_method() # Chamando o método público

thing._protected_method()  # Funciona, mas não é recomendado.
# thing.__private_method()  # Erro: AttributeError



#ATIVIDADE: 
# Questão 1 : Implemente a versão da classe Student apresentada na aula teórica e crie atributos públicos:
class Student:
    SchoolName = 'UFPB' # exemplo de atributos classe , que possuiem o mesmo valor para todos os objetos da classe
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #acessando fora da classe
estudante1 = Student('helena', 18)
print(estudante1.SchoolName)
print(estudante1.name)
print(estudante1.age)

#Questão 2 : Crie a classe conta com os atributos privados abaixo. Pense em possíveis métodos para esta classe e implemente-os.
    #Atributos: numero, titular, saldo, limite
    #métodos: sacar, depositar, get e set (numero, titular) e getSaldo.
    
class Conta:
    def __init__(self,numero, titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo =saldo
        self.__limite= limite
    def getNumero(self):
        return self.__numero
    def setNumero(self, numero):
        self.__numero = numero
    def getTitular(self):
        return self.__titular
    def setTitular(self, titular):
        self.__titular = titular
    def getSaldo(self):
        return self.__saldo
    def setSaldo(self, saldo):
        self.__saldo = saldo
    def getLimite(self):
        return self.__limite
    def setLimite(self, limite):
        self.__limite = limite
    def sacar(self, valor):
        if valor <=self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo Insuficiente')
    def depositar(self,valor):
        self.__saldo += valor
            
con1 = Conta(896,'Maria', 1000,10000)
print(con1.getNumero())
print(con1.getTitular())
print(con1.getSaldo())
print(con1.getLimite())
con1.sacar(100)
print(con1.getSaldo())