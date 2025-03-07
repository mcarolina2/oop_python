# Nessa aula estudamos sobre os conceitos de herança e composição 
# composição (ou delegação): é a criação de uma nova classe a partir das instâncias de outra classe existente.
# exemplo de composição (exemplo da aula) :
class Data:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

class Hora:
    def __init__(self, hora):
        self.hora = hora

    def __str__(self):
        return self.hora

class DataHora:
    def __init__(self, data, hora):
        self.estaData = Data(data)  # Instância de Data
        self.estaHora = Hora(hora)  # Instância de Hora

    def __str__(self):
        return f"{self.estaData} {self.estaHora}"

data_hora = DataHora("27/12/2023", "12:53")
print(data_hora)


#herança simples: é uma subclasse(classe filha) que herdar atributos e métodos de uma superclasse(classe mãe):
  #Exemplo (exemplo da aula):
class Veiculo:
    def __init__(self, nome, cor, ano, velocidade):
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10

class Conversivel(Veiculo):  # Herda de Veiculo
    def __init__(self, nome, cor, ano, velocidade, teto):
        super().__init__(nome, cor, ano, velocidade)
        self.teto = teto

    def subir_teto(self):
        self.teto = True

    def descer_teto(self):
        self.teto = False

c1 = Conversivel("Honda civic", "Cinza", 2016, 80, True)
c1.acelerar()
print(c1.velocidade) 


#herança múltipla: é uma subclasse(classe filha) que pode herdar atributos e métodos de varias superclasses(classes mães):
  # Exemplo(exemplo da aula):
class Autenticavel:
    def autentica(self, senha):
        return senha == "1234"

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

class Gerente(Funcionario, Autenticavel):  # Herda de duas classes
    pass

g = Gerente("Carlos")
print(g.autentica("1234")) 
