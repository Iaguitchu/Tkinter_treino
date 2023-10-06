from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase.ttfonts import TTfont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser

class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf')

    def geraRelatCliente(self):
        self.c = canvas.Canvas('cliente.pdf')

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.fone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont('Helvetica-Bold', 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont('Helvetica-Bold', 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'Nome: ' )
        self.c.drawString(50, 640, 'Telefone: ')
        self.c.drawString(50, 610, 'Cidade: ')
        
        self.c.setFont('Helvetica', 18)
        self.c.drawString(120, 700, self.codigoRel)
        self.c.drawString(110, 670, self.nomeRel)
        self.c.drawString(135, 640, self.foneRel)
        self.c.drawString(120, 610, self.cidadeRel)

        self.c.rect(10, 550, 550, 5, fill= True, stroke= False)

        self.c.showPage()
        self.c.save()
        self.printCliente()

