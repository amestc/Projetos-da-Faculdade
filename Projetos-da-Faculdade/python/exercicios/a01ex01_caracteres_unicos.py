# Leia todos os caracteres de uma string e retorne todos os 
# caracteres que não possuírem par. Por exemplo:
#     aabcc  => b
#     aabbccaafbbbaaacaa  => fc
#     aabbcc => None

texto = str('aabbccaafbbbaaacaa')
igual = int(0)
sozinhos = []

for i, c in enumerate(texto):
    if i + 1 < len(texto):
        if c == texto[i + 1]:
            igual += 1
        elif igual > 0:
            igual = 0
        elif igual == 0 and c in sozinhos:
            sozinhos.remove(c)
        else:
            sozinhos.append(c)
            igual = 0
print(sozinhos)
    