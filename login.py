import PySimpleGUI as sg
cadastro={'nome':'adm','senha':'1234',
          'nome':'Operador turno manha','senha':'1234',
          'nome':'Operador turno tarde','senha':'1234',}

col1=[
    [sg.Image(filename="111.png")],
]
col2=[
    [sg.T("Usuario"),sg.I(key='-USUARIO-')],
    [sg.T("Senha"),sg.I(key='-SENHA-',password_char='*')],
]
layout=[
    [sg.Col(col1),sg.VerticalSeparator(),sg.Col(col2)],
    [sg.B("OK"),sg.B('SAIR')],
    [sg.HorizontalSeparator()],
    [sg.B('SUPORTE')],
]

window = sg.Window("NOVO PEDIDO", layout,size=(800,250), resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Fechar"):
        # sg.popup("ENCERRAR",font=("Any", 18))
        break
    if event =='OK':
        usuario=values['-USUARIO-']
        senha=values['-SENHA-']
        for nome in cadastro:
            if usuario == nome['nome'] and senha == nome['senha']:
                sg.popup("logado")
                 
window.close()