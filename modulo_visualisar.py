import PySimpleGUI as sg

pesquisa_cupom=[]

def venda_cupom(lista_cupom):
    titulos = ["Item","Cod","    EAN    "," Descrição do Produto","QTD","PUni R$","Preço R$"]
    layout=[[sg.Push(),sg.T("VENDA CUPOM",font=("any",20,'bold')),sg.Push()],
            [sg.T("CNPJ Empresa",size=(33,1)),sg.T("CPF Cliente",size=(34,1)),sg.T("N° Cupom")],
            [sg.I(key="-CNPJ-",size=(15,1),font=("Any",18)),sg.P(),sg.I(key="-CPF-",size=(15,1),font=("Any",18)),sg.P(),sg.I("1",key="-CUPOM-",size=(6,1),font=("Any",18))],
            [sg.T("Valor da Compra",size=(16,1)),sg.T("Data da Compra",size=(29,1)),sg.T("Operador")],
            [sg.I(key="-VALOR-",size=(10,1),font=("Any",18)),sg.I(key="-DATA-",size=(18,1),font=("Any",18)),sg.I(key="-USUARIO-",size=(18,1),font=("Any",19))],
            [sg.Table(values=pesquisa_cupom, headings=titulos, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="right",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=15, key="-TABELA-", row_height=20)],
            [sg.B("PESQUISAR",size=(10,1)),sg.B("SAIR",size=(10,1))],
    ]  
    window = sg.Window("VENDA CUPOM",layout,finalize=True)                                                      
    while True:
        try:
            event,values = window.read()
            if event in (sg.WIN_CLOSED,"SAIR"):
                break
            cupom=values["-CUPOM-"]
            if not cupom:
                sg.popup("Digite o valor da pesquisa")
                    
                continue
            if event=="PESQUISAR":
                pesquisa_cupom.clear()
            
                
                print(f"o numero do cupos{cupom}")
                
                for indice,compra in enumerate(lista_cupom):
                    if indice  == int(cupom):
                        pesquisa_cupom.append(compra)
                        print(pesquisa_cupom)
                        window["-TABELA-"].print(values=pesquisa_cupom) 
                        #window["-TABELA-"].update(values=compra)   
                        l=len(pesquisa_cupom)
                        print(l)
                        indice +1            
                        break
        except:
            sg.Text("Não Encontrado!", font=("Any", 18))           

    window.close()