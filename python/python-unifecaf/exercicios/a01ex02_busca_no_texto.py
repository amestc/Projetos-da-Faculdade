# Busque no texto principal o valor digitado pelo usuário, 
# ao final retorne True se o valor for encontrado ou False 
# caso contrário. Deve ser analisado caractere por caractere. 
# Exemplo de entrada e saída:
#     Entrada do usuário: brasil
#     Texto: no brasil existem muitos lugares bonitos
#     Retorno experado: True

texto = 'no brasil existem muitos lugares bonitos'
busca = input('Digite o texto a ser buscado: ')

for i, c in enumerate(texto):
    if i + 1 <= len(texto):
        if c == busca[0]:
            if texto[i:i + len(busca)] == busca:
                print(True)

                
            
        
        