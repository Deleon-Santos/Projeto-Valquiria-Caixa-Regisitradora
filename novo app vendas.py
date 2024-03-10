#SISTEMA DE COBRAÇA EM CAIXA DE SUPERMERCADOS E AFINS
#Este sistema esta em desenvolvimento em carater academico e conta com colaboração de profissionais e estudantes 
#da area de Tecnololgia e desenvolvimento de sistemas

import PySimpleGUI as sg
import json

lista_produto = []
carrinho = []
cupom = int(0)
item_cancelado = []
valor_pagar = 0
num_item = int(0)



# =============================================================================================================
def remover(valor_pagar):
    try:  # leia a lista1 e encontre o item informado
        remove_item = int(sg.popup_get_text('Remover o Item', font=("Any", 18)))
        print(f"item removido{remove_item}")
        for indice, material in enumerate(carrinho):
            if indice == remove_item:
                valor_pagar -= material[6]
                material[4]*=-1
                material[5]*=-1
                material[6]*=-1
                window["-TABELA-"].update(values=carrinho)
                return valor_pagar
    except:
        sg.popup("Rejeitar Item", font=("Any", 18))
        return valor_pagar
    
    
    


# =============================================================================================================

# =====================================================================================================================
def pagar(valor_pagar):
    frame6=[[sg.Text("Valor Total da Compra ", size=(28, 1), font=("Any", 12)),
        sg.Text(f"R$ {valor_pagar:.2f}", size=(18, 1), justification='right', key="valor", font=("Any", 18))],
        [sg.Text("Valor Recolhido ", size=(28, 1), font=("Any", 12)),
        sg.Text(f'R$ 0.00', size=(18, 1), key="recebido", justification='right', font=("Any", 18))],
        [sg.Text("Troco Devolvido ", size=(28, 1), font=("Any", 12)),
        sg.Text(f'R$ 0.00', size=(18, 1), key="R$", justification='right', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Button('CARTAO', size=(20, 1)), sg.Button('PIX', size=(20, 1)), sg.Button('DINHEIRO', size=(20, 1))],

    ]
    layout = [
        [sg.Text("CONDIÇÃO DE PAGAMENTO", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("",size=(8,1)),sg.Image(filename="111.png",size=(400,100))],
        [sg.Text("", size=(10, 1))],
        [sg.Frame("",frame6)]

    ]

    window = sg.Window("PAGAMENTO", layout, finalize=True)

    while True:
        
        event, values = window.read()
        pago = valor_pagar
        troco = 0
        window["valor"].update(f"R$ {valor_pagar:.2f}")

        if event == (sg.WIN_CLOSED):
            sg.popup("Cancelar forma de Pagamento", font=("Any", 12))
            #return soma2


        elif event in ("CARTAO", "PIX"):  # para cartão e pix o valor e descontado itegralmente
            if valor_pagar > 0:  # somente se o subtotal existir e for maior que "0"
                valor_pagar = 0
                window["valor"].update(f"R$ {valor_pagar:.2f}")
                window["recebido"].update(f"R$ {pago:.2f}")
                sg.popup("Pagamento Autorizado", font=("Any", 12))
                return valor_pagar
                #break

        elif event == "DINHEIRO":
            try:
                dinheiro = sg.popup_get_text("Valor Recebido", font=("Any", 12))
                if dinheiro is not None:  # verifica se tem valores
                    dinheiro = float(dinheiro)
                    if dinheiro >= valor_pagar:
                        troco = dinheiro - valor_pagar
                        valor_pagar = 0
                        window["valor"].update(f"R$ {valor_pagar:.2f}")
                        window["recebido"].update(f"R$ {dinheiro:.2f}")
                        window["R$"].update(f"R$ {troco:.2f}")

                        sg.popup("Pagamento efetuado com sucesso", font=("Any", 18))
                        return valor_pagar  # desconta o subtotal e retorna o troco
                        #break
                    else:
                        sg.popup("Valor Insuficiente", font=("Any", 18))
                        continue
                else:
                    continue
            except ValueError:
                sg.popup("Insira um valor válido", font=("Any", 18))
                continue
        break
    window.close()


# ===========================================================================================================
def achar(material):
    for lanche in dic:
        if lanche["cod"] == material:
            return lanche["cod"]  # busca o produto dentro do cadastro
    sg.popup("Erro em Produto", title="Erro", font=("Any", 18))
    return False





# ===========================================================================================================
def limpar_saida():
    carrinho.clear()
    window["-CUPOM-"].update("")
    
    window["-SUBTOTAL-"].update("")
    window["-DESCRICAO-"].update("")
    

# limpa os campos sempre que uma nova função e chamada

# ===================================== Inicio do programa principal======================================================================
sg.theme("darkBlue3")
titulos = ["Item","Cod","    EAN    "," Descrição do Produto","QTD","PUni R$","Preço R$"]

menu_layout = [["Novo", ["Nova Compra"]],          
               ["Totais", ["Venda Cupom"]], ["Suporte", ["Ajuda", "Data"]]]

bloco_1=[   [sg.Text("Numero do Cupom", size=(35, 1),font=("Any",17)), sg.Input(size=(17, 1), key="-CUPOM-", font=("Any", 25),justification="right")],
            [sg.Table(values=carrinho, headings=titulos, max_col_width=10, auto_size_columns=True,
            display_row_numbers=False, justification="right",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=25, key="-TABELA-", row_height=20)],
            [sg.Text(" Preço Unitário R$",size=(67,1),font=("Any",12)),sg.Text("SubTotal Item R$",size=(13,1),font=("Any",12))],
            [sg.Input(key="-VALORUNITARIO-",size=(10,1),font=("Any",18),justification="right"),sg.Text(" ",size=(57,1)),sg.Input(key="-PRECO-",size=(10,1),font=("Any",18),justification="right")],
            [sg.Text("TOTAL R$", size=(12, 1), font=("Any", 40)),
            sg.Input(size=(13, 1), key="-SUBTOTAL-", font=("Any", 41), justification='right')],]
             
bloco_2=[   [sg.Text(" CAIXA FECHADO", size=(15, 1), key='-CAIXA-', font=("Any", 56, "bold"))],
            
            [sg.Text('Código do Produto', size=(25, 1), font=("Any", 12)),sg.Text("", size=(35, 1)),
             sg.Text('  Quantidade', size=(10, 1), font=("Any", 12))],
            [sg.InputText(background_color='White', size=(3,2 ), key='-MATERIAL-', font=("Any", 25)),
             sg.InputText(background_color='White', size=(14,2 ), key='-EAN-', font=("Any", 25)),
             sg.Text("", size=(24, 1)),sg.InputText("1", size=(8, 2), key='-QTD-', font=("Any", 25),justification="right")],
            [sg.Text('Descrição do Produto', size=(25, 1), font=("Any", 12))],
            [sg.InputText(size=(38, 2), key='-DESCRICAO-', font=("Any", 25))],]

bloco_3=[   [sg.Button('OK', size=(15,1),font=("Any",25)), sg.Text("", size=(10, 1)),sg.Button('DELETE', size=(15, 1),font=("Any",25))],
            [sg.Button('PAGAR', size=(15, 1),font=("Any",25)),sg.Text("", size=(10, 1)), sg.Button('VOLTAR', size=(15, 1),font=("Any",25))],]

bloco_4=[   [sg.Image(filename="images.png",size=(695,210))],]
bloco_5=[   [sg.Text("Operador de Caixa:",size=(17,1),font=("Any",18)),sg.Input("ADMINISTRADOR DO SISTEMA",key='-USUARIO-',size=(40, 1),font=("Any", 15))],
            [sg.CalendarButton("Data",size=(5,1),close_when_date_chosen=True,target="data",location=(0,0),no_titlebar=False),
            sg.Input(key="-DATA-",size=(17,1)),sg.Text("               Em Desenvolvimento", size=(28, 1), font=("Any", 10)),
            sg.Text("      linkedin.com/in/deleon-santos-1b835a290")],]
            
            

frame1=[   
            [sg.Frame("",bloco_2)],
            [sg.Frame("",bloco_3)],
            [sg.Frame("",bloco_4)],
            [sg.Frame("",bloco_5)]]

frame2=[    [sg.Frame("",bloco_1)] , ]

layout = [  
            [sg.Menu(menu_layout)],           
            [sg.Col(frame1),sg.Col(frame2)],]

#====================================================================================================================================
try:
    with open('comanda.txt', 'r') as adic:
        dic = json.load(adic)

    # Seu código para ler o arquivo
except FileNotFoundError:
    sg.popup("O arquivo 'comanda.txt' não foi encontrado. Verifique o caminho ou crie o arquivo.")

#with open('comanda.txt', 'r') as adic:  # comando para ler o Aquivo.txt com os dados dos produtos
#====================================================================================================================================  

window = sg.Window("NOVO PEDIDO", layout,size=(800,800), resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Fechar"):
        # sg.popup("ENCERRAR",font=("Any", 18))
        break
    elif event == "Nova Compra":
        cupom += 1
        window['-CUPOM-'].update(f'N°{cupom}')
        window['-CAIXA-'].update('      CAIXA ABERTO')
        window['-SUBTOTAL-'].update(f'R$ {valor_pagar:.2f}')
        window["-TABELA-"].update("")
        carrinho=[cupom]
        
        # dentro deste bloco de eventos serão registrados apenas os botoes (OK,DELETE,PAGAR,VOLTAR)
        while True:
            try:
                event, values = window.read()
                if event =='OK': 
                    # verifica se ha valores nos campos de produto e quantidade
                    material = values['-MATERIAL-']
                    qtd = int(values['-QTD-'])
                    if not material:
                        sg.popup("Erro em Produto!", title="Erro", font=("Any", 18))
                        continue
                    elif qtd > 0 and qtd < 100:
                        plu_pro = achar(material)
                        # recebe o codigo e integra o produto ao dicionario e lista local
                        if plu_pro == False:
                            sg.popup("Erro em Produto", title="Erro", font=("Any", 18))
                            continue
                        else:
                            qtd = int(qtd)
                            for item in dic:
                                if item["cod"] == plu_pro:
                                    num_item += 1
                                    ean = item["ean"]
                                    material = item["lanche"]
                                    preco_unitario=item["preco"]
                                    preco = item['preco'] * qtd
                                    valor_pagar += preco
                            dicionario=[ num_item ,plu_pro,  ean,  material, qtd ,preco_unitario, preco]
                                           
                            carrinho.append(dicionario)
                            window['-TABELA-'].update(values=carrinho)
                            window['-VALORUNITARIO-'].update(f"{preco_unitario:.2f}")
                            window['-PRECO-'].update(f"{preco:.2f}")
                            window['-SUBTOTAL-'].update(f" {valor_pagar:.2f}")
                            print(carrinho)
                            
                          
                elif event == 'DELETE':
                    valor_pagar = float(remover(valor_pagar))
                    window['-SUBTOTAL-'].update(f"R$ {valor_pagar:.2f}")
                    window["-TABELA-"].update(values=carrinho)

                   
                    continue
                elif event == 'PAGAR':
                    # condição para conciderar o cupom com "pago"
                    valor_pagar = pagar(valor_pagar)
                    if valor_pagar == float(0):
                        lista_produto.extend(carrinho)
                        #limpar_saida()
                        num_item = 0
                        print(f"lista_produto{lista_produto}")
                        break
                    else:
                        continue
                elif event == "VOLTAR":  # limpa todos os valores e lista local
                    carrinho.clear()
                    limpar_saida()

                    valor_pagar = 0
                    cupom -= 1
                    
                    break
                elif event == (sg.WIN_CLOSED):
                    sg.popup("ENCERRAR", font=("Any", 18))
                    break
            except ValueError:  # trata erro de valor não numerico
                sg.popup('Erro na quantidade', title="Erro em Quantidade", font=("Any", 18))
                continue
    
    
    elif event == "VOLTAR":
        window['caixa'].update('CAIXA FECHADO')
        limpar_saida()
        continue
    
    
    elif event == "Data":
        limpar_saida()
        data = sg.popup_get_text("Data", font=("Any", 18))
        if data:  # permite inserir uma data atual ao sistema
            window['-DATA-'].update(f'{data}')

    elif event == "Ajuda":
        try:
            with open('ajuda.txt', 'r') as legenda:
                arquivo = legenda.read()
                sg.popup_scrolled(arquivo, title="Ajuda")
            # Seu código para ler o arquivo
        except FileNotFoundError:
            sg.popup("O arquivo 'comanda.txt' não foi encontrado. Verifique o caminho ou crie o arquivo.")
        continue
window.close()


