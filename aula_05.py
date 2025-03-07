## Nessa aula estudamos um pouco sobre decompositores
## definição : é uma função que embrulha outra função ,adicionando comportamentos antes ou depois da função original. 
## acontece da seguinte forma : ela recebe uma função como paramentro e retorna uma nova função modificada. 

## exemplo sem o decorador: 
def meu_decorador(funcao):
    def wrapper():
        print("antes da função")
        funcao()
        print("depois da função")
    return wrapper
def dizer_oi():
    print("oi")
dizer_oi_naodecorada=meu_decorador(dizer_oi) #decorador manual
dizer_oi_naodecorada()
print()

## exemplo com o decorador:
@meu_decorador
def dizer_oi_decorada():
    print("oi")

dizer_oi_decorada()