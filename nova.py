'''def create_pdf(data, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    data_cupom='cupom ECF'
    elements = []

    style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                        ('BOX', (0, 0), (-1, -1),  0.25, colors.black)])

    data_formatted = []
    for row in data:
        data_formatted.append([str(item) for item in row])

    table = Table(data_formatted)
    table.setStyle(style)
    elements.append(table)

    doc.build(elements)
    



def informacao(lista_dados):
    informacao = '-'*32 
    quebra="\n"
    
    informacao+=quebra
    informacao+=lista_dados[6]
    informacao += '\nEND : AV. Boa Vista n-1012 Santa Rosa/SP\n'
    
    informacao+='CNPJ :'+lista_dados[3]+ "IE 07.112.888/000-00\n"
    informacao+='Data : '+lista_dados[1]+ 'CCPF : '+lista_dados[4]
    informacao+=quebra
    informacao+='OP : '+lista_dados[2]+'CUPOM : '+lista_dados[0] 
    return informacao


def criar_pdf(content):
    pdf_filename = "ticket_embarque.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    c.setFont("Helvetica", 18)
    c.setFillColorRGB(0, 0, 0)
    text_object = c.beginText(110, 710)
    text_object.textLines(content)
    c.drawText(text_object)
    
    c.save()
    return pdf_filename



lista_dados=[[1, '2024-03-21 17:41:22', 'Administrador', '45.123.0001/40', '45.123.441-40', 33.8, 'TEM DE TUDO ME']]
pesquisa_cupom=[[1, '102', '7890000000102', 'Cafe Melita extra forte 1kg', 1, 16.9, 16.9], [2, '102', '7890000000102', 'Cafe Melita extra forte 1kg', 1, 16.9, 16.9]]

#lista_combinada=(lista_dados + pesquisa_cupom)
create_pdf(pesquisa_cupom, "lista_combinada.pdf")'''
