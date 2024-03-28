from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Função para criar o PDF
def create_pdf(data, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    style = TableStyle([('ALIGN', (0, 0), (-1, -1), (0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0), 'CENTER'),
                        ('VALIGN', (0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0), 'MIDDLE'),
                        ('INNERGRID', (0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0),(-1, -1),(0, 0), 0.25, colors.black),
                        ('BOX', (0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0), (-1, -1),(0, 0), 0.25, colors.black)])

    data_formatted = []
    for row in data:
        data_formatted.append([str(item) for item in row])

    table = Table(data_formatted)
    table.setStyle(style)
    elements.append(table)

    doc.build(elements)



def lista_combinada(d , pesquisa_cupom):
    lista_combinada=(d + pesquisa_cupom)

# Criar PDF para lista_combinada
    create_pdf(lista_combinada, "lista_combinada.pdf")