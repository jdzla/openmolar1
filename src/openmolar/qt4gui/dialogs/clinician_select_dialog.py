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
        self.setWindowTitle(_("Select a Clinician"))

        layout = QtGui.QVBoxLayout(self)
        self.listwidget = QtGui.QListWidget()
        self.listwidget.setSelectionBehavior(
            QtGui.QAbstractItemView.SelectRows)
        self.listwidget.setSelectionMode(
            QtGui.QAbstractItemView.SingleSelection)

        clinicians = [_("NONE")] + localsettings.activedents + \
            localsettings.activehygs
        self.listwidget.addItems(clinicians)

        try:
            i = clinicians.index(localsettings.clinicianInits)
        except ValueError:
            i = 0
        self.listwidget.setCurrentRow(i)

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
    def selectedClinician(self):
        if self.listwidget.currentRow() == 0:
            return ""
        return str(self.listwidget.currentItem().text().toAscii())

    def result(self):
        if self.exec_():
            chosen = self.selectedClinician
            change_needed = chosen != localsettings.clinicianInits
            localsettings.clinicianInits = chosen
            localsettings.clinicianNo = localsettings.ops_reverse.get(
                chosen, 0)
            curr_operator = localsettings.operator.split("/")
            u2 = curr_operator[-1]
            if u2 == chosen:
                u2 = ""
            if u2:
                input = QtGui.QMessageBox.question(self, _("Confirm"),
                _("Set assistant as") + " %s?"% u2,
                QtGui.QMessageBox.No | QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.Yes )
                if input == QtGui.QMessageBox.No:
                    u2 = ""
            localsettings.setOperator(chosen, u2)
            return (change_needed, chosen)
        return (False, None)

if __name__ == "__main__":
    from openmolar.qt4gui import resources_rc
    localsettings.initiate()
    app = QtGui.QApplication([])
    ui = Dialog()
    print ui.result()
    app.closeAllWindows()
