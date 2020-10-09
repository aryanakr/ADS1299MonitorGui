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


class Ui_profileSelectForm(object):
    def setupUi(self, profileSelectForm):
        profileSelectForm.setObjectName("profileSelectForm")
        profileSelectForm.resize(425, 323)
        profileSelectForm.setMinimumSize(QtCore.QSize(425, 323))
        profileSelectForm.setMaximumSize(QtCore.QSize(425, 323))
        self.label = QtWidgets.QLabel(profileSelectForm)
        self.label.setGeometry(QtCore.QRect(110, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.profileComboBox = QtWidgets.QComboBox(profileSelectForm)
        self.profileComboBox.setGeometry(QtCore.QRect(110, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.profileComboBox.setFont(font)
        self.profileComboBox.setObjectName("profileComboBox")
        self.profileComboBox.addItem("")
        self.profileSubmitBtn = QtWidgets.QPushButton(profileSelectForm)
        self.profileSubmitBtn.setEnabled(False)
        self.profileSubmitBtn.setGeometry(QtCore.QRect(170, 200, 81, 31))
        self.profileSubmitBtn.setObjectName("profileSubmitBtn")
        self.configureProfileBtn = QtWidgets.QPushButton(profileSelectForm)
        self.configureProfileBtn.setGeometry(QtCore.QRect(170, 140, 81, 31))
        self.configureProfileBtn.setObjectName("configureProfileBtn")

        self.retranslateUi(profileSelectForm)
        QtCore.QMetaObject.connectSlotsByName(profileSelectForm)

    def retranslateUi(self, profileSelectForm):
        _translate = QtCore.QCoreApplication.translate
        profileSelectForm.setWindowTitle(_translate("profileSelectForm", "Form"))
        self.label.setText(_translate("profileSelectForm", "Select Registers Profile"))
        self.profileComboBox.setItemText(0, _translate("profileSelectForm", "Default Profile"))
        self.profileSubmitBtn.setText(_translate("profileSelectForm", "Submit"))
        self.configureProfileBtn.setText(_translate("profileSelectForm", "Configure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profileSelectForm = QtWidgets.QWidget()
    ui = Ui_profileSelectForm()
    ui.setupUi(profileSelectForm)
    profileSelectForm.show()
    sys.exit(app.exec_())
