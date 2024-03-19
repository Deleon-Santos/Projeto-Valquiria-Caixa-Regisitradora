import PySimpleGUI as sg


carrinho=[]
def pesquisar(dic):

    titulos=[" Cod ","    EAN    ","   Descrição do Produto  "]

    frame1=[[sg.Table(values=carrinho, headings=titulos, max_col_width=10, auto_size_columns=True,
                display_row_numbers=False, justification="center",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=25, key="-TABELA-", row_height=20)],]
    layout=[[sg.T("PESQUISA",size=(20,1),)],
            [sg.Frame("",frame1)],
            [sg.P(),sg.B('OK'),sg.P()],]

    window = sg.Window('PESQUISA POR ITEM', layout, finalize=True)  
    for item in dic:
        cod = item['cod']
        ean = item['ean']
        desc = item['item']
        carrinho.append([cod, ean, desc])

    window['-TABELA-'].update(values=carrinho)    
    
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "SAIR"):
            sg.popup("ENCERRAR",font=("Any", 18))
            carrinho.clear()
            break 
        
        if event =="OK":
            if values['-TABELA-']:
                linha_selecionada = values['-TABELA-'][0]
                escolha = carrinho[linha_selecionada]
                return escolha[1],escolha[2] 
            
    window.close()   