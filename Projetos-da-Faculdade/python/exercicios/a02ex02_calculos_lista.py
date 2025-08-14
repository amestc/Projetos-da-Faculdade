# Dada uma lista de números, calcule:
#   - a soma de todos os números
#   - a média de todos os números
#   - O maior número
#   - o menor número 

numeros = [10, 20, 30, 40, 50]

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')