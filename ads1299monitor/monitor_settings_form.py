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


class Ui_MonitorSettings(object):
    def setupUi(self, MonitorSettings):
        MonitorSettings.setObjectName("MonitorSettings")
        MonitorSettings.resize(433, 267)
        self.label = QtWidgets.QLabel(MonitorSettings)
        self.label.setGeometry(QtCore.QRect(150, 20, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ch1CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch1CB.setGeometry(QtCore.QRect(40, 90, 71, 18))
        self.ch1CB.setObjectName("ch1CB")
        self.ch5CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch5CB.setGeometry(QtCore.QRect(40, 130, 71, 18))
        self.ch5CB.setObjectName("ch5CB")
        self.ch6CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch6CB.setGeometry(QtCore.QRect(140, 130, 71, 18))
        self.ch6CB.setObjectName("ch6CB")
        self.ch2CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch2CB.setGeometry(QtCore.QRect(140, 90, 71, 18))
        self.ch2CB.setObjectName("ch2CB")
        self.ch7CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch7CB.setGeometry(QtCore.QRect(230, 130, 71, 18))
        self.ch7CB.setObjectName("ch7CB")
        self.ch3CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch3CB.setGeometry(QtCore.QRect(230, 90, 71, 18))
        self.ch3CB.setObjectName("ch3CB")
        self.ch8CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch8CB.setGeometry(QtCore.QRect(330, 130, 71, 18))
        self.ch8CB.setObjectName("ch8CB")
        self.ch4CB = QtWidgets.QCheckBox(MonitorSettings)
        self.ch4CB.setGeometry(QtCore.QRect(330, 90, 71, 18))
        self.ch4CB.setObjectName("ch4CB")
        self.submitBtn = QtWidgets.QPushButton(MonitorSettings)
        self.submitBtn.setGeometry(QtCore.QRect(180, 220, 75, 23))
        self.submitBtn.setObjectName("submitBtn")
        self.checkBox = QtWidgets.QCheckBox(MonitorSettings)
        self.checkBox.setGeometry(QtCore.QRect(150, 180, 131, 18))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(MonitorSettings)
        QtCore.QMetaObject.connectSlotsByName(MonitorSettings)

    def retranslateUi(self, MonitorSettings):
        _translate = QtCore.QCoreApplication.translate
        MonitorSettings.setWindowTitle(_translate("MonitorSettings", "Form"))
        self.label.setText(_translate("MonitorSettings", "Monitor Setting"))
        self.ch1CB.setText(_translate("MonitorSettings", "Channel 1"))
        self.ch5CB.setText(_translate("MonitorSettings", "Channel 5"))
        self.ch6CB.setText(_translate("MonitorSettings", "Channel 6"))
        self.ch2CB.setText(_translate("MonitorSettings", "Channel 2"))
        self.ch7CB.setText(_translate("MonitorSettings", "Channel 7"))
        self.ch3CB.setText(_translate("MonitorSettings", "Channel 3"))
        self.ch8CB.setText(_translate("MonitorSettings", "Channel 8"))
        self.ch4CB.setText(_translate("MonitorSettings", "Channel 4"))
        self.submitBtn.setText(_translate("MonitorSettings", "Submit"))
        self.checkBox.setText(_translate("MonitorSettings", "Show Lead-Off Status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MonitorSettings = QtWidgets.QWidget()
    ui = Ui_MonitorSettings()
    ui.setupUi(MonitorSettings)
    MonitorSettings.show()
    sys.exit(app.exec_())
