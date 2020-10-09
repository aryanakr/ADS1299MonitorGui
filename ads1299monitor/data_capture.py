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

from .data_capture_settings_form import Ui_DataCaptureInitialSettingsForm
from .data_capture_form import Ui_DataCaptureForm


class DataCaptureSetup(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.data_settings_form = Ui_DataCaptureInitialSettingsForm()
        self.data_settings_form.setupUi(self)

        self.save_location = ''
        self.data_settings_form.saveLocationButton.clicked.connect(self.get_save_location)

        self.data_settings_form.saveButton.clicked.connect(self.create_profile)
        self.data_settings_form.saveTypeComboBox.addItem("csv")
        self.data_settings_form.saveTypeComboBox.addItem("xlsx")

    def get_save_location(self):
        dialog = qtw.QFileDialog()
        self.save_location = dialog.getExistingDirectory(self, 'Select a directory to save data')
        self.data_settings_form.SaveLocationLabel.setText(self.save_location)

    def create_profile(self):
        path = self.save_location + '/' + self.data_settings_form.captureName.text()
        if not os.path.exists(path):
            os.makedirs(path)
        filename = self.data_settings_form.captureName.text() + '.adsrecprofile'
        with open(os.path.join(path, filename), 'w+') as f:
            f.write(self.data_settings_form.captureName.text())
            f.write(',' + self.data_settings_form.dataLimitSpinBox.text())
            f.write(',0')
            f.write(',' + self.data_settings_form.saveTypeComboBox.currentText())

            # Channels to use setting
            f.write(',' + str(self.data_settings_form.cBchannel1.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel2.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel3.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel4.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel5.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel6.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel7.checkState()))
            f.write(',' + str(self.data_settings_form.cBchannel8.checkState()))

            # Categories Setting
            if self.data_settings_form.cat1Name.text() != '':
                f.write(','+self.data_settings_form.cat1Name.text())

            if self.data_settings_form.cat2Name.text() != '':
                f.write(','+self.data_settings_form.cat2Name.text())

            if self.data_settings_form.cat3Name.text() != '':
                f.write(','+self.data_settings_form.cat3Name.text())

            if self.data_settings_form.cat4Name.text() != '':
                f.write(','+self.data_settings_form.cat4Name.text())

            if self.data_settings_form.cat5Name.text() != '':
                f.write(','+self.data_settings_form.cat5Name.text())

            if self.data_settings_form.cat6Name.text() != '':
                f.write(','+self.data_settings_form.cat6Name.text())

            if self.data_settings_form.cat7Name.text() != '':
                f.write(','+self.data_settings_form.cat7Name.text())

            if self.data_settings_form.cat8Name.text() != '':
                f.write(','+self.data_settings_form.cat8Name.text())

        self.data_settings_form.retranslateUi(self)
        self.close()


class DataCapture(qtw.QWidget):
    startRecord = qtc.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.data_capture_form = Ui_DataCaptureForm()
        self.data_capture_form.setupUi(self)

        self.settings_file = ''
        self.save_location = ''
        self.save_type = ''
        self.data_limit = 0
        self.data_count = 0
        self.selected_channels = []
        self.categories = []

    def set_params(self, filename):
        self.settings_file = filename
        with open(filename, 'r') as f:
            setting_string = f.readline().strip()

        settings_list = setting_string.split(',')

        self.save_location = os.path.dirname(os.path.abspath(filename))

        self.data_capture_form.captureNameLabel.setText(settings_list[0])
        self.data_limit = settings_list[1]
        self.data_count = settings_list[2]
        self.save_type = settings_list[3]
        self.selected_channels = settings_list[4:12]
        self.categories = settings_list[12:]
        for cat in self.categories:
            self.data_capture_form.categoryComboBox.addItem(cat)

    def finalize_record(self):
        self.data_capture_form.statusLabel.setText("Done!")
        self.data_count = int(self.data_count) + 1

        with open(self.settings_file, 'w+') as f:
            f.write(self.data_capture_form.captureNameLabel.text())
            f.write(',' + self.data_limit)
            f.write(',' + str(self.data_count))
            f.write(',' + self.save_type)
            for channel in self.selected_channels:
                f.write(',' + channel)
            for cat in self.categories:
                f.write(',' + cat)
