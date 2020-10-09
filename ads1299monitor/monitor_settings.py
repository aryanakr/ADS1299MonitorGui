# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from .monitor_settings_form import Ui_MonitorSettings


class MonitorSettingsWidget(qtw.QWidget):
    submitted = qtc.pyqtSignal(list)

    def __init__(self):
        super().__init__()

        self.monitor_settings_form = Ui_MonitorSettings()
        self.monitor_settings_form.setupUi(self)

        self.monitor_settings_form.submitBtn.clicked.connect(self.submit_settings)

    def submit_settings(self):

        settings = [self.monitor_settings_form.ch1CB.checkState(), self.monitor_settings_form.ch2CB.checkState(),
                    self.monitor_settings_form.ch3CB.checkState(), self.monitor_settings_form.ch4CB.checkState(),
                    self.monitor_settings_form.ch5CB.checkState(), self.monitor_settings_form.ch6CB.checkState(),
                    self.monitor_settings_form.ch7CB.checkState(), self.monitor_settings_form.ch8CB.checkState(),
                    self.monitor_settings_form.checkBox.checkState()]
        # Show lead off window is checkBox :D (Forgot to change the default name)
        self.submitted.emit(settings)
        self.close()
