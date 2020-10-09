# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
# Created by: PyQt5 UI code generator 5.15.0
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartConnectionForm(object):
    def setupUi(self, StartConnectionForm):
        StartConnectionForm.setObjectName("StartConnectionForm")
        StartConnectionForm.resize(421, 349)
        self.label = QtWidgets.QLabel(StartConnectionForm)
        self.label.setGeometry(QtCore.QRect(140, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StartConnectionForm)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(StartConnectionForm)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ipLineEdit = QtWidgets.QLineEdit(StartConnectionForm)
        self.ipLineEdit.setGeometry(QtCore.QRect(130, 120, 251, 20))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.portLineEdit = QtWidgets.QLineEdit(StartConnectionForm)
        self.portLineEdit.setGeometry(QtCore.QRect(130, 170, 251, 20))
        self.portLineEdit.setObjectName("portLineEdit")
        self.statusLabel = QtWidgets.QLabel(StartConnectionForm)
        self.statusLabel.setGeometry(QtCore.QRect(170, 220, 81, 16))
        self.statusLabel.setObjectName("statusLabel")
        self.connectBtn = QtWidgets.QPushButton(StartConnectionForm)
        self.connectBtn.setGeometry(QtCore.QRect(170, 280, 75, 23))
        self.connectBtn.setObjectName("connectBtn")

        self.retranslateUi(StartConnectionForm)
        QtCore.QMetaObject.connectSlotsByName(StartConnectionForm)

    def retranslateUi(self, StartConnectionForm):
        _translate = QtCore.QCoreApplication.translate
        StartConnectionForm.setWindowTitle(_translate("StartConnectionForm", "Form"))
        self.label.setText(_translate("StartConnectionForm", "Start Connection"))
        self.label_2.setText(_translate("StartConnectionForm", "TCP IP:"))
        self.label_3.setText(_translate("StartConnectionForm", "TCP Port:"))
        self.statusLabel.setText(_translate("StartConnectionForm", "Not Connected"))
        self.connectBtn.setText(_translate("StartConnectionForm", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartConnectionForm = QtWidgets.QWidget()
    ui = Ui_StartConnectionForm()
    ui.setupUi(StartConnectionForm)
    StartConnectionForm.show()
    sys.exit(app.exec_())
