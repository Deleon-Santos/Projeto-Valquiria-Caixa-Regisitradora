import PySimpleGUI as sg
import json
carrinho=[]
cadastro_item={}
def novo_item():
    # abre os itens existentes do arquivo JSON
    with open("comanda.txt", 'r') as arquivo:
        dic = json.load(arquivo)
    
    titulos=[' cod ','     ean     ',"               Descrição           "," preço "]
    frame1=[sg.Table(values=carrinho, headings=titulos, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="center",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=10, key="-TABELA-", row_height=20)],
            
    layout = [
        [sg.Text("", size=(20, 1))],
        [sg.Text("CADASTRAR ITEM", size=(50, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(20, 1))],
        [sg.Text("Descrição:", size=(10, 1)),sg.InputText(background_color='White', key="produto", size=(25, 1), font=("Any", 18)),
         sg.Text("Preço:", size=(10, 1)),sg.InputText(background_color='White', key="preco", size=(5, 1), font=("Any", 18))], 
        [sg.Frame('',frame1)],
        [sg.Text("", size=(20, 1))],
        [sg.Text("", size=(23, 1)), sg.Button("CADASTRAR", size=(18, 1)), sg.Button("SAIR", size=(18, 1),button_color='red')],
        [sg.Text("", size=(20, 1))],
    ]

    window = sg.Window("Cadastro de Itens", layout)
    while True:
        try:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "SAIR"):
                break
            if event == "CADASTRAR":
                material = values["produto"]
                codigo = len(dic) + 101  # conta os itens e adiciona "101"
                
                ean = 7890000000000 + codigo
                codigo = str(codigo)
                ean = str(ean) 
                prec = float(values["preco"])
                carrinho.append([codigo, ean, material, prec])
            

            cadastro_item = {"cod": codigo, "ean": ean, "item": material, "preco": prec}
            # Adicione o novo item ao dicionário
            dic.append(cadastro_item)
            with open("comanda.txt", 'w') as arquivo:

                json.dump(dic, arquivo, indent=4)
                window['-TABELA-'].update(values=carrinho)
            
            
        except ValueError:
            sg.popup("Informe valor numerico", title="Preço", font=("Any", 18))
    window.close()
