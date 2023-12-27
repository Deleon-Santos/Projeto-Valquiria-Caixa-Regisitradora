import PySimpleGUI as sg
import json


lista_produto = []
carrinho = []
com = int(0)
cancela = []
soma2 = 0
num = int(0)

try:
    with open('comanda.txt', 'r') as adic:
        dic = json.load(adic)

    # Seu código para ler o arquivo
except FileNotFoundError:
    sg.popup("O arquivo 'comanda.txt' não foi encontrado. Verifique o caminho ou crie o arquivo.")

#with open('comanda.txt', 'r') as adic:  # comando para ler o Aquivo.txt com os dados dos produtos
   

# =============================================================================================================
def remover(soma2):
    try:  # leia a lista1 e encontre o item informado
        remove = int(sg.popup_get_text('Remover o Item', font=("Any", 18)))
        for lanche in carrinho:
            if lanche["Item"] == remove:
                soma2 -= lanche["Preco"]
                cancela.append(lanche["Preco"])
                sg.popup(
                    f'N°{lanche["Item"]} {lanche["Cod"]}-{lanche["Lanche"]} {lanche["Quantidade"]} R$ {pre:.2f}',
                    font=("Any", 18))
                carrinho.remove(lanche)  # rmova o item da lista1
        return soma2
    except:
        sg.popup("Não Encontrado", font=("Any", 18))
        return soma2


# =============================================================================================================
def venda_cupom():
    layout_menu = [
        ["Menu", ["Todos"]],
    ]
    layout = [[sg.Menu(layout_menu)],
              [sg.Text("VENDA POR CUPOM", size=(50, 1), justification='center', font=("Any", 18))],
              [sg.Text("", size=(10, 1))],
              [sg.Text("N° do Cupom Fiscal", size=(20, 1)),
               sg.InputText(background_color='White', key="cupom", size=(10)), sg.Text("", size=(44, 1)),
               sg.Button("Pesquisar", size=(11, 1))],
              [sg.Multiline(size=(100, 20), key='output')],
              [sg.Text("", size=(58, 1)), sg.Text("Total", size=(8, 1), font=("Any", 18)),
               sg.Text(key="R$", size=(8, 1), justification='right', font=("Any", 18))],
              ]
    window = sg.Window("Resumo de Vendas", layout, finalize=True)
    window['output'].print(
        "      Item       Produto                                                                        Quantidade                   Valor")
    while True:
        try:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Fechar"):
                break
            elif event == "Todos":
                window['output'].update("")
                soma_total = 0
                for cupom in set(
                        item["Comanda"] for item in lista_produto):  # passa por todos os cupons e todos os itens
                    soma = 0
                    window['output'].print(f'{"":<4}  CUPOM N° {cupom}')
                    for lanche in lista_produto:
                        if lanche["Comanda"] == cupom:
                            window['output'].print(
                                f'{"":<4}  N°{lanche["Item"]:<8} {lanche["Cod"]} - {lanche["Ean"]} - {lanche["Lanche"]:<40} {lanche["Quantidade"]}')
                            window['output'].print(f'R$ {lanche["Preco"]:.2f}'.rjust(140))
                            window["output"].print(
                                "      ======================================================================")
                            soma += lanche["Preco"]
                    window['output'].print(f'"R$ {soma:.2f}'.rjust(140))
                    window["output"].print(
                        "      ======================================================================")
                    soma_total += soma
                window["R$"].update(f"R$ {soma_total:.2f}")  # soma total


            elif event == "Pesquisar":
                cupom = values["cupom"]

                if not cupom:  # verifica se tem valor em cupom
                    sg.Text("Informe o N° do Cupom", font=("Any", 18))
                else:
                    cupom = int(cupom)  # para esse cupom, todos os itens
                    for produto in lista_produto:
                        if produto["Comanda"] == cupom:
                            soma = 0
                            if produto["Comanda"] == cupom:
                                window['output'].update("")
                                window['output'].print(f'{"":<4}  CUPOM N° {cupom}')
                                for lanche in lista_produto:
                                    if lanche["Comanda"] == cupom:
                                        window['output'].print(
                                            f'{"":<4}  N°{lanche["Item"]:<8} {lanche["Cod"]} - {lanche["Ean"]} - {lanche["Lanche"]:<40} {lanche["Quantidade"]}')  # R$ {lanche["Preco"]:.2f}')
                                        window['output'].print(f'R$ {lanche["Preco"]:.2f}'.rjust(140))
                                        window["output"].print(
                                            "      ======================================================================")
                                        soma += lanche["Preco"]
                                window["R$"].update(f"R$ {soma:.2f}")
                                break
                        else:
                            sg.popup("Não Encontrado", font=("Any", 18))
        except:
            sg.Text("Não Encontrado!", font=("Any", 18))
    window.close()


