import PySimpleGUI as sg
import modulo_gravar as imprimir

pesquisa_cupom=[]
def venda_cupom(lista_cupom,lista_dados,usuario,valor_pagar):

    titulos = ["Item", "COD","    EAN    "," Descrição do Produto","QTD","PUni R$","Preço R$"]
    layout=[[sg.Push(),sg.T("VENDA CUPOM",font=("any",20,'bold')),sg.Push()],
            [sg.T("CNPJ Empresa",size=(42,1)),sg.T("CPF Cliente",size=(42,1)),sg.T("N° Cupom")],
            [sg.I(key="-CNPJ-",size=(15,1),font=("Any",18),justification='right'),sg.P(),sg.I(key="-CPF-",size=(15,1),font=("Any",18),justification='right'),sg.P(),sg.I("1",key="-CUPOM-",size=(6,1),font=("Any",18),justification='right')],
            [sg.T("Valor da Compra",size=(16,1)),sg.T("Data da Compra",size=(29,1)),sg.T("Operador")],
            [sg.I(key="-VALOR-",size=(10,1),font=("Any",18),justification='right'),sg.I(key="-DATA-",size=(18,1),font=("Any",18),justification='right'),sg.I(key="-USUARIO-",size=(18,1),font=("Any",19),justification='right')],
            [sg.Table(values=pesquisa_cupom, headings=titulos, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="center",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=15, key="-TABELA-", row_height=20)],
            [sg.P(),sg.B("PESQUISAR",size=(10,1)),sg.P(),sg.B("SAIR",size=(10,1),button_color='red'),sg.P(),sg.B("IMPRIMIR",size=(10,1)),sg.P()],
    ]  
    window = sg.Window("VENDA CUPOM",layout,finalize=True)                                                      
    while True:
        #try:
        event,values = window.read()
        if event in (sg.WIN_CLOSED,"SAIR"):

            break
        cupom=values["-CUPOM-"]
        if not cupom:
            sg.popup("Digite o valor da pesquisa")     
            continue

        if event == "PESQUISAR":
            for dado in (lista_dados):
                if dado[0] == int(cupom):
                    d=dado 
                    window["-CUPOM-"].update(d[0])                      
                    window["-DATA-"].update(d[1])
                    window["-USUARIO-"].update(d[2])
                    window["-CNPJ-"].update(d[3])
                    window["-CPF-"].update(d[4])
                    window["-VALOR-"].update(f"{valor_pagar:.2f}")
                    
                    for compra in lista_cupom:
                        if compra[0] == int(cupom):
                            pesquisa_cupom.clear()
                            pesquisa_cupom.extend(compra[1:])
                            window["-TABELA-"].update(values=pesquisa_cupom)
                            break
        elif event == 'IMPRIMIR':
            cnpj = values["-CNPJ-"]
            data = values["-DATA-"]
            cupom = values["-CUPOM-"]
            cpf = values["-CPF-"]
            valor = values["-VALOR-"]
            informacao =f"=============================================\n"
            informacao += f"Razão Social: .........................................TEM DE TUDO ME\n"
            informacao += f"END: ..........................AV. Boa Vista n-1012 Santa Rosa/SP\n\n"
            informacao += f"CNPJ: .....................{cnpj} IE : 07.112.888/000-00\n"
            informacao += f"Data: {data}                Cliente: {cpf}\n"
            informacao += f"CUPOM: 000{cupom}\n"                
            informacao += f"Valor: {valor}\n"
            informacao += f"Operador : {usuario}\n"
            informacao+=f"==============================================\n"
            print(informacao)
            
            resp=imprimir.imprimir(informacao,pesquisa_cupom)
            if resp ==True:
                sg.popup("PDF Salvo")
            else:
                sg.popup("erro ao imprimir")
        '''except Exception as e:
            print(f"Erro: {e}")
            sg.popup("houve um erro e o resultaado não foi exibido.")
            continue'''

    window.close()