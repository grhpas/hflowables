# -*- coding: utf-8 -*-
# hflowables (hflowables.py)
# ========================================================================
# Description: Exporting Reportlab acroform components to Flowables
#
#              Tested with Python v2.7.X (win32)
# Author: Gregory Papadopoulos
# Copyright: 
#
# Modification History
# Date         Author Comment
# ========================================================================
# 2017/xx/xx - grhpas (aka Gregory Papadopoulos)
#                  Created
#              Not fully PEP8 compliant - yet. Due to compatibility to 
#              Reportlab code
# ========================================================================
# These are the flag values used in acroforms. They are Boolean values, harcoded to bits. 
# Usage: fieldFlags='multiline, richText' turns multiline True and richtext True. All others False
# 
#         #adobe counts bits 1 - 32
#         fieldFlagValues = dict(
#                         readOnly = 1<<0,
#                         required = 1<<1,
#                         noExport = 1<<2,
#                         noToggleToOff = 1<<14,
#                         radio = 1<<15,
#                         pushButton = 1<<16,
#                         radiosInUnison = 1<<25,
#                         #text fields
#                         multiline = 1<<12,
#                         password = 1<<13,
#                         fileSelect = 1<<20,         #1.4
#                         doNotSpellCheck = 1<<22,    #1.4
#                         doNotScroll = 1<<23,        #1.4
#                         comb = 1<<24,               #1.5
#                         richText = 1<<25,           #1.5
# 
#                         #choice fields
#                         combo = 1<<17,
#                         edit = 1<<18,
#                         sort = 1<<19,
#                         multiSelect = 1<<21,        #1.4
#                         commitOnSelChange = 1<<26,  #1.5
#                         )
# 
#         annotationFlagValues = dict(
#                             invisible=1<<0,
#                             hidden=1<<1,
#                             nozoom=1<<3,
#                             norotate=1<<4,
#                             noview=1<<5,
#                             readonly=1<<6,
#                             locked=1<<7,            #1.4
#                             togglenoview=1<<8,      #1.9
#                             lockedcontents=1<<9,    #1.7
#                             )
#         annotationFlagValues['print']=1<<2

from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase.acroform import AcroForm
from reportlab.platypus.flowables import Flowable
import reportlab.pdfbase.pdfform as pdfform
import reportlab.pdfbase.acroform as acroform

VERTICAL = 0
HORIZONTAL = 1


class Ftextbox(Flowable):
    """TODO: Docstring for Ftextbox"""
    def __init__(self, fieldname='', value='', width=200, height=18, xoffset=0, yoffset=0, tooltip='', fontName=None, fontSize=12, fieldFlags=''):
        Flowable.__init__(self)
        self.fieldname = fieldname
        self.value = value
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.tooltip = tooltip
        self.fontname = fontName
        self.fontsize = fontSize
        self.fieldflags = fieldFlags

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        hcanvas = self.canv
        hcanvas.translate(self.xoffset, self.yoffset)
        hcanvas.acroForm.textfield(
            name=self.fieldname,
            tooltip=self.tooltip,
            value=self.value,
            x=self.xoffset, y=self.yoffset-2,
            width=self.width, height=self.height,
            # buttonStyle='diamond',
            # borderStyle='bevelled',
            borderWidth=1,
            borderColor=colors.grey,
            fillColor=colors.white,
            textColor=colors.black,
            forceBorder=True,
            relative=True, 
            fontName=self.fontname,
            fontSize=self.fontsize,
            fieldFlags=self.fieldflags)

        
class Fcheckbox(Flowable):
    """TODO: Docstring for Fcheckbox"""
    def __init__(self, fieldname='', value='', size=12, xoffset=0, yoffset=0, tooltip='', fontName=None, fontSize=12):
        Flowable.__init__(self)
        self.fieldname = fieldname
        self.value = value
        self.size = size
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.tooltip = tooltip
        self.fontname = fontName
        self.fontsize = fontSize

    def wrap(self, *args):
        return self.size, self.size

    def draw(self):
        hcanvas = self.canv
        hcanvas.translate(self.xoffset, self.yoffset)
        hcanvas.acroForm.checkbox(
            name=self.fieldname,
            tooltip=self.tooltip,
            checked=True,
            x=self.xoffset, y=self.yoffset-2,
            size=self.size, 
            # buttonStyle='diamond',
            # borderStyle='bevelled',
            borderWidth=1,
            borderColor=colors.black,
            fillColor=colors.white,
            textColor=colors.black,
            forceBorder=True,
            relative=True)

        if self.fontname is not None:
            hcanvas.setFont(self.fontname, self.fontsize)
        hcanvas.drawString(self.xoffset + self.size + 4, self.yoffset, self.value)


