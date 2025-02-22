# nessa aula vimos um pouco dos diferentes paradigimas de progrmação e observações da linguagem python.

# Exemplos de códigos dos paradigmas imperativo/procedural: 
numeros =[1,2,3,4,5,6,7,8,9,10]
numeros_impares = []

for numero in numeros:
    if (numero % 2 != 0):
        numeros_impares.append(numero)
print(numeros_impares)


# Exemplos de códigos dos paradigmas declarativo/funcional:
numeros =[1,2,3,4,5,6,7,8,9,10]
numeros_impares = list(filter(lambda numero: numero % 2 != 0, numeros))

print(numeros_impares)
