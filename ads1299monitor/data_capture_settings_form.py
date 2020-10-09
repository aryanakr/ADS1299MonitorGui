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


class Ui_DataCaptureInitialSettingsForm(object):
    def setupUi(self, DataCaptureInitialSettingsForm):
        DataCaptureInitialSettingsForm.setObjectName("DataCaptureInitialSettingsForm")
        DataCaptureInitialSettingsForm.resize(606, 642)
        self.label = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label.setGeometry(QtCore.QRect(200, 20, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.saveLocationButton = QtWidgets.QPushButton(DataCaptureInitialSettingsForm)
        self.saveLocationButton.setGeometry(QtCore.QRect(30, 160, 91, 31))
        self.saveLocationButton.setObjectName("saveLocationButton")
        self.SaveLocationLabel = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.SaveLocationLabel.setGeometry(QtCore.QRect(130, 170, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SaveLocationLabel.setFont(font)
        self.SaveLocationLabel.setObjectName("SaveLocationLabel")
        self.dataLimitSpinBox = QtWidgets.QSpinBox(DataCaptureInitialSettingsForm)
        self.dataLimitSpinBox.setGeometry(QtCore.QRect(140, 230, 121, 22))
        self.dataLimitSpinBox.setMaximum(5000)
        self.dataLimitSpinBox.setSingleStep(100)
        self.dataLimitSpinBox.setObjectName("dataLimitSpinBox")
        self.label_2 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_2.setGeometry(QtCore.QRect(30, 230, 101, 16))
        self.label_2.setObjectName("label_2")
        self.cat1Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat1Name.setGeometry(QtCore.QRect(110, 290, 161, 20))
        self.cat1Name.setObjectName("cat1Name")
        self.cat2Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat2Name.setGeometry(QtCore.QRect(110, 330, 161, 20))
        self.cat2Name.setObjectName("cat2Name")
        self.cat3Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat3Name.setGeometry(QtCore.QRect(110, 370, 161, 20))
        self.cat3Name.setObjectName("cat3Name")
        self.cat4Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat4Name.setGeometry(QtCore.QRect(110, 410, 161, 20))
        self.cat4Name.setObjectName("cat4Name")
        self.cat5Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat5Name.setGeometry(QtCore.QRect(420, 290, 161, 20))
        self.cat5Name.setObjectName("cat5Name")
        self.cat6Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat6Name.setGeometry(QtCore.QRect(420, 330, 161, 20))
        self.cat6Name.setObjectName("cat6Name")
        self.cat7Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat7Name.setGeometry(QtCore.QRect(420, 370, 161, 20))
        self.cat7Name.setObjectName("cat7Name")
        self.cat8Name = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.cat8Name.setGeometry(QtCore.QRect(420, 410, 161, 20))
        self.cat8Name.setObjectName("cat8Name")
        self.label_3 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_5.setGeometry(QtCore.QRect(30, 370, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_6.setGeometry(QtCore.QRect(30, 410, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_7.setGeometry(QtCore.QRect(340, 290, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_8.setGeometry(QtCore.QRect(340, 330, 71, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_9.setGeometry(QtCore.QRect(340, 370, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_10.setGeometry(QtCore.QRect(340, 410, 71, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_11.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.label_11.setObjectName("label_11")
        self.captureName = QtWidgets.QLineEdit(DataCaptureInitialSettingsForm)
        self.captureName.setGeometry(QtCore.QRect(150, 100, 161, 20))
        self.captureName.setObjectName("captureName")
        self.saveButton = QtWidgets.QPushButton(DataCaptureInitialSettingsForm)
        self.saveButton.setGeometry(QtCore.QRect(250, 600, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.label_12 = QtWidgets.QLabel(DataCaptureInitialSettingsForm)
        self.label_12.setGeometry(QtCore.QRect(30, 470, 47, 13))
        self.label_12.setObjectName("label_12")
        self.saveTypeComboBox = QtWidgets.QComboBox(DataCaptureInitialSettingsForm)
        self.saveTypeComboBox.setGeometry(QtCore.QRect(110, 470, 111, 22))
        self.saveTypeComboBox.setObjectName("saveTypeComboBox")
        self.cBchannel1 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel1.setGeometry(QtCore.QRect(330, 460, 111, 18))
        self.cBchannel1.setObjectName("cBchannel1")
        self.cBchannel2 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel2.setGeometry(QtCore.QRect(330, 490, 111, 18))
        self.cBchannel2.setObjectName("cBchannel2")
        self.cBchannel3 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel3.setGeometry(QtCore.QRect(330, 520, 111, 18))
        self.cBchannel3.setObjectName("cBchannel3")
        self.cBchannel4 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel4.setGeometry(QtCore.QRect(330, 550, 111, 18))
        self.cBchannel4.setObjectName("cBchannel4")
        self.cBchannel8 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel8.setGeometry(QtCore.QRect(460, 550, 111, 18))
        self.cBchannel8.setObjectName("cBchannel8")
        self.cBchannel7 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel7.setGeometry(QtCore.QRect(460, 520, 111, 18))
        self.cBchannel7.setObjectName("cBchannel7")
        self.cBchannel6 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel6.setGeometry(QtCore.QRect(460, 490, 111, 18))
        self.cBchannel6.setObjectName("cBchannel6")
        self.cBchannel5 = QtWidgets.QCheckBox(DataCaptureInitialSettingsForm)
        self.cBchannel5.setGeometry(QtCore.QRect(460, 460, 111, 18))
        self.cBchannel5.setObjectName("cBchannel5")

        self.retranslateUi(DataCaptureInitialSettingsForm)
        QtCore.QMetaObject.connectSlotsByName(DataCaptureInitialSettingsForm)

    def retranslateUi(self, DataCaptureInitialSettingsForm):
        _translate = QtCore.QCoreApplication.translate
        DataCaptureInitialSettingsForm.setWindowTitle(_translate("DataCaptureInitialSettingsForm", "Form"))
        self.label.setText(_translate("DataCaptureInitialSettingsForm", "New Data Capture Profile"))
        self.saveLocationButton.setText(_translate("DataCaptureInitialSettingsForm", "Select Folder"))
        self.SaveLocationLabel.setText(_translate("DataCaptureInitialSettingsForm", "Save"))
        self.label_2.setText(_translate("DataCaptureInitialSettingsForm", "Number of Points:"))
        self.label_3.setText(_translate("DataCaptureInitialSettingsForm", "Category 1:"))
        self.label_4.setText(_translate("DataCaptureInitialSettingsForm", "Category 2:"))
        self.label_5.setText(_translate("DataCaptureInitialSettingsForm", "Category 3:"))
        self.label_6.setText(_translate("DataCaptureInitialSettingsForm", "Category 4:"))
        self.label_7.setText(_translate("DataCaptureInitialSettingsForm", "Category 5:"))
        self.label_8.setText(_translate("DataCaptureInitialSettingsForm", "Category 6:"))
        self.label_9.setText(_translate("DataCaptureInitialSettingsForm", "Category 7:"))
        self.label_10.setText(_translate("DataCaptureInitialSettingsForm", "Category 8:"))
        self.label_11.setText(_translate("DataCaptureInitialSettingsForm", "Data Capture Name:"))
        self.saveButton.setText(_translate("DataCaptureInitialSettingsForm", "Save"))
        self.label_12.setText(_translate("DataCaptureInitialSettingsForm", "Save As:"))
        self.cBchannel1.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 1"))
        self.cBchannel2.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 2"))
        self.cBchannel3.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 3"))
        self.cBchannel4.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 4"))
        self.cBchannel8.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 8"))
        self.cBchannel7.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 7"))
        self.cBchannel6.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 6"))
        self.cBchannel5.setText(_translate("DataCaptureInitialSettingsForm", "Record Channel 5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataCaptureInitialSettingsForm = QtWidgets.QWidget()
    ui = Ui_DataCaptureInitialSettingsForm()
    ui.setupUi(DataCaptureInitialSettingsForm)
    DataCaptureInitialSettingsForm.show()
    sys.exit(app.exec_())
