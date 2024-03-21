import PySimpleGUI as sg


pesquisa=[]
def pesquisar(dic):

    titulos=[" Cod ","     EAN     ","   Descrição do Produto  "]

    frame1=[[sg.Table(values=pesquisa, headings=titulos, max_col_width=10, auto_size_columns=True,
                display_row_numbers=False, justification="center",text_color="black",font=("Any",14),background_color="lightyellow", num_rows=10, key="-TABELA-", row_height=20)],]
    layout=[[sg.T("PESQUISA",size=(20,1),)],
            [sg.Frame("",frame1)],
            [sg.P(),sg.B('OK'),sg.P()],]

    window = sg.Window('PESQUISA POR ITEM', layout, finalize=True)  
    for item in dic:
        cod = item['cod']
        ean = item['ean']
        desc = item['item']
        pesquisa.append([cod, ean, desc])

    window['-TABELA-'].update(values=pesquisa)    
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            pesquisa.clear()
             
        
        if event =="OK":
            if values['-TABELA-']:
                linha_selecionada = values['-TABELA-'][0]
                escolha = pesquisa[linha_selecionada]
                return escolha[1],escolha[2] 
            
    window.close()   