def arquivar(lista_cupom):    
    try:
        with open('dados/bd_vendas.txt', 'r') as arquivo_vendas:# Seu código para ler o arquivo
            bd_vendas = arquivo_vendas.read()
            
            bd_vendas.extend(lista_cupom)
            
        with open("dados/bd.vendas", 'w') as arquivo_vendas:
            arquivo_vendas.write(bd_vendas)
                            

                
    except FileNotFoundError:
        return False