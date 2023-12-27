import PySimpleGUI as sg
data=["1","101","78919821101","arroz camil pct 5kg",1,20.20]
sg.theme("LightBlue3")

menu_layout = [["Novo", ["Nova Compra", "Novo Produto", "Pesquisar Produto"]],
               ["Totais", ["Venda Cupom", "Venda Total"]], ["Suporte", ["Ajuda", "Data"]]]

bloco_1=[   [sg.Text("CAIXA FECHADO", size=(70, 1), key='caixa', justification='center', font=("Any", 55, "bold"))],
             ]

bloco_2=[   [sg.Text('Código do Produto', size=(25, 1), font=("Any", 18)),sg.Text("", size=(32, 1)),sg.Text('Quantidade', size=(10, 1), font=("Any", 18))],
            [sg.InputText(background_color='White', size=(3,2 ), key='lanche1', font=("Any", 25)),
             sg.InputText(background_color='White', size=(14,2 ), key='lanche1', font=("Any", 25)),
             sg.Text("", size=(35, 1)),sg.InputText("1", size=(8, 2), key='qtd', font=("Any", 25))],
            [sg.Text('Código do Produto', size=(25, 1), font=("Any", 18))],
            [sg.InputText(size=(43, 2), key='descricao', font=("Any", 25))],]

bloco_3=[   [sg.Button('OK', size=(30,2)), sg.Text("", size=(32, 1)),sg.Button('DELETE', size=(30, 2))],
            [sg.Button('PAGAR', size=(30, 2)),sg.Text("", size=(32, 1)), sg.Button('VOLTAR', size=(30, 2))],
            ]

bloco_4=[   [sg.Image(filename="images.png",size=(780,210))],
         ]

frame1=[   
            [sg.Frame("",bloco_2)],
            [sg.Frame("",bloco_3)],
            [sg.Frame("",bloco_4)],
            


            ]

frame2=[   [sg.Table(values=data, headings=["Item", "Cod", "EAN","Descricao","QTD","Preco"], auto_size_columns=True, justification='right',size=(12,18), key='output')],]

layout = [  
            [sg.Menu(menu_layout)],
            [sg.Frame("",bloco_1)],
            [sg.Text(" ", size=(73, 1)), sg.Text(size=(23, 1), key="com", justification='right', font=("Any", 18))],
            
            [sg.Col(frame1),sg.Col(frame2)],
            [sg.Text("12 de outubro de 1233", size=(25, 1), key='data', font=("Any", 12)),
            sg.Text("DESENVOLVIDO POR:", size=(18, 1), font=("Any", 10)),
            sg.Text("linkedin.com/in/deleon-santos-1b835a290", size=(40, 1), key='LOG', font=("Any", 10)),
            sg.Text("", size=(10, 1)), sg.Text("SubTotal", size=(7, 2), font=("Any", 40)),
            sg.Text(size=(10, 2), key="subtotal", font=("Any", 40), justification='right')],]

window = sg.Window("NOVO PEDIDO", layout, resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Fechar"):
        # sg.popup("ENCERRAR",font=("Any", 18))
        break
    if event == "ok":
        # Adicionando uma linha vazia com strings vazias
        data.append(["", "", "", "", "", ""])
        window["output"].update(values=data)

window.close()