# ===========================================================================================================
def total():
    layout = [
        [sg.Text("VENDA TOTAL DO DIA", size=(50, 1), justification='center', font=("Any", 18))],
        [sg.Multiline(size=(100, 20), key='output')],
        [sg.Text("", size=(56, 1)), sg.Text(key="qtd", font=("Any", 18)), sg.Text("", size=(9, 1)),
         sg.Text(key="R$", justification='center', font=("Any", 18))],
    ]
    window = sg.Window("Resumo de Vendas", layout, finalize=True)
    window['output'].print(
        "      Produto                                                                                       Quantidade                Valor")
    qtd_t = 0
    som_t = 0
    for l in dic:  # passa por todos os cupons e todos os iten
        produto = l["lanche"]
        qtd = 0
        somas = 0
        for lanche in lista_produto:
            if lanche["Lanche"] == produto:
                qtd += lanche["Quantidade"]
                cod = lanche["Cod"]
                ean = lanche["Ean"]
                somas += lanche["Preco"]
        if qtd > 0:
            window['output'].print(f'{"":<5} {cod} - {ean} - {produto:<10}{qtd:>30}')
            window['output'].print(f'                                 R$ {somas:.2f}'.rjust(140))
            window["output"].print("      ======================================================================")
            qtd_t += qtd
            som_t += somas
    window['qtd'].print(f'Qtd {qtd_t}')  # pega a quantidade total
    window['R$'].print(f'R$ {som_t:.2f}')  # pega o valor total
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Fechar"):
            break
    window.close()


