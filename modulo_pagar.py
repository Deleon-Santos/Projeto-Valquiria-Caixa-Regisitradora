import PySimpleGUI as sg

def pagar(valor_pagar):

    frame6=[[sg.Text("Valor da Compra ", size=(28, 1), font=("Any", 12)),
        sg.Text(f"R$ {valor_pagar:.2f}", size=(18, 1), justification='right', key="valor", font=("Any", 18))],
        [sg.Text("Valor Recabido ", size=(28, 1), font=("Any", 12)),
        sg.Text(f'R$ 0.00', size=(18, 1), key="recebido", justification='right', font=("Any", 18))],
        [sg.Text("Troco Devolvido ", size=(28, 1), font=("Any", 12)),
        sg.Text(f'R$ 0.00', size=(18, 1), key="R$", justification='right', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Button('CARTAO', font=("Any", 18),size=(15, 1)), sg.Button('PIX',font=("Any", 18), size=(15, 1)), sg.Button('DINHEIRO',font=("Any", 18), size=(15, 1))],
        [sg.T("")],
    ]

    layout = [
        [sg.Text("CONDIÇÃO DE PAGAMENTO", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("",size=(8,1)),sg.Image(filename="imagem/f_pagamentos.png",size=(404,197))],
        [sg.Text("", size=(10, 1))],
        [sg.Frame("",frame6)],
       ]
    
    window = sg.Window("PAGAMENTO", layout, finalize=False)

    while True:
        
        event, values = window.read()
        pago = valor_pagar
        troco = 0
        window["valor"].update(f"R$ {valor_pagar:.2f}")

        if event == sg.WIN_CLOSED:
            sg.popup("Cancelar forma de Pagamento", font=("Any", 18))
            return valor_pagar
            
        elif event in ("CARTAO", "PIX"):  # para cartão e pix o valor e descontado itegralmente
            if valor_pagar > 0:  # somente se o subtotal existir e for maior que "0"
                valor_pagar = 0
                window["valor"].update(f"R$ {valor_pagar:.2f}")
                window["recebido"].update(f"R$ {pago:.2f}")
                sg.popup("Pagamento Autorizado", font=("Any", 18))
                return valor_pagar
   
        elif event == "DINHEIRO":
            try:
                dinheiro = sg.popup_get_text("Valor Recebido", font=("Any", 12))
                if dinheiro is not None:  # verifica se tem valores
                    dinheiro = float(dinheiro)
                    if dinheiro >= valor_pagar:
                        sg.popup("Pagamento efetuado com sucesso", font=("Any", 18))
                        troco = dinheiro - valor_pagar
                        valor_pagar = 0
                        window["valor"].update(f"R$ {valor_pagar:.2f}")
                        window["recebido"].update(f"R$ {dinheiro:.2f}")
                        window["R$"].update(f"R$ {troco:.2f}")
                        return valor_pagar  # desconta o subtotal e retorna o troco
                        
                    else:
                        sg.popup("Valor Insuficiente", font=("Any", 18))
                        continue
                else:
                    continue
            except ValueError:
                sg.popup("Insira um valor válido", font=("Any", 18))
                continue
        
    window.close()

