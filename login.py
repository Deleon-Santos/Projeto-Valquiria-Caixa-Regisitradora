import PySimpleGUI as sg
import vendas
l=['Administrador','Operador1','Operador2']
cadastro=[
        {'nome':'Administrador','senha':'1234'},
        {'nome':'Operador1','senha':'1234'},
        {'nome':'Operador2','senha':'1234'},]

col1=[
    [sg.Image(filename="imagem_login.png",size=(392,267))],
]
col2=[
    [sg.T("Usuario",font=('any',18)),sg.DD(values=l,size=(20,1),font=('any',18),key='-USUARIO-')],
    [sg.T("Senha  ",font=('any',18)),sg.I(key='-SENHA-',size=(20,1),font=('any',18),password_char='*')],
    [sg.Push(),sg.CalendarButton("Data",font=('any',12),size=(5,1),close_when_date_chosen=True,target="-DATA-",location=(0,0),no_titlebar=False),
    sg.Input(key="-DATA-",font=('any',18),size=(17,1)),sg.Push()],
    
]
layout=[
    [sg.Push(),sg.T('ENTRAR EM VENDAS',font=('Any',30)),sg.P()],
    [sg.Col(col1),sg.VerticalSeparator(),sg.Col(col2)],
    [sg.P(),sg.B("OK",font=('any',18),size=(10,1)),sg.P()],
    [sg.HorizontalSeparator()],
    [sg.P(),sg.B('SAIR',font=('any',18),size=(10,1),button_color='red'),sg.P(),sg.B('SUPORTE',font=('any',18),size=(10,1)),sg.P()]
]

window = sg.Window("NOVO PEDIDO", layout,size=(800,450))
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "SAIR"):
        # sg.popup("ENCERRAR",font=("Any", 18))
        break
    if event =='OK':
        usuario=values['-USUARIO-']
        print(usuario)
        senha=values['-SENHA-']
        data=str(values['-DATA-'])
        
        if not usuario or not senha or not data:
            sg.popup("Usuario, senha e Data não devem ser nulos")
            continue
        else:
            for user in cadastro:
                if user['nome']==usuario  and user['senha']== senha:
                    sistema=vendas.sistema(usuario,data)
            sg.popup_error('Inserir Usuario e Senha para entrar')       
            continue
    elif event=='SUPORTE':
        sg.popup_scrolled('USUARIO: Operador1\nSENHA: 1234',title="Senhas") 
        continue            
window.close()