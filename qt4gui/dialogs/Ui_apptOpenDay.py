# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openmolar/openmolar/qt-designer/apptOpenDay.ui'
#
# Created: Fri Jun 19 12:56:56 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 360)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 2)
        spacerItem = QtGui.QSpacerItem(86, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 3, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(73, 25, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(58, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.dayStart_timeEdit = QtGui.QTimeEdit(Dialog)
        self.dayStart_timeEdit.setObjectName("dayStart_timeEdit")
        self.gridLayout.addWidget(self.dayStart_timeEdit, 3, 4, 1, 1)
        self.es1_checkBox = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.es1_checkBox.sizePolicy().hasHeightForWidth())
        self.es1_checkBox.setSizePolicy(sizePolicy)
        self.es1_checkBox.setObjectName("es1_checkBox")
        self.gridLayout.addWidget(self.es1_checkBox, 4, 0, 2, 3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.es1Start_timeEdit = QtGui.QTimeEdit(Dialog)
        self.es1Start_timeEdit.setObjectName("es1Start_timeEdit")
        self.gridLayout.addWidget(self.es1Start_timeEdit, 4, 4, 2, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 5, 1, 1)
        self.es1Finish_timeEdit = QtGui.QTimeEdit(Dialog)
        self.es1Finish_timeEdit.setObjectName("es1Finish_timeEdit")
        self.gridLayout.addWidget(self.es1Finish_timeEdit, 4, 6, 2, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 3, 1, 1)
        self.lunchStart_timeEdit = QtGui.QTimeEdit(Dialog)
        self.lunchStart_timeEdit.setObjectName("lunchStart_timeEdit")
        self.gridLayout.addWidget(self.lunchStart_timeEdit, 6, 4, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 5, 1, 1)
        self.lunchFinish_timeEdit = QtGui.QTimeEdit(Dialog)
        self.lunchFinish_timeEdit.setObjectName("lunchFinish_timeEdit")
        self.gridLayout.addWidget(self.lunchFinish_timeEdit, 6, 6, 1, 1)
        self.es2_checkBox = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.es2_checkBox.sizePolicy().hasHeightForWidth())
        self.es2_checkBox.setSizePolicy(sizePolicy)
        self.es2_checkBox.setObjectName("es2_checkBox")
        self.gridLayout.addWidget(self.es2_checkBox, 7, 0, 1, 3)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 3, 1, 1)
        self.es2Start_timeEdit = QtGui.QTimeEdit(Dialog)
        self.es2Start_timeEdit.setObjectName("es2Start_timeEdit")
        self.gridLayout.addWidget(self.es2Start_timeEdit, 7, 4, 1, 1)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 5, 1, 1)
        self.es2Finish_timeEdit = QtGui.QTimeEdit(Dialog)
        self.es2Finish_timeEdit.setObjectName("es2Finish_timeEdit")
        self.gridLayout.addWidget(self.es2Finish_timeEdit, 7, 6, 1, 1)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 5, 1, 1)
        self.dayFinish_timeEdit = QtGui.QTimeEdit(Dialog)
        self.dayFinish_timeEdit.setObjectName("dayFinish_timeEdit")
        self.gridLayout.addWidget(self.dayFinish_timeEdit, 8, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 7)
        self.lunch_checkBox = QtGui.QCheckBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lunch_checkBox.sizePolicy().hasHeightForWidth())
        self.lunch_checkBox.setSizePolicy(sizePolicy)
        self.lunch_checkBox.setObjectName("lunch_checkBox")
        self.gridLayout.addWidget(self.lunch_checkBox, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.dayStart_timeEdit)
        Dialog.setTabOrder(self.dayStart_timeEdit, self.es1_checkBox)
        Dialog.setTabOrder(self.es1_checkBox, self.es1Start_timeEdit)
        Dialog.setTabOrder(self.es1Start_timeEdit, self.es1Finish_timeEdit)
        Dialog.setTabOrder(self.es1Finish_timeEdit, self.lunchStart_timeEdit)
        Dialog.setTabOrder(self.lunchStart_timeEdit, self.lunchFinish_timeEdit)
        Dialog.setTabOrder(self.lunchFinish_timeEdit, self.es2_checkBox)
        Dialog.setTabOrder(self.es2_checkBox, self.es2Start_timeEdit)
        Dialog.setTabOrder(self.es2Start_timeEdit, self.es2Finish_timeEdit)
        Dialog.setTabOrder(self.es2Finish_timeEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Open a Day", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Clinician", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Date to Open", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Day Start", None, QtGui.QApplication.UnicodeUTF8))
        self.es1_checkBox.setText(QtGui.QApplication.translate("Dialog", "Morning Emergency Slot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.es2_checkBox.setText(QtGui.QApplication.translate("Dialog", "Afternoon Emergency Slot ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "Day Finish", None, QtGui.QApplication.UnicodeUTF8))
        self.lunch_checkBox.setText(QtGui.QApplication.translate("Dialog", "Lunch", None, QtGui.QApplication.UnicodeUTF8))
