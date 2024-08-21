import PySimpleGUI as sg
import modulo_imprimir as imprimir
import modulo_arquivar as arquivar

pesquisa_cupom = []
pesquisa = []

def venda_cupom(lista_dados):
    titulos1 = ["    Cupom     ", "      Data     ","    Cliente    ","  Valor R$  "]
    titulos2 = ["Item", "COD","    EAN    ","Descrição do Produto","QTD","PUni R$","Preço R$"]

    layout1 = [
        [sg.Table(values=pesquisa, headings=titulos1, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="center", text_color="black", font=("Any", 11), background_color="lightyellow", num_rows=15, key="-TABELA1-", row_height=20)],
    ]

    layout2 = [
        [sg.Table(values=pesquisa_cupom, headings=titulos2, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="center", text_color="black", font=("Any", 11), background_color="lightyellow", num_rows=15, key="-TABELA-", row_height=20)],
    ]

    janela = [
        [sg.T("CNPJ ", size=(24, 1)), sg.T("Empresa ", size=(39, 1)), sg.T("Cliente")],
        [sg.I(key="-CNPJ-", size=(15, 1), font=("Any", 18), justification='right'),
         sg.I(key="-EMPRESA-", size=(24, 1), font=("Any", 18), justification='right'),
         sg.I(key="-CPF-", size=(15, 1), font=("Any", 18), justification='right')],
        
        [sg.T("Valor da Compra R$", size=(15, 1)), sg.T("Data da Compra", size=(29, 1)), sg.T("Operador", size=(31, 1)), sg.T("N° Cupom")],
        [sg.I(key="-VALOR-", size=(9, 1), font=("Any", 18), justification='right'),
         sg.I(key="-DATA-", size=(18, 1), font=("Any", 17), justification='right'),
         sg.I(key="-USUARIO-", size=(18, 1), font=("Any", 19), justification='right'),
         sg.I(key="-CUPOM-", size=(6, 1), font=("Any", 18), justification='right')],
        
        [sg.P(), sg.B("PESQUISAR", size=(10, 1)), sg.B("IMPRIMIR", size=(10, 1)), sg.B("SAIR", size=(10, 1), button_color='red')],
        [sg.TabGroup([
            [sg.Tab("Cupons", layout1)],
            [sg.Tab("Itens", layout2)],
        ])],
    ]

    window = sg.Window("VENDA CUPOM", janela, finalize=True, resizable=True) 

    for item in lista_dados:
        cupom, data, cliente , valor, usuario, cnpj, razao_social = item[0],item[1],item[3],(f"{float(item[2]):.2f}"),item[6],item[4],item[5]
      
        pesquisa.append([cupom, data, cliente, valor])
        window['-TABELA1-'].update(values=pesquisa)
    pesquisa.clear()
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "SAIR"):
            pesquisa_cupom.clear()
            break

        if event == "-TABELA1-":
            selected_row_index = values["-TABELA1-"][0]  
            selected_row = pesquisa[selected_row_index]  # Pega os dados da linha selecionada
            cupom = selected_row[0]  
            window["-CUPOM-"].update(cupom[0])  
            continue

        if event == "PESQUISAR":
            cupom = values["-CUPOM-"]
            if not cupom:
                sg.popup_error('Cupom não localizado', font=('Any', 12), title='ERRO')
                continue
            else:
                try:
                    d=False
                    for dado in lista_dados:
                        if dado[0] == int(cupom):
                            d = dado
                            
                            #mostra as informações em campos especificos da janela
                            window["-CUPOM-"].update(d[0])
                            window["-DATA-"].update(d[1])
                            window["-USUARIO-"].update(d[6])
                            window["-CNPJ-"].update(d[4])
                            window["-CPF-"].update(d[3])
                            window["-VALOR-"].update(f"{float(d[2]):.2f}")#formatação para apresentar os vlores com 2 digitos apos a vigula
                            window["-EMPRESA-"].update(d[5])
                            
                            pesquisa_cupom.clear()#limpa a lista para evitar concatenar
                            lista_cupom=arquivar.lista_item_por_carrinho(cupom)
                            for compra in lista_cupom:
                                pesquisa_cupom.append(compra[1:])

                            window["-TABELA-"].update(values=pesquisa_cupom)
                            break
                    if not d:
                        sg.popup_error('Cupom Não Localizado', font=('Any', 12), no_titlebar=True)
                        window["-TABELA-"].update('')
                except ValueError:
                    sg.popup_error('Cupom Invalido!', font=('Any', 12), title='ERRO')
                

        elif event == 'IMPRIMIR':
            informacao='\n' #Composicao da string formatada de dados de venda
            informacao += f"Razão Social: {razao_social}\n"
            informacao += f"End: AV. Boa Vista n-1012 Santa Rosa/SP\n"
            informacao += f"CNPJ: {cnpj}  IE : 07.112.888/000-00\n\n"
            informacao += f"Data: {data}\n" 
            informacao += f"Cliente: {cliente}\n"               
            
            informacao += f"Operador: {usuario}\n"
            informacao += f"Cupom R$: {cupom}\n"
            informacao += f"Valor: {valor}"

            gerar_pdf = imprimir.create_pdf(informacao, pesquisa_cupom,"impressora.pdf")#Chamda da funcao "PDF" com informacao da venda e dados do cupom
            if gerar_pdf:
                sg.popup("PDF Salvo", font=('Any', 12), title='IMPRIMIR PDF')
            else:
                sg.popup_error("Erro ao imprimir", font=('Any', 12), title='ERRO')

    window.close()

