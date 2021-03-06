# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# See the GNU General Public License for more details.
from __future__ import division

from PyQt4 import QtCore,QtGui
from openmolar.settings import localsettings

import datetime

class Receipt(object):

    def __init__(self):
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A5)
        self.pdfprinter = QtGui.QPrinter()
        self.pdfprinter.setPageSize(QtGui.QPrinter.A5)
        self.setProps()
        self.receivedDict={}
        self.isDuplicate=False
        self.dupdate=QtCore.QDate.currentDate()

    def setProps(self, tit="", fn="", sn="", ad1="", ad2="", ad3="",
    ad4="", ad5="", pcd="", p="", n="", s="", t=""):

        self.title=tit
        self.fname=fn
        self.sname=sn
        self.addr1=ad1
        self.addr2=ad2
        self.addr3=ad3
        self.town=ad4
        self.county=ad5
        self.pcde=pcd
        self.pamount=p
        self.namount=n
        self.samount=s
        self.total=t

    def print_(self):
        dialog = QtGui.QPrintDialog(self.printer)
        if not dialog.exec_():
            return
        self.pdfprinter.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.pdfprinter.setOutputFileName(localsettings.TEMP_PDF)

        for printer in (self.printer,self.pdfprinter):

            LeftMargin = 50
            TopMargin = 150
            serifFont = QtGui.QFont("Times", 11)
            fm=QtGui.QFontMetrics(serifFont)
            serifLineHeight = fm.height()
            painter = QtGui.QPainter(printer)
            pageRect = printer.pageRect()
            painter.setPen(QtCore.Qt.black)
            painter.setFont(serifFont)
            center = QtGui.QTextOption(QtCore.Qt.AlignCenter)
            alignRight = QtGui.QTextOption(QtCore.Qt.AlignRight)
            if self.isDuplicate:
                painter.drawText(QtCore.QRectF(0, 100,pageRect.width()\
                ,serifLineHeight),\
                QtCore.QString("DUPLICATE RECEIPT"),
                center)

            x,y = LeftMargin,TopMargin+30
            painter.drawText(x, y, "%s %s %s"%(self.title.title(),self.fname.title(),self.sname.title()))
            y += serifLineHeight
            for line in (self.addr1,self.addr2,self.addr3,self.town,self.county):
                if line!="":
                    painter.drawText(x, y, str(line).title()+",")
                    y += serifLineHeight
            if self.pcde!="":
                painter.drawText(x, y, str(self.pcde+"."))  #postcode


            x,y=LeftMargin+50,TopMargin+serifLineHeight*10
            mystr='Received on  '
            w=fm.width(mystr)
            painter.drawText(x, y, mystr)
            if not self.isDuplicate:
                painter.drawText(x+w, y,
                QtCore.QDate.currentDate().toString(
                    localsettings.QDATE_FORMAT))
            else:
                painter.drawText(x+w, y, self.dupdate.toString(
                    localsettings.QDATE_FORMAT))

            y += serifLineHeight*2


            painter.drawText(x, y, QtCore.QString('relating to:-'))
            y += serifLineHeight

            for key in self.receivedDict.keys():
                amount=self.receivedDict[key]
                if float(amount) != 0:
                    rect_f = QtCore.QRectF(x,y,180,serifLineHeight)
                    painter.drawText(rect_f, QtCore.QString(key))

                    rect_f = QtCore.QRectF(x+180, y,100,serifLineHeight)
                    text = QtCore.QString(localsettings.formatMoney(amount))
                    painter.drawText(rect_f , text, alignRight)

                    y += serifLineHeight


            y += serifLineHeight

            painter.drawLine(int(x),int(y),int(x)+280,int(y))#130+150=280
            y += serifLineHeight*1.5

            rect_f = QtCore.QRectF(x,y,180,serifLineHeight)
            painter.drawText(rect_f, "TOTAL")

            rect_f = QtCore.QRectF(x+180, y,100,serifLineHeight)
            text = QtCore.QString(localsettings.formatMoney(self.total))
            painter.drawText(rect_f, text, alignRight)

            y += serifLineHeight*4

            font = QtGui.QFont("Helvetica", 7)
            font.setItalic(True)
            painter.setFont(font)
            painter.drawText(x, y, _("Thankyou for your custom."))
        return True

if __name__ == "__main__":
    import os
    os.chdir(os.path.expanduser("~"))

    localsettings.initiate()
    app = QtGui.QApplication([])
    myreceipt = Receipt()
    myreceipt.title = "tit"
    myreceipt.fname ="fname"
    myreceipt.sname ="sname"
    myreceipt.addr1 ="addr1"
    myreceipt.addr2 ="addr2"
    myreceipt.addr3 ="addr3"
    myreceipt.town ="addr4"
    myreceipt.county ="addr5"
    myreceipt.pcde ="PCDE"
    myreceipt.receivedDict ={
        "Private Treatment":"10.00",
        "NHS Treatment":"20.00",
        "Cuddly Toy":"5.00",
        "Sundry Items":"30.00"
        }
    myreceipt.total = "65.00"
    myreceipt.isDuplicate = True
    myreceipt.dupdate = QtCore.QDate(2009,3,2)
    myreceipt.print_()

