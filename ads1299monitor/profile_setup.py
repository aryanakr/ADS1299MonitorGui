# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

import os

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from .profile_registration_form import Ui_ProfileRegistration


class CreateProfileWidget(qtw.QMainWindow):
    submitted = qtc.pyqtSignal()

    def __init__(self):
        """MainWindow Constructor"""
        super().__init__()
        self.registration_form = Ui_ProfileRegistration()
        self.registration_form.setupUi(self)

        self.registration_form.create_profile_btn.clicked.connect(self.create_profile_file)

    def create_profile_file(self):
        path = os.getcwd() + '/profiles'
        if not os.path.exists(path):
            os.makedirs(path)
        filename = self.registration_form.name_field.text() + '.adsregprofile'
        with open(os.path.join(path, filename), 'w+') as tmp_file:
            tmp_file.write("CONFIG1:")
            tmp_file.write(self.registration_form.config1_field.text())

            tmp_file.write(",CONFIG2:")
            tmp_file.write(self.registration_form.config2_field.text())

            tmp_file.write(",CONFIG3:")
            tmp_file.write(self.registration_form.config3_field.text())

            tmp_file.write(",LOFF:")
            tmp_file.write(self.registration_form.loff_field.text())

            tmp_file.write(",CH1SET:")
            tmp_file.write(self.registration_form.ch1_field.text())

            tmp_file.write(",CH2SET:")
            tmp_file.write(self.registration_form.ch2_field.text())

            tmp_file.write(",CH3SET:")
            tmp_file.write(self.registration_form.ch3_field.text())

            tmp_file.write(",CH4SET:")
            tmp_file.write(self.registration_form.ch4_field.text())

            tmp_file.write(",CH5SET:")
            tmp_file.write(self.registration_form.ch5_field.text())

            tmp_file.write(",CH6SET:")
            tmp_file.write(self.registration_form.ch6_field.text())

            tmp_file.write(",CH7SET:")
            tmp_file.write(self.registration_form.ch7_field.text())

            tmp_file.write(",CH8SET:")
            tmp_file.write(self.registration_form.ch8_field.text())

            tmp_file.write(",BIAS_SENSP:")
            tmp_file.write(self.registration_form.biassensp_field.text())

            tmp_file.write(",BIAS_SENSN:")
            tmp_file.write(self.registration_form.biassensn_field.text())

            tmp_file.write(",LOFF_SENSP:")
            tmp_file.write(self.registration_form.loffsensp_field.text())

            tmp_file.write(",LOFF_SENSN:")
            tmp_file.write(self.registration_form.loffsensn_field.text())

            tmp_file.write(",LOFF_FLIP:")
            tmp_file.write(self.registration_form.loffflip_field.text())

            tmp_file.write(",MISC1:")
            tmp_file.write(self.registration_form.misc1_field.text())

            tmp_file.write(",MISC2:")
            tmp_file.write(self.registration_form.misc2_field.text())

            tmp_file.write(",GPIO:")
            tmp_file.write(self.registration_form.gpio_field.text())

            tmp_file.write(",CONFIG4:")
            tmp_file.write(self.registration_form.config4_field.text())

        self.registration_form.retranslateUi(self)
        self.submitted.emit()
        self.close()

    def closeEvent(self, event):
        self.registration_form.retranslateUi(self)
