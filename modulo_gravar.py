import json

def gravar(lista_cupom):
    
    # abre os itens existentes do arquivo JSON
    #try:    
    with open("gravar.txt", 'r') as arquivo:
        compra = json.load(arquivo)
    
        # Adicione o novo item ao dicionário
    compra.append(lista_cupom)
    with open("gravar.txt", 'w') as arquivo:

        json.dump(compra, arquivo, indent=4)  
    '''except :
        print('houve um erro inesparado')
        return'''
        
    
