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


class Ui_DataCaptureForm(object):
    def setupUi(self, DataCaptureForm):
        DataCaptureForm.setObjectName("DataCaptureForm")
        DataCaptureForm.resize(408, 287)
        self.captureNameLabel = QtWidgets.QLabel(DataCaptureForm)
        self.captureNameLabel.setGeometry(QtCore.QRect(40, 30, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.captureNameLabel.setFont(font)
        self.captureNameLabel.setObjectName("captureNameLabel")
        self.categoryComboBox = QtWidgets.QComboBox(DataCaptureForm)
        self.categoryComboBox.setGeometry(QtCore.QRect(40, 110, 181, 21))
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.recordButton = QtWidgets.QPushButton(DataCaptureForm)
        self.recordButton.setGeometry(QtCore.QRect(270, 100, 71, 41))
        self.recordButton.setObjectName("recordButton")
        self.statusLabel = QtWidgets.QLabel(DataCaptureForm)
        self.statusLabel.setGeometry(QtCore.QRect(40, 190, 171, 16))
        self.statusLabel.setObjectName("statusLabel")

        self.retranslateUi(DataCaptureForm)
        QtCore.QMetaObject.connectSlotsByName(DataCaptureForm)

    def retranslateUi(self, DataCaptureForm):
        _translate = QtCore.QCoreApplication.translate
        DataCaptureForm.setWindowTitle(_translate("DataCaptureForm", "Form"))
        self.captureNameLabel.setText(_translate("DataCaptureForm", "TextLabel"))
        self.recordButton.setText(_translate("DataCaptureForm", "Record"))
        self.statusLabel.setText(_translate("DataCaptureForm", "Status: Idle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataCaptureForm = QtWidgets.QWidget()
    ui = Ui_DataCaptureForm()
    ui.setupUi(DataCaptureForm)
    DataCaptureForm.show()
    sys.exit(app.exec_())
