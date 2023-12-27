import PySimpleGUI as sg
data=[]
table=[]
sg.theme("DarkBlue1")

visor  =[[sg.Input("0", size=(18, 1), font=("Any", 30, "bold"), key="out", justification='right')],]

numeros=[[sg.Button("7", size=(7,3), key="7", font="bold"), sg.Button("8", size=(7, 3), key="8", font="bold"), sg.Button("9", size=(7, 3), key="9", font="bold")],
        [sg.Button("4", size=(7, 3), key="4", font="bold"), sg.Button("5", size=(7, 3), key="5", font="bold"), sg.Button("6", size=(7, 3), key="6", font="bold")],
        [sg.Button("1", size=(7, 3), key="1", font="bold"), sg.Button("2", size=(7, 3), key="2", font="bold"), sg.Button("3", size=(7, 3), key="3", font="bold")],
        [sg.Button("+/-", size=(7, 3), key="+/-", font="bold"), sg.Button("0", size=(7, 3), key="0", font="bold"), sg.Button(",", size=(7, 3), key=".", font="bold")],]
    

bloco1 =[[sg.Button("<", size=(6, 3), font="bold", key="<")],
        [sg.Button("x", size=(6, 3), font="bold", key="*")],
        [sg.Button("-", size=(6, 3), font="bold", key="-")],
        [sg.Button("+", size=(6, 3), font="bold", key="+")],]

bloco2 =[[sg.Button("C", size=(7, 3), font="bold", key="c")],
        [sg.Button("/", size=(7, 3), font="bold", key="/")],
        [sg.Button("%", size=(7, 3), font="bold", key="%")],
        [sg.Button("=", size=(7, 3), font="bold", key="=")],]
    

layout_calculadora =[[sg.Frame("", visor)],
                     [sg.Frame("", numeros), sg.Col(bloco1), sg.Col(bloco2)],
                     [sg.Radio("Média", "RADIO1", size=(9, 1), key="m"),
                      sg.Radio("Raíz", "RADIO1", size=(9, 1), key="r"),
                      sg.Radio("Potência", "RADIO1", size=(9, 1), key="po"),
                      sg.Radio("IMC", "RADIO1", size=(9, 1), key="imc")
                      ],]
#//////////////////////////////////////////////////////////////////////////////  

c1 = [
    [sg.Radio("Adição", "RADIO", default=True, size=(8, 1), key="somar"), sg.Radio("Subtração", "RADIO", size=(8, 1), key="diminuir"),
     sg.Radio("Multiplicação", "RADIO", size=(9, 1), key="multiplicar"), sg.Radio("Divisão", "RADIO", size=(5, 1), key="dividir")],
    [sg.Text("Vamos conhecer a taboada do Numero:", font=("Verdana", 11)),
     sg.Spin(values=[i for i in range(1, 10)], initial_value=1, key='spin', size=(1, 1), font=("Verdana", 11)),
     sg.Button("OK", size=(5, 1))],
    [sg.Image(filename="images.png", size=(230, 310)), 
     sg.Table(values= data, headings=["N1", "Op", "N2","Op2","Resp"], auto_size_columns=True, justification='right',size=(12,18) ,key='-OUT-')],
    [sg.Button("Limpar")],
]
c2 = [[sg.Image(filename="images.png", size=(230, 409))], ]

va1 = [[sg.Frame("", c1)],]
col =[[sg.Col(va1)],]

tab_layout1 = [[sg.Frame("",layout_calculadora)], ]
tab_layout2 = [[sg.Frame("",col)], ]

menu_botao = [["Opções", ["Raiz Quandrada", "Potência", "Percentual", "Média"]], ["Ajuda", ["Ajuda", "Sobre"]]]
janela = [
    [sg.MenuBar(menu_botao)],
    [sg.Text("NOVA TABOADA", size=(45, 1), justification='center', font=("Any", 18, "bold"), relief='flat')],
    [sg.TabGroup([
    [sg.Tab("Calculadora", tab_layout1), sg.Tab("images", tab_layout2)],]),sg.Image(filename="images.png", size=(230, 409))],
    [sg.Text("", size=(11, 1)), sg.Button("Sair",size=(12,1)),sg.Button("Calculadora",size=(12,1))],
    ]




    
window = sg.Window("TABOADA", janela, resizable=True)

while True:
    
    event, values = window.read()
    operadores = ["+", "-", "*","/"]
    numeros=["1","2","3","4","5","6","7","8","9"]
    manter = ""
    operacao = ""
    numeros = [str(i) for i in range(0, 10)]#uma laço para gerar "0 a 9 convertidos em str
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break
    if event == "OK":
        numero = int(values["spin"])

        
        if values["somar"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "+", fator, "=", numero + fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["diminuir"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "-", fator, "=", numero - fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["multiplicar"] == True:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                data.append([numero, "x", fator, "=", numero * fator])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)

        elif values["dividir"]:
            data.append(["", ""," ", "", ""])
            data.append(["==", "==","==", "==", "===="])
            for fator in range(1, 11):
                resutado=numero/fator
                resultado_formatado = "{:.1f}".format(resutado)
                data.append([numero, "/", fator, "=", resultado_formatado])
            data.append(["==","==","==", "==", "===="])
            window["-OUT-"].update(values=data)
        elif event=="Clear":
            window["-OUT-"].update("")   
           
                

        

          
        
        elif event in numeros:
            if not operacao:
                if len(manter) < 17:
                    manter += event
                    window["out"].update(manter)
                    numero=event
            else:
                manter+=event
                numero_2=event
                window["out"].update(manter)
        elif event in operadores:
            operacao=event
            if event not in manter:
                manter += event
            else:
                manter = manter[:-1] + event  #
            window["out"].update(manter)
        elif event == "=":
            if operacao:
                
                if operacao == "+":
                    resp =str(float (numero)+ float(numero_2))
                elif operacao == "-":
                    resp =str(float (numero)- float(numero_2))
                elif operacao == "*":
                    resp =str(float (numero)* float(numero_2))
                elif operacao == "/":
                    if numero_2 != 0:
                        resp =str(float (numero)/ float(numero_2))
                    else:
                        resp = "Erro"
                manter = (f"{resp}".replace(".0",""))
                window["out"].update(manter)
                
                operacao = ""
                numero=(manter)
                numero_2=''
        elif event=="<":
            if len(manter):
                manter=manter[:-1]
                window["out"].update(manter)
        elif event == "c":
            manter = ""
            operacao = ""
            window["out"].update("0")
        elif event == "+/-":
            manter=str(float(manter) * -1)
            window["out"].update(manter)
        elif event==".":
            if "." not in manter:
                manter += "."
                window["out"].update(manter)
        elif event == "%":
            if operacao:
                
                porcentagem = float(numero) * (float(manter) / 100)  # Convertendo para porcentagem
                numero_2 = porcentagem

                if operacao == "+":
                    resp = str(float(numero) + numero_2)
                elif operacao == "-":
                    resp = str(float(numero) - numero_2)
                elif operacao == "*":
                    resp = str(float(numero) * numero_2)
                elif operacao == "/":
                    if numero_2 != 0:
                        resp =str(float (numero)+ float(numero_2))
                    else:
                        manter = "Erro"
                #manter = (f"{resp}".replace(".0",""))
                window["out"].update(resp)
                numero=manter 
                operacao = ""
                numero_2=''
                print(manter)
window.close()