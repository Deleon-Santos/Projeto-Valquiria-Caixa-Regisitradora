from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def imprimir(informacao, pesquisa_cupom):
    def create_tabela(data, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []

        # Estilo da tabela
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ])

        # Formatação dos dados para a tabela
        data_formatted = [[str(item) for item in row] for row in data]
        table = Table(data_formatted)
        table.setStyle(style)
        
        elements.append(table)  # Add table to elements list
        doc.build(elements)  # Build the PDF with elements
        print(table)
        

    def criar_pdf(content, table_data, filename):
        pdf_filename = filename
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica-Bold", 10)
        title_text = "CUPOM FISCAL"
        title_width = c.stringWidth(title_text, "Helvetica-Bold", 10)
        c.drawString((letter[0] - title_width) / 2, 750, title_text)

        c.setFont("Helvetica", 12)
        # Drawing content text
        text_object = c.beginText(130, 730)
        text_object.textLines(content)
        c.drawText(text_object)

        # Drawing table
        table = Table(table_data)
        table.wrapOn(c, 300, 800)  # Wrap table within specified width and height
        table.drawOn(c, 120, 500)  # Draw table on canvas

        c.save()

    # Gerar PDF combinando a tabela de itens e as informações do cupom
    create_tabela(pesquisa_cupom, "cupom_completo.pdf")
    criar_pdf(informacao, pesquisa_cupom, "pdf_salvo.pdf")
    return True

# Exemplo de uso:



