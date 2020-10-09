# -----------------------------------------------------------
# ads1299 MIT monitoring software v-1.0
#
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

from PyQt5 import QtWidgets as qtw

from .leadoff_status_form import Ui_LeadoffStatus


class LeadOffStatusMonitorWidget(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.leadoff_monitor_form = Ui_LeadoffStatus()
        self.leadoff_monitor_form.setupUi(self)

    def update_status(self, status_bits):

        status_str = str(bin(int(status_bits)))
        if len(status_str) < 22:
            return

        # Update positive channels status
        self.leadoff_monitor_form.statusChannel1P.setText('ON' if status_str[13] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel2P.setText('ON' if status_str[12] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel3P.setText('ON' if status_str[11] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel4P.setText('ON' if status_str[10] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel5P.setText('ON' if status_str[9] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel6P.setText('ON' if status_str[8] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel7P.setText('ON' if status_str[7] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel8P.setText('ON' if status_str[6] == '1' else 'OFF')
        # Update negative channels status
        self.leadoff_monitor_form.statusChannel1N.setText('ON' if status_str[21] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel2N.setText('ON' if status_str[20] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel3N.setText('ON' if status_str[19] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel4N.setText('ON' if status_str[18] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel5N.setText('ON' if status_str[17] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel6N.setText('ON' if status_str[16] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel7N.setText('ON' if status_str[15] == '1' else 'OFF')
        self.leadoff_monitor_form.statusChannel8N.setText('ON' if status_str[14] == '1' else 'OFF')
