import PySimpleGUI as sg

def pagar(valor_pagar):

    frame6=[[sg.P(),sg.T("Valor da Compra ", size=(23, 1), font=("Any", 12)),
             sg.I(f" {valor_pagar:.2f}", size=(18, 1), justification='right', key="valor", font=("Any", 18)),sg.P()],
            [sg.P(),sg.T("Valor Recabido  ", size=(23, 1), font=("Any", 12)),
            sg.I(f' 0.00', size=(18, 1), key="recebido", justification='right', font=("Any", 18)),sg.P()],
            [sg.P(),sg.T("Troco Devolvido ", size=(23, 1), font=("Any", 12)),
            sg.I(f' 0.00', size=(18, 1), key="R$", justification='right', font=("Any", 18)),sg.P()],
            [sg.T("", size=(10, 1))],
            [sg.P(),sg.B("CARTAO", font=("Any", 12),size=(15, 1)), sg.B('PIX',font=("Any", 12), size=(15, 1)), sg.B('DINHEIRO',font=("Any", 12), size=(15, 1)),sg.P(),sg.B("SAIR",font=("Any", 12), size=(15, 1)),sg.P()],
        
    ]

    layout = [
        [sg.T("CONDIÇÃO DE PAGAMENTO", size=(35, 1), justification='center', font=("Any", 18,'bold'))],
        [sg.P(),sg.Image(filename="imagem/f_pagamento.png",size=(504,145)),sg.P()],
        [sg.T("", size=(10, 1))],
        [sg.P(),sg.Frame("",frame6),sg.P()],
       ]
    
    window = sg.Window("PAGAMENTO", layout, finalize=True)

    while True:
        
        event, values = window.read()
        pago = valor_pagar
        troco = 0
        #window["valor"].update(f"R$ {valor_pagar:.2f}")

        if event in (sg.WIN_CLOSED , "SAIR"):
            sg.popup("Continuar ")
            
            break
            
           
        if event in ('PIX', "CARTAO"):  # para cartão e pix o valor e descontado itegralmente
            if valor_pagar > 0:  # somente se o subtotal existir e for maior que "0"
                valor_pagar = 0
                window["valor"].update(f"R$ {valor_pagar:.2f}")
                window["recebido"].update(f"R$ {pago:.2f}")
                sg.popup("Autorizado", font=("Any", 18))
                return valor_pagar
            

        elif event == "DINHEIRO":
            try:
                dinheiro = sg.popup_get_text("Valor Recebido", font=("Any", 18),default_text='0,00')
                if dinheiro is not None:  # verifica se tem valores
                    dinheiro = float(dinheiro)
                    if dinheiro < valor_pagar:
                        sg.popup("Insuficiente", font=("Any", 18))
                        continue
                        
                    else:
                        
                        troco = dinheiro - valor_pagar
                        valor_pagar = 0
                        window["valor"].update(f"R$ {valor_pagar:.2f}")
                        window["recebido"].update(f"R$ {dinheiro:.2f}")
                        window["R$"].update(f"R$ {troco:.2f}")
                        sg.popup("Autorizado", font=("Any", 18))
                          # desconta o subtotal e retorna o troco
                        return valor_pagar
                else:
                    sg.popup("Informe o valor recebido")
                    
                        
                

            except Exception as erro:
                sg.popup(f"Erro: {erro}", font=("Any", 18))
                continue
        
    window.close()