# =====================================================================================================================
def pagar(soma2):
    layout = [
        [sg.Text("CONDIÇÃO DE PAGAMENTO", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Text("Valor Total da Compra ", size=(28, 1), font=("Any", 12)),
         sg.Text(f"R$ {soma2:.2f}", size=(18, 1), justification='right', key="valor", font=("Any", 18))],
        [sg.Text("Valor Recolhido ", size=(28, 1), font=("Any", 12)),
         sg.Text(f'R$ 0.00', size=(18, 1), key="recebido", justification='right', font=("Any", 18))],
        [sg.Text("Troco Devolvido ", size=(28, 1), font=("Any", 12)),
         sg.Text(f'R$ 0.00', size=(18, 1), key="R$", justification='right', font=("Any", 18))],
        [sg.Text("", size=(10, 1))],
        [sg.Button('CARTAO', size=(20, 1)), sg.Button('PIX', size=(20, 1)), sg.Button('DINHEIRO', size=(20, 1))],

    ]

    window = sg.Window("PAGAMENTO", layout, finalize=True)

    while True:
        event, values = window.read()
        pago = soma2
        troco = 0
        window["valor"].update(f"R$ {soma2:.2f}")

        if event == (sg.WIN_CLOSED):
            sg.popup("Cancelar forma de Pagamento", font=("Any", 18))
            return soma2

        elif event in ("CARTAO", "PIX"):  # para cartão e pix o valor e descontado itegralmente
            if soma2 > 0:  # somente se o subtotal existir e for maior que "0"
                soma2 = 0
                window["valor"].update(f"R$ {soma2:.2f}")
                window["recebido"].update(f"R$ {pago:.2f}")
                sg.popup("Pagamento Autorizado", font=("Any", 18))
                return soma2
                break

        elif event == "DINHEIRO":
            try:
                dinheiro = sg.popup_get_text("Valor Recebido", font=("Any", 18))
                if dinheiro is not None:  # verifica se tem valores
                    dinheiro = float(dinheiro)
                    if dinheiro >= soma2:
                        troco = dinheiro - soma2
                        soma2 = 0
                        window["valor"].update(f"R$ {soma2:.2f}")
                        window["recebido"].update(f"R$ {dinheiro:.2f}")
                        window["R$"].update(f"R$ {troco:.2f}")

                        sg.popup("Pagamento efetuado com sucesso", font=("Any", 18))
                        return soma2  # desconta o subtotal e retorna o troco
                        break
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


# ============================================================================================================
def novo_item():
    # abre os itens existentes do arquivo JSON
    with open("comanda.txt", 'r') as arquivo:
        dic = json.load(arquivo)

    layout = [
        [sg.Text("CADASTRAR ITEM", size=(35, 1), justification='center', font=("Any", 18))],
        [sg.Text("", size=(20, 1))],
        [sg.Text("Código:", size=(10, 1)), sg.Text("", size=(10, 1), key="codigo")],
        [sg.Text("Produto:", size=(10, 1)),
         sg.InputText(background_color='White', key="produto", size=(25, 1), font=("Any", 18))],
        [sg.Text("Preço:", size=(10, 1)),
         sg.InputText(background_color='White', key="preco", size=(25, 1), font=("Any", 18))],
        [sg.Text("", size=(20, 1))],
        [sg.Text("", size=(17, 1)), sg.Button("Cadastrar", size=(11, 1)), sg.Button("Sair", size=(11, 1))],
    ]

    window = sg.Window("Cadastro de Itens", layout)
    while True:
        try:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Sair"):
                break
            elif event == "Cadastrar":
                prod = values["produto"]
                if len(prod) > 25:
                    sg.popup_scrolled(
                        "A descrição nao deve ser maior que o campo input\nDescreva o item com ate 25 caracteres")
                    continue
                else:

                    t = len(dic) + 101  # conta os itens e adiciona "101"
                    numero = str(t)
                    ean = 7890000000000 + t
                    ean = str(ean)  # converte o inteiro em str concatenendo o codigo gerado
                    window["codigo"].update(numero)
                    # prod = values["produto"]
                    prec = float(values["preco"])
                    cadastro_item = {"cod": numero, "ean": ean, "lanche": prod, "preco": prec}
                    # Adicione o novo item ao dicionário
                    dic.append(cadastro_item)
                    with open("comanda.txt", 'w') as arquivo:

                        json.dump(dic, arquivo, indent=4)
                # sg.popup_scrolled(*cadastro_item, title="Item Cadastrado", font=("Any",18))
                item_str = f"Código: {cadastro_item['cod']} - {cadastro_item['ean']}\nLanche: {cadastro_item['lanche']}\nPreço: R${cadastro_item['preco']:.2f}"

                # Exiba os dados formatados com sg.popup_scrolled
                sg.popup_scrolled(item_str, title="Item Cadastrado", font=("Any", 18))
                break
        except ValueError:
            sg.popup("Informe valor numerico", title="Preço", font=("Any", 18))
    window.close()


# ===========================================================================================================
def limpar_saida():
    carrinho.clear()

    window["com"].update("")
    window["output"].update("")
    window["subtotal"].update("")
    window["descricao"].update("")


# limpa os campos sempre que uma nova função e chamada

# ===================================== Inicio do programa principal======================================================================
sg.theme("LightBlue3")

menu_layout = [["Novo", ["Nova Compra", "Novo Produto", "Pesquisar Produto"]],
               ["Totais", ["Venda Cupom", "Venda Total"]], ["Suporte", ["Ajuda", "Data"]]]

bloco_1=[   [sg.Text("CAIXA FECHADO", size=(70, 1), key='caixa', justification='center', font=("Any", 55, "bold"))],
             ]

bloco_2=[   [sg.Text('Código do Produto', size=(25, 1), font=("Any", 18)),sg.Text("", size=(32, 1)),sg.Text('Quantidade', size=(10, 1), font=("Any", 18))],
            [sg.InputText(background_color='White', size=(3,2 ), key='lanche1', font=("Any", 25)),
             sg.InputText(background_color='White', size=(14,2 ), key='ean', font=("Any", 25)),
             sg.Text("", size=(35, 1)),sg.InputText("1", size=(8, 2), key='qtd', font=("Any", 25))],
            [sg.Text('Código do Produto', size=(25, 1), font=("Any", 18))],
            [sg.InputText(size=(43, 2), key='descricao', font=("Any", 25))],]

bloco_3=[   [sg.Button('OK', size=(30,2)), sg.Text("", size=(32, 1)),sg.Button('DELETE', size=(30, 2))],
            [sg.Button('PAGAR', size=(30, 2)),sg.Text("", size=(32, 1)), sg.Button('VOLTAR', size=(30, 2))],
            ]

bloco_4=[   [sg.Image(filename="images.png",size=(780,210))],
         ]

frame1=[   
            [sg.Frame("",bloco_2)],
            [sg.Frame("",bloco_3)],
            [sg.Frame("",bloco_4)],
            


            ]

frame2=[   [sg.Multiline(size=(85, 28), key='output', font=("Any", 12))],]

layout = [  
            [sg.Menu(menu_layout)],
            [sg.Frame("",bloco_1)],
            [sg.Text(" ", size=(88, 1)), sg.Text(size=(23, 1), key="com", justification='right', font=("Any", 18))],
            
            [sg.Col(frame1),sg.Col(frame2)],
            [sg.Text("12 de outubro de 1233", size=(25, 1), key='data', font=("Any", 12)),
            sg.Text("DESENVOLVIDO POR:", size=(18, 1), font=("Any", 10)),
            sg.Text("linkedin.com/in/deleon-santos-1b835a290", size=(40, 1), key='LOG', font=("Any", 10)),
            sg.Text("", size=(10, 1)), sg.Text("SubTotal", size=(12, 2), font=("Any", 40)),
            sg.Text(size=(10, 2), key="subtotal", font=("Any", 40), justification='right')],]
window = sg.Window("NOVO PEDIDO", layout, resizable=True)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Fechar"):
        # sg.popup("ENCERRAR",font=("Any", 18))
        break
    elif event == "Nova Compra":
        com += 1
        window['com'].update(f'CUPOM FISCAL N°{com}')
        window['caixa'].update('CAIXA ABERTO')
        window['subtotal'].update(f'R$ {soma2:.2f}')
        window["output"].update("")
        # dentro deste bloco de eventos serão registrados apenas os botoes (OK,DELETE,PAGAR,VOLTAR)
        while True:
            try:
                event, values = window.read()
                if event =='OK': 
                    # verifica se ha valores nos campos de produto e quantidade
                    material = values['lanche1']
                    qtd = int(values["qtd"])
                    if not material:
                        sg.popup("Erro em Produto!", title="Erro", font=("Any", 18))
                        continue
                    elif qtd > 0 and qtd < 100:
                        pro = achar(material)
                        # recebe o codigo e integra o produto ao dicionario e lista local
                        if pro == False:
                            #sg.popup("Erro em Produto", title="Erro", font=("Any", 18))
                            continue
                        else:
                            qtd = int(qtd)
                            for item in dic:
                                if item["cod"] == pro:
                                    num += 1
                                    ean = item["ean"]
                                    lanche = item["lanche"]
                                    preco = item['preco'] * qtd
                                    soma2 += preco
                            dicionario = {'Comanda': com, 'Item': num, "Cod": pro, "Ean": ean, 'Lanche': lanche,
                                          'Quantidade': qtd,
                                          'Preco': preco}
                            carrinho.append(dicionario.copy())
                            # escreve os valores na tela de output
                            for lanche in carrinho:
                                pre = lanche["Preco"]
                            window['output'].print(
                                f'       N°{"":<7}{lanche["Item"]}{"":>15}{lanche["Cod"]} - {lanche["Ean"]} - {lanche["Lanche"]:<18}{"":>20} {lanche["Quantidade"]:<18}')
                            window['output'].print(f'R$ {pre:.2f}'.rjust(156))
                            window["output"].print(
                                "      ======================================================================")
                            window['subtotal'].update(f"R$ {soma2:.2f}")
                            window["descricao"].update(f" {lanche['Ean']} - {lanche['Lanche']}")
                            window["lanche1"].update("")
                            continue
                    else:
                        sg.popup("Erro em Quantidade", title="Erro em Quan", font=("Any", 18))
                elif event == 'DELETE':
                    soma2 = remover(soma2)
                    window['subtotal'].update(f"R$ {soma2:.2f}")
                    condicao = len(cancela)
                    # condição para mostra o valor estornado
                    if condicao == 1:
                        window['output'].print(f'-R$ {cancela[0]:.2f}'.rjust(140))
                        window["output"].print(
                            "      ======================================================================")
                        cancela.clear()
                    continue

                elif event == 'PAGAR':
                    # condição para conciderar o cupom com "pago"
                    soma2 = pagar(soma2)
                    if soma2 == float(0):
                        lista_produto.extend(carrinho)
                        limpar_saida()
                        num = 0
                        break
                    else:
                        continue
                elif event == "VOLTAR":  # limpa todos os valores e lista local
                    carrinho.clear()
                    limpar_saida()

                    soma2 = 0
                    com -= 1
                    num = 0
                    break
                elif event == (sg.WIN_CLOSED):
                    sg.popup("ENCERRAR", font=("Any", 18))
                    break
            except ValueError:  # trata erro de valor não numerico
                sg.popup('Erro na quantidade', title="Erro em Quantidade", font=("Any", 18))
                continue
    elif event == "Venda Total":
        limpar_saida()
        total()
    elif event == "Pesquisar Produto":  # mostra todos os produtos cadastrados
        window["com"].update("PESQUISAR PRODUTO")
        window["output"].print(
            f'{"      CÓDIGO" :<10}                      {"PRODUTO":<60}                      {"PRECO"}')
        for lanche in dic:
            window['output'].print(f'      {lanche["cod"]} - {lanche["ean"]} - {lanche["lanche"]:<18}{"":>20} ')
            window['output'].print(f'R$ {lanche["preco"]:.2f}'.rjust(140))
            window["output"].print("      ======================================================================")
    elif event == "VOLTAR":
        window['caixa'].update('CAIXA FECHADO')
        limpar_saida()
        continue
    elif event == "Novo Produto":
        limpar_saida()
        novo_item()
    elif event == "Venda Cupom":
        limpar_saida()
        venda_cupom()
    elif event == "Data":
        limpar_saida()
        data = sg.popup_get_text("Data", font=("Any", 18))
        if data:  # permite inserir uma data atual ao sistema
            window["data"].update(f'{data}')

    elif event == "Ajuda":
        sg.popup_scrolled(" Sistema em desenvolvimento, algumas funcionalidades  podem  apresentar erros\n" +
                          "e falhas inesperadas, caso ocorram problemas reportem ao desenvolvedor  atraves\n" +
                          "do contato disponivel pra que as correções seja incorporadas ao codigo.Em brevo\n" +
                          "apresentaremos uma bibliotca. Aguardem!\n" +
                          "delps.santos1987@gmail.com , linkedin.com/in/deleon-santos-1b835a290\n" +
                          "\n" +
                          "PRIMEIROS PASSOS EM APP_VENDAS\n" +
                          "\n" +
                          "-Novo>\n" +
                          "  -Pesqisar Produto: Pesquisa todos os produtos cadastrados ate o ultimo login.\n" +
                          "  -Novo Produto:Cadastra um novo produto no banco de dados(OBS:o novo item sera\n" +
                          "   exibido no proximo login).\n" +
                          "  -Nova Compra: Habilita o numero de cupom e inicia a tela de registro.\n" +
                          "       -Botão OK: Confirma a escolha do item selacionado na entrada de produto.\n" +
                          "       -Botão DELETE: Permite excluir um item da seu carrinho de compra. \n" +
                          "       -Botão PAGAR: Permite pagar o sub total do carrinho de compra. \n" +
                          "       -Botão VOLTAR: Permite cancelar o cupon ou sair de qualquer menu do APP.\n" +
                          "\n" +
                          "-Totais>\n" +
                          "   -Venda Cupon: Permite consultar por numero de cupon ou todos os cupons\n" +
                          "   -Venda Total: Permite ver a venda total por item, valores  e total de  venda\n" +
                          "\n" +
                          "-Suporte>\n" +
                          "   -Ajuda: Retorna um menu minimalista com as principais funcionalidades de app\n" +
                          "   -Data: permite alterar a data no sistema", title='Ajuda')
        continue
window.close()

#