class Flistbox(Flowable):
    """TODO: Docstring for Flistbox"""
    def __init__(self, fieldname='', value='', options=['', ], width=120, height=36, xoffset=0, yoffset=0, tooltip='', fontName=None, fontSize=12, fieldFlags=''):
        Flowable.__init__(self)
        self.fieldname = fieldname
        self.value = value
        self.options = options
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.tooltip = tooltip
        self.fontname = fontName
        self.fontsize = fontSize
        self.fieldflags = fieldFlags

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        hcanvas = self.canv
        hcanvas.translate(self.xoffset, self.yoffset)
        hcanvas.acroForm.listbox(
            name=self.fieldname,
            tooltip=self.tooltip,
            value=self.value,
            options=self.options,
            x=self.xoffset, y=self.yoffset-2,
            # width=self.width, height=self.height,
            # buttonStyle='diamond',
            # borderStyle='bevelled',
            borderWidth=1,
            borderColor=colors.black,
            fillColor=colors.white,
            textColor=colors.black,
            forceBorder=True,
            relative=True, 
            fontName=self.fontname,
            fontSize=self.fontsize,
            fieldFlags=self.fieldflags)


class Fchoicebox(Flowable):
    """TODO: Docstring for Fchoicebox"""    
    def __init__(self, fieldname='', value='', options=['', ], width=120, height=36, xoffset=0, yoffset=0, tooltip='', fontName=None, fontSize=12, fieldFlags=''):
        Flowable.__init__(self)
        self.fieldname = fieldname
        self.value = value
        self.options = options
        self.width = width
        self.height = height
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.tooltip = tooltip
        self.fontname = fontName
        self.fontsize = fontSize
        self.fieldflags = fieldFlags

    def wrap(self, *args):
        return self.width, self.height

    def draw(self):
        hcanvas = self.canv
        hcanvas.translate(self.xoffset, self.yoffset)
        hcanvas.acroForm.choice(
            name=self.fieldname,
            tooltip=self.tooltip,
            value=self.value,
            options=self.options, 
            x=self.xoffset, y=self.yoffset-2,
            width=self.width, height=self.height,
            # buttonStyle='diamond',
            # borderStyle='bevelled',
            borderWidth=1,
            borderColor=colors.black,
            fillColor=colors.white,
            textColor=colors.black,
            forceBorder=True,
            relative=True, 
            fontName=self.fontname,
            fontSize=self.fontsize,
            fieldFlags=self.fieldflags)


class Fradiobox(Flowable):
    """TODO: Docstring for Fradiobox"""     
    def __init__(self, fieldname='', values=['1', '2'], selected=None, size=20, xoffset=0, yoffset=0, tooltip='', fontName=None, fontSize=12, direction=HORIZONTAL):
        Flowable.__init__(self)
        self.fieldname = fieldname
        self.values = values
        self.selected = selected
        self.size = size
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.tooltip = tooltip
        self.fontname = fontName
        self.fontsize = fontSize
        self.direction = direction
        group = acroform.RadioGroup(self.fieldname)

    def wrap(self, *args):
        i = len(self.values)
        if self.direction is HORIZONTAL:
            width = self.xoffset + i*(self.size + 2)  # TODO: Add Textwidth
            height = self.yoffset - self.size/2 - 2
        else:
            width = self.xoffset - self.size/2 - 2
            height = self.yoffset + i*(self.size + 2)
        
        return width, height

    def draw(self):
        hcanvas = self.canv
        hcanvas.translate(self.xoffset, self.yoffset)
        x = self.xoffset - self.size - 2
        for i, value in enumerate(self.values):  # in enumerate(reversed(self.values) if self.direction is VERTICAL else self.values):
            if self.direction is HORIZONTAL:
                x += self.size + 2  # self.xoffset+i*(self.size+2)
                y = self.yoffset - 3*self.size/2 - 2
            else:
                x = self.xoffset  # - self.size/2 - 2
                y = self.yoffset + i*(self.size + 2)

            hcanvas.acroForm.radio(
                name=self.fieldname,
                tooltip=self.tooltip,
                value=value,
                selected=True if i == self.selected else False,
                x=x, y=y,
                size=self.size,
                # buttonStyle='diamond',
                # borderStyle='bevelled',
                borderWidth=1,
                borderColor=colors.black,
                fillColor=colors.white,
                textColor=colors.black,
                forceBorder=True,
                relative=True)

            if self.fontname is not None:
                hcanvas.setFont(self.fontname, self.fontsize)
            if self.direction is HORIZONTAL:
                hcanvas.drawString(x + 5*self.size/4 + 1, y + self.size/4, value)
                x += hcanvas.stringWidth(value) + 5*self.size/4 + 1
            else:
                hcanvas.drawString(x + 5*self.size/4 + 2, y, value)
