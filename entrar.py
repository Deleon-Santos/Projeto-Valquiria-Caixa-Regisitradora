"""Projeto Valquíria
Aplicação baseada em caixa registradora do tipo comercio do seguimento varejo alimentos"""

import PySimpleGUI as sg
import modulo_registrar as vendas
import json



try: # Executa a abertura do BD em .txt com itens cadastrados
    with open('dados/usuarios.txt', 'r') as bd:
        dados_usuario = json.load(bd)
except FileNotFoundError:
    sg.popup("O arquivo 'badosdUsuario.txt' não foi encontrado. Verifique o caminho ou crie o arquivo.")

sg.LOOK_AND_FEEL_TABLE['MyCreatedTheme'] = {
    'BACKGROUND': '#483D8B', 
    'TEXT': '#F0FFF0', 
    'INPUT': '#DCDCDC', 
    'TEXT_INPUT': '#000000', 
    'SCROLL': '#99CC99', 
    'BUTTON': ('#ffffff', '#6A5ACD'), 
    'PROGRESS': ('#D1826B', '#CC8019'), 
    'BORDER': 4, 
    'SLIDER_DEPTH': 4,  
    'PROGRESS_DEPTH': 1, } 
sg.theme('MyCreatedTheme') # Prsonaliza a interface grafica com um tema especifico

lista_operadores=['Administrador','Operador do Turno 1','Operador do Turno 2']
lista_empresas=['Tem De Tudo ME']

col1=[
    [sg.Image(filename="imagem/imagem_login.png",size=(392,267))],]

col2=[
    [sg.T("Empresa",font=('any',12))],
    [sg.DD(default_value="Tem De Tudo ME",values=lista_empresas,size=(21,1),font=('any',17),key='-EMPRESA-')],
    [sg.T("Usuario",font=('any',12))],
    [sg.DD(default_value="Administrador",values=lista_operadores,size=(21,1),font=('any',18),key='-USUARIO-')],
    [sg.T("Senha  ",font=('any',12))],
    [sg.I('1234',key='-SENHA-',size=(21,1),font=('any',18),password_char='*')],
    [sg.T("",font=('Ani',1))],
    [sg.CalendarButton("Data",font=('Any',12),size=(4,1),close_when_date_chosen=True,target="-DATA-",location=(900,500),no_titlebar=False),
        sg.Input('2024-03-21 17:41:22',key="-DATA-",font=('any',16),size=(16,1))],
    [sg.T("",font=('Ani',1))],     ]

layout=[
    
   [sg.Frame('',[ 
       [sg.Col(col1),sg.VerticalSeparator(),sg.Col(col2)]])],
    [sg.T('VALQUIRIA.com'),sg.P(),sg.B("OK", tooltip='o:79',font=('any',10,'bold'),size=(9,1)),
        sg.B('SAIR',tooltip='Escape:27',font=('any',10,'bold'),size=(9,1),button_color='red'),
        sg.B('SUPORTE',tooltip='s:83',font=('any',10,'bold'),size=(10,1))] ,     ]

window = sg.Window("LOGIN VENDAS", layout,size=(740,365),finalize=True,return_keyboard_events=True,no_titlebar=False,titlebar_icon="img5.ico")
 
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "SAIR",'Escape:27'):
        break

    if event =='OK' or event =='o:79':      
        
        usuario,senha,data,empresa = values['-USUARIO-'],values['-SENHA-'],str(values['-DATA-']),values['-EMPRESA-']
        
        if not usuario or not senha or not data or not empresa :
            sg.popup_error("Usuario, Senha ou Data\nnão devem ser nulos",font=('Any',12))
            continue
        else:
            try:
                autenticado = False  # Variável para controlar a autenticação
                for user in dados_usuario:
                    if user['nome'] == usuario and user['senha'] == senha:
                        window.close()
                        vendas.sistema(usuario, data, empresa)
                        autenticado = True
                        break
                
                if not autenticado:
                    sg.popup_error('Usuário ou Senha Incorretos', font=('Any', 12), no_titlebar=True)

            except Exception as e:
                sg.popup(f"Erro inesperado:\n {str(e)}", font=('Any', 12), no_titlebar=True)
                print(e)
                
    elif event in ('SUPORTE','s:83'):
        try:
            with open('dados/usuarios.txt', 'r') as legenda:# Leitura das informações de suporte ao usuario
                arquivo = legenda.read()
                sg.popup_scrolled(arquivo, title="AJUDA")
        except FileNotFoundError:
            sg.popup("O arquivo 'comanda.txt' não foi encontrado.\n  Verifique o caminho ou crie o arquivo.",font=('Any',12),no_titlebar=True)
   
        
                    
window.close()