# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License
# for more details.

from PyQt4 import QtGui, QtCore
import types
from openmolar.settings import localsettings
from xml.dom import minidom

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle(_("Select an Assitant"))

        layout = QtGui.QVBoxLayout(self)
        self.listwidget = QtGui.QListWidget()
        self.listwidget.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.listwidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)

        assistants = [_("NONE")] + localsettings.allowed_logins
        self.listwidget.addItems(assistants)

        self.listwidget.setCurrentRow(0)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        layout.addWidget(self.listwidget)
        layout.addWidget(self.buttonBox)

        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.accept)
        self.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), self.reject)


    @property
    def selectedAssistant(self):
        if self.listwidget.currentRow() == 0:
            return ""
        return str(self.listwidget.currentItem().text().toAscii())

    def result(self):
        if self.exec_():
            u2 = self.selectedAssistant
            localsettings.setOperator(localsettings.clinicianInits, u2)
            return (True, u2)
        return (False, None)

if __name__ == "__main__":
    from openmolar.qt4gui import resources_rc
    localsettings.initiateUsers()
    app = QtGui.QApplication([])
    ui = Dialog()
    print ui.result()
    app.closeAllWindows()
