# Retorne todos os números exitentes em ambas as listas
# Exemplo:
#   Entrada: 
#       ListaA = [4, 9, 3 , 7, 8]
#       Listab = [9, 5, 4 , 2, 1]
#   Saída Experada: [9, 4]

lista_a = [4, 9, 3, 7, 8]
lista_b = [9, 5, 4, 2, 1]
intersecao = []

for i in lista_a:
    if i in lista_b and i not in intersecao:
        intersecao.append(i)
print(f'Interseção: {intersecao}')