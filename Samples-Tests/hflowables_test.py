# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

from reportlab.pdfgen import canvas
from reportlab.pdfbase.acroform import AcroForm
from reportlab.platypus.flowables import Flowable
import reportlab.pdfbase.pdfform as pdfform
# textWidth = stringWidth(text, fontName, fontSize) 
from hflowables import *
 
pdfmetrics.registerFont(TTFont('Greek', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('Greek-Italic', 'ariali.ttf'))
pdfmetrics.registerFont(TTFont('Greek-Bold', 'arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Greek-BoldItalic', 'arialbi.ttf'))

addMapping('Greek', 0, 0, 'Greek')    #normal
addMapping('Greek', 0, 1, 'Greek-Italic')    #italic
addMapping('Greek', 1, 0, 'Greek-Bold')    #bold
addMapping('Greek', 1, 1, 'Greek-BoldItalic')    #italic and bold


doc = SimpleDocTemplate("pdf with acroform.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
Story=[]

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, fontName='Greek'))

titletext = '<font size=12>ChechBox</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Fcheckbox(fieldname='Test1', value=unicode('Show me. Και ελληνικά', 'utf-8'), fontName='Greek'))
Story.append(Spacer(1, 12))

titletext = '<font size=12>TextBox</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Ftextbox(fieldname='Test2', value=unicode('Test','utf-8')))
Story.append(Spacer(1, 12))

titletext = '<font size=12>ChoiceBox</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Fchoicebox(fieldname='Test3', value='1 of many', options=['1 of many', '2', '3']))
Story.append(Spacer(1, 12))

titletext = '<font size=12>ListBox</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Flistbox(fieldname='Test4', value='1 of many', options=['1 of many', '2', '3']))
Story.append(Spacer(1, 12))

titletext = '<font size=12>RadioBox Vertical</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Fradiobox(fieldname='Test5', values=['0','1','2','3'], selected=3, size=20, direction=VERTICAL))
Story.append(Spacer(1, 12))

titletext = '<font size=12>RadioBox Horizontal</font>'
Story.append(Paragraph(titletext, styles["Normal"]))
Story.append(Spacer(1, 12))
Story.append(Fradiobox(fieldname='Test6', values=[unicode('τιμή 1','utf-8'),'1',unicode('τιμή 2','utf-8'),'3'], selected=3, size=20, fontName='Greek', direction=HORIZONTAL))
Story.append(Spacer(1, 12))

doc.build(Story)
