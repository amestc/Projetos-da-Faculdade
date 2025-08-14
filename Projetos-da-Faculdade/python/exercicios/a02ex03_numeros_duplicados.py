# Retorne todos os números repetidos de uma lista de números
# Exemplo:
#   Entrada: [6, 1, 1, 7, 2 , 6, 1]
#   Saída Experada: [6, 1]

numeros = [6, 1, 1, 7, 2, 6, 1]
numeros_duplicados = []

for i in numeros:
    if numeros.count(i) > 1 and i not in numeros_duplicados:
        numeros_duplicados.append(i)

print(f'Números duplicados: {numeros_duplicados}')