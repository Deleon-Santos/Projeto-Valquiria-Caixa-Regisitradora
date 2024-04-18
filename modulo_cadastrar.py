import PySimpleGUI as sg
import json
carrinho=[]
cadastro_item={}
def novo_item():
    # abre os itens existentes do arquivo JSON
    with open("dados/bd.txt", 'r') as arquivo:
        dic = json.load(arquivo)
    
    titulos=[' cod ','     ean     ',"               Descrição           "," preço "]
    frame1=[[sg.Text("Descrição:", size=(50, 1)),sg.Text("Preço:", size=(10, 1))],
        [sg.InputText(background_color='White', key="-PRODUTO-", size=(25, 1), font=("Any", 18)),sg.P(),
         sg.InputText(background_color='White', key="-PRECO-", size=(5, 1), font=("Any", 18)),sg.P(),sg.Button("CADASTRAR", size=(12, 1))],
        [sg.Table(values=carrinho, headings=titulos, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="center",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=10, key="-TABELA-", row_height=20)],
            ]
    layout = [
        [sg.Text("", size=(20, 1))],
        [sg.P(),sg.Text("CADASTRAR ITEM", size=(20, 1), justification='center', font=("Any", 18,'bold')),sg.P()],
        [sg.Text("", size=(10, 1))],
         
        [sg.Frame('',frame1)],
        [sg.Text("", size=(10, 1))],
        [sg.P(),  sg.Button("SAIR", size=(10, 1),button_color='red'),sg.P()],
        [sg.Text("", size=(10, 1))],
    ]

    window = sg.Window("Cadastro de Itens", layout)
    while True:
        try:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "SAIR"):
                break
            if event == "CADASTRAR":
                material = values["-PRODUTO-"]
                codigo = len(dic) + 101  # conta os itens e adiciona "101"
                
                ean = 7890000000000 + codigo
                codigo = str(codigo)
                ean = str(ean) 
                prec = float(values["-PRECO-"])
                carrinho.append([codigo, ean, material, prec])
                window['-PRODUTO-'].Update('')
                window['-PRECO-'].Update('')

            cadastro_item = {"cod": codigo, "ean": ean, "item": material, "preco": prec}
            # Adicione o novo item ao dicionário
            dic.append(cadastro_item)
            with open("dados/bd.txt", 'w') as arquivo:

                json.dump(dic, arquivo, indent=4)
                window['-TABELA-'].update(values=carrinho)
       
        except ValueError:
            sg.popup("Informe valor numerico", title="Preço", font=("Any", 18))
    window.close()
