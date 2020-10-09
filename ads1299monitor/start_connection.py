# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

from PyQt5 import QtWidgets as qtw

from .start_connection_form import Ui_StartConnectionForm


class StartConnectionWidget(qtw.QWidget):

    def __init__(self):
        super().__init__()
        self.start_connection_form = Ui_StartConnectionForm()
        self.start_connection_form.setupUi(self)
