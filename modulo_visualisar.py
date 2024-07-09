import PySimpleGUI as sg
import modulo_imprimir as imprimir

pesquisa_cupom = []
pesquisa = []

def venda_cupom(lista_cupom, lista_dados, usuario):
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

    pesquisa.clear()
    for item in lista_dados:
        cupom = item[0]
        data = item[1]
        cliente = item[4]
        valor = item[5]
        pesquisa.append([cupom, data, cliente, valor])
        window['-TABELA1-'].update(values=pesquisa)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "SAIR"):
            pesquisa_cupom.clear()
            break

        if event == "-TABELA1-":
            selected_row_index = values["-TABELA1-"][0]  # Pega o índice da linha selecionada
            selected_row = pesquisa[selected_row_index]  # Pega os dados da linha selecionada
            cupom = selected_row[0]  # Pega o valor do cupom da linha selecionada
            window["-CUPOM-"].update(cupom[0])  # Atualiza o campo -CUPOM- com o valor do cupom
            continue

        if event == "PESQUISAR":
            cupom = values["-CUPOM-"]
            if not cupom:
                sg.popup_error('Cupom não localizado', font=('Any', 12), title='ERRO')
                continue
            else:
                try:
                    for dado in lista_dados:
                        if dado[0] == int(cupom):
                            d = dado
                            
                            window["-CUPOM-"].update(d[0])
                            window["-DATA-"].update(d[1])
                            window["-USUARIO-"].update(d[2])
                            window["-CNPJ-"].update(d[3])
                            window["-CPF-"].update(d[4])
                            window["-VALOR-"].update(d[5])
                            window["-EMPRESA-"].update(d[6])
                        
                            for compra in lista_cupom:
                                if compra[0] == int(cupom):
                                    pesquisa_cupom.clear()
                                    pesquisa_cupom.extend(compra[1:])
                                    window["-TABELA-"].update(values=pesquisa_cupom)
                                    break
                except ValueError:
                    sg.popup_error('Cupom Invalido!', font=('Any', 12), title='ERRO')
                except:
                    sg.popup_error('Cupom não localizado', font=('Any', 12), title='ERRO')

        elif event == 'IMPRIMIR':
            if not values['-CNPJ-'] or not values["-DATA-"] or not values["-CUPOM-"] or not values["-CPF-"] or not values["-VALOR-"]:
                sg.popup_error('Cupom Invalido!', font=('Any', 12), title='ERRO')
            else:
                cnpj = values["-CNPJ-"]
                data = values["-DATA-"]
                cupom = values["-CUPOM-"]
                cpf = values["-CPF-"]
                valor = values["-VALOR-"]
                informacao = f"========================================================\n"
                informacao += f"Razão Social:      ........................................................ TEM DE TUDO ME\n"
                informacao += f"END:      ......................................... AV. Boa Vista n-1012 Santa Rosa/SP\n\n"
                informacao += f"CNPJ:         ................................ {cnpj}  IE : 07.112.888/000-00\n"
                informacao += f"Data:     {data}                              Cliente:  {cpf}\n"
                informacao += f"CUPOM:  000{cupom}\n"                
                informacao += f"Valor:  {valor}\n"
                informacao += f"Operador: {usuario}\n"
                informacao += f"========================================================\n"
                print(informacao)
                
                gerar_pdf = imprimir.pdf(informacao, pesquisa_cupom)
                if gerar_pdf:
                    sg.popup("PDF Salvo", font=('Any', 12), title='IMPRIMIR PDF')
                else:
                    sg.popup_error("Erro ao imprimir", font=('Any', 12), title='ERRO')

    window.close()

# Exemplo de chamada à função venda_cupom
# lista_cupom = ...  # Substitua pelo seu código para carregar a lista de cupons
# lista_dados = ...  # Substitua pelo seu código para carregar a lista de dados
# venda_cupom(lista_cupom, lista_dados, "Operador Exemplo")
