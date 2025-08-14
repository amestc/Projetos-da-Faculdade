# Una duas aleatórias listas em uma só com ordenação decrescente de valores
# Exemplo:
#   Entrada: 
#       ListaA = [1, 9, 4 , 5, 7, 2, 1]
#       Listab = [3, 2, 7 , 8, 6]
#   Saída Experada: [9, 8, 7, 7, 6, 5, 4, 3, 2, 2, 1, 1]

lista_a = [1, 9, 4, 5, 7, 2, 1]
lista_b = [3, 2, 7, 8, 6]
uniao = lista_a + lista_b
uniao.sort(reverse=True)
print(f'Lista unida e ordenada: {uniao}')