    #SISTEMA DE COBRAÇA EM CAIXA DE SUPERMERCADOS E AFINS
    #Este sistema esta em desenvolvimento em carater academico e conta com colaboração de profissionais e estudantes 
    #da area de Tecnololgia e desenvolvimento de sistemas
def sistema(usuario,data):
    import PySimpleGUI as sg
    import json
    import modulo_pagar
    import modulo_funcao
    import pesquisa
    import novo_item

    lista_produto = []
    carrinho = []
    cupom = int(0)
    item_cancelado = []
    valor_pagar = 0
    num_item = int(0)


    # ===========================================================================================================
    def achar(material):
        for item in dic:
            if material in (item["cod"],item["ean"]) :
                return item["cod"]  # busca o produto dentro do cadastro
        
        return False



            
    # ===========================================================================================================
    def limpar_saida():
        carrinho.clear()
        window["-CUPOM-"].update("")
        window["-SUBTOTAL-"].update("")
        window["-DESCRICAO-"].update("")
        
        window['-VALORUNITARIO-'].update('')
        window['-PRECO-'].update('')
        sg.popup("Operação Encerrada\n  Volte ao menu 'Nova Compra' para continua")

    # limpa os campos sempre que uma nova função e chamada

    # ===================================== Inicio do programa principal======================================================================
    sg.theme("darkBlue3")

    user=["Administrador","Operador turno manha", "Operador turno tarde"]

    titulos = ["Item"," Cod ","    EAN    ","   Descrição do Produto  "," QTD "," PUni R$ ","Preço R$"]

    menu_layout = [
        ["Novo", ["Nova Compra",'Nova Pesquisa','Novo Item']],
        ["Totais", ["Venda Cupom"]], 
        ["Suporte", ["Ajuda", "Data"]]]

    bloco_1=[   [sg.Text("Numero do Cupom", size=(35, 1),font=("Any",17)), sg.Input(size=(17, 1), key="-CUPOM-", font=("Any", 25),justification="right")],
                [sg.Table(values=carrinho, headings=titulos, max_col_width=10, auto_size_columns=True,
                display_row_numbers=False, justification="center",text_color="black",font=("Any",11),background_color="lightyellow", num_rows=25, key="-TABELA-", row_height=20)],
                [sg.Text(" Preço Unitário R$",size=(67,1),font=("Any",12)),sg.Text("SubTotal Item R$",size=(13,1),font=("Any",12))],
                [sg.Input(key="-VALORUNITARIO-",size=(10,1),font=("Any",18),justification="right"),sg.Text(" ",size=(57,1)),sg.Input(key="-PRECO-",size=(10,1),font=("Any",18),justification="right")],
                [sg.Text("TOTAL R$", size=(12, 1), font=("Any", 40)),
                sg.Input(size=(13, 1), key="-SUBTOTAL-", font=("Any", 41), justification='right')],]
                
    bloco_2=[   [sg.Text(" CAIXA FECHADO", size=(15, 1), key='-CAIXA-', font=("Any", 56, "bold"))],
                
                [sg.Text('Código do Produto', size=(25, 1), font=("Any", 12)),sg.Text("", size=(43, 1)),
                sg.Text('  Quantidade', size=(10, 1), font=("Any", 12))],
                [sg.InputText(background_color='White', size=(14,2 ), key='-EAN-', font=("Any", 25)),
                sg.Text("", size=(46, 1)),sg.InputText("1", size=(2, 2), key='-QTD-', font=("Any", 25),justification="right")],
                [sg.Text('Descrição do Produto', size=(25, 1), font=("Any", 12))],
                
                [sg.I(size=(34, 2), key='-DESCRICAO-', font=("Any", 26)), sg.Button(">",font=("Any", 18))],]

    bloco_3=[   [sg.Button('OK', size=(15,1),font=("Any",25)), sg.Text("", size=(10, 1)),sg.Button('DELETE', size=(15, 1),font=("Any",25))],
                [sg.Button('PAGAR', size=(15, 1),font=("Any",25)),sg.Text("", size=(10, 1)), sg.Button('VOLTAR', size=(15, 1),font=("Any",25))],]

    bloco_4=[   [sg.Image(filename="tra.png",size=(695,210))],]

    bloco_5=[   [sg.Text("Operador de Caixa:",size=(17,1),font=("Any",18)),sg.DD(user,key='-USUARIO-',size=(39, 1),font=("Any", 15))],
                [sg.CalendarButton("Data",size=(5,1),close_when_date_chosen=True,target="-DATA-",location=(0,0),no_titlebar=False),
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
        window['-DATA-'].update(data)
        window['-USUARIO-'].update(usuario)
        if event in (sg.WIN_CLOSED, "Fechar"):
            break
        elif event == "Nova Compra":
            cupom += 1
            carrinho=[cupom]
            window['-CUPOM-'].update(f'N°{cupom}')
            window['-CAIXA-'].update('      CAIXA ABERTO')
            window['-SUBTOTAL-'].update(f'R$ {valor_pagar:.2f}')
            window["-TABELA-"].update("")
            
            # dentro deste bloco de eventos serão registrados apenas os botoes (OK,DELETE,PAGAR,VOLTAR)
            while True:
                try:
                    event, values = window.read()
                    if event =='OK': 
                        # verifica se ha valores nos campos de produto e quantidade                  
                        material = values['-EAN-']
                        descricao= values["-DESCRICAO-"]
                        qtd = int(values['-QTD-'])                                               
                        if not material:
                            sg.popup("Erro no campo material!", title="Erro", font=("Any", 10),button_color="red")
                            continue
                        if qtd <1  or qtd > 99 or qtd == "none":
                            sg.popup("Erro no campo Quantidade!", title="Erro", font=("Any", 10),button_color="red")
                            continue
                        
                        plu_pro = achar(material)
                        if plu_pro == False:
                            sg.popup("Erro no campo material", title="Erro", font=("Any", 110),button_color="red")
                            continue
                            # recebe o codigo e integra o produto ao dicionario e lista local # recebe o codigo e integra o produto ao dicionario e lista local
                        else:
                            qtd = int(qtd)
                            for item in dic:
                                if item["cod"] == plu_pro:
                                    num_item += 1
                                    ean = item["ean"]
                                    material = item["item"]
                                    preco_unitario=item["preco"]
                                    preco = item['preco'] * qtd
                                    valor_pagar += preco
                            produto=[ num_item ,plu_pro,  ean,  material, qtd ,preco_unitario, preco]
                                            
                            carrinho.append(produto)
                            window['-TABELA-'].update(values=carrinho)
                            window['-VALORUNITARIO-'].update(f"{preco_unitario:.2f}")
                            window['-PRECO-'].update(f"{preco:.2f}")
                            window['-SUBTOTAL-'].update(f" {valor_pagar:.2f}")

                    elif event == ">" :
                        desc=pesquisa.pesquisar(dic)
                                        
                    elif event == 'DELETE':
                        valor_pagar = modulo_funcao.remover(valor_pagar,carrinho,window["-TABELA-"])
                        window['-SUBTOTAL-'].update(f"R$ {valor_pagar:.2f}")
                        window["-TABELA-"].update(values=carrinho)
                        continue

                    elif event == 'PAGAR':
                        # condição para conciderar o cupom com "pago"
                        valor_pagar = modulo_pagar.pagar(valor_pagar)
                        if valor_pagar == float(0):
                            lista_produto.extend(carrinho)
                            #limpar_saida()
                            num_item = 0
                            limpar_saida()
                            break
                        else:
                            continue
                    elif event == "VOLTAR":  # limpa todos os valores e lista local
                        
                        limpar_saida()
                        num_item = 0
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
            window['-CAIXA-'].update('CAIXA FECHADO')
            limpar_saida()
            continue
        elif event == "Nova Pesquisa" :
            desc=pesquisa.pesquisar(dic)
            continue
        elif event == 'Novo Item':
            i=novo_item.novo_item()
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


