# Nessa aula estudamos sobre Tratamento De Erros Usando Exceções:
# - são objetos especiais usados para representar erros em tempo de execução , todas as exceções são subclasses da classe exeption

# Criando uma classe de exceção:
class MinhaExcecao(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
class MinhaExcecao2(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return self.mensagem

#raise MinhaExcecao2("Erro!")


#testnado o try:
try:  
    raise MinhaExcecao2("Erro!") 
except MinhaExcecao as e1:
    print('Minha exceção1 ocorreu, valor: {}'.format(e1.valor))
except MinhaExcecao2 as e2:
    print('Minha exceção2 ocorreu, mensagem: ', e2.mensagem)
    
    
#Questão: Crie um classe TestaValidaNumero com um metodo "validaNumero(num)", que lança as seguintes exceções de acordo com o valor do parâmetro num:
#a) menor ou igual a 0: lança a exceção ValorAbaixoException;
#b) maior que 100 e menor que 1000: lança a exceção ValorAcimaException;
#c) maior ou igual a 1000: lança a exceção ValorMuitoAcimaException;
#d) Escreva o código das classes de exceção ValorAbaixoException, ValorAcimaException e ValorMuitoAcimaException.

class ValorAbaixoException(Exception):
    """Exeções para valores menoes ou iguais a 0"""
    pass
class ValorAcimaException(Exception):
    """Exeções para valores maiores que 100 e menoes que 1000"""
    pass
class ValorMuitoAcimaException(Exception):
    """Exeções para valores maiores ou iguais a 1000 """
    pass

class TestaValidaNumero(Exception):
    def validaNumero(self,num):
        """ """
        if num <= 0 :
           raise ValorAbaixoException("O valor está abaixo do permitido")
        elif  100< num < 1000: 
           raise  ValorAcimaException("O valor está acima do limite permitido")
        elif num >= 1000:
            raise ValorMuitoAcimaException("O valor está muito acima do permitido")

try:
    t= TestaValidaNumero()
    t.validaNumero(0)
except Exception as e:
    print(f"Erro: {e}")
