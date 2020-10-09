# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import socket
from glob import iglob
import os

from .profile_select_form import Ui_profileSelectForm
from .profile_setup import CreateProfileWidget
from .monitor import MonitorWindow
from .data_capture import DataCaptureSetup
from .data_capture import DataCapture
from .monitor_settings import MonitorSettingsWidget
from .leadoff_monitor import LeadOffStatusMonitorWidget
from .start_connection import StartConnectionWidget


class MainWindow(qtw.QMainWindow):

    default_profile = {
        'CONFIG1': '10010110',
        'CONFIG2': '11000000',
        'CONFIG3': '01100000',
        'LOFF': '00000000',
        'CH1SET': '01100001',
        'CH2SET': '01100001',
        'CH3SET': '01100001',
        'CH4SET': '01100001',
        'CH5SET': '01100001',
        'CH6SET': '01100001',
        'CH7SET': '01100001',
        'CH8SET': '01100001',
        'BIAS_SENSP': '00000000',
        'BIAS_SENSN': '00000000',
        'LOFF_SENSP': '00000000',
        'LOFF_SENSN': '00000000',
        'LOFF_FLIP': '00000000',
        'MISC1': '00000000',
        'MISC2': '00000000',
        'GPIO': '00001111',
        'CONFIG4': '00000000'
    }

    def __init__(self):
        """MainWindow Constructor"""
        super().__init__()

        self.profiles_path = os.getcwd() + '/profiles/'

        socket.setdefaulttimeout(5)
        self.s = None
        self.conn, self.addr = None, None

        # Create windows and widgets
        # Profile select widget
        select_profile_wdg = qtw.QWidget()
        self.profile_select_form = Ui_profileSelectForm()
        self.profile_select_form.setupUi(select_profile_wdg)
        self.profile_select_form.profileSubmitBtn.setEnabled(True)
        for prof in list(map(os.path.basename, iglob(self.profiles_path+"*.adsregprofile"))):
            self.profile_select_form.profileComboBox.addItem(prof.split('.')[0], prof)
        self.profile_select_form.profileSubmitBtn.clicked.connect(self.set_registers)
        self.profile_select_form.configureProfileBtn.clicked.connect(self.configure_profile)
        self.profile_select_form.profileComboBox.setCurrentIndex(0)
        self.setCentralWidget(select_profile_wdg)

        # Start connection widget
        self.start_connection_wdg = StartConnectionWidget()
        self.start_connection_wdg.start_connection_form.ipLineEdit.setText('192.168.1.64')
        self.start_connection_wdg.start_connection_form.portLineEdit.setText('6005')
        self.start_connection_wdg.start_connection_form.connectBtn.clicked.connect(self.initiate_tcp_connection)

        # Create register profile widget
        self.register_profile = CreateProfileWidget()
        self.register_profile.submitted.connect(self.update_profile_combobox)

        # Monitor windows
        self.monitor = MonitorWindow(self.conn)
        self.monitor_settings = MonitorSettingsWidget()
        self.monitor_settings.submitted.connect(self.monitor.set_settings)
        self.leadoff_status_monitor = LeadOffStatusMonitorWidget()
        self.monitor.setStatus.connect(self.leadoff_status_monitor.update_status)

        # Data capture windows
        self.data_capture_setup = DataCaptureSetup()
        self.data_capture = DataCapture()
        self.data_capture.data_capture_form.recordButton.clicked.connect(self.record_start)

        # Creating StatusBar
        self.connection_message = qtw.QLabel()
        self.statusBar().addPermanentWidget(self.connection_message)
        self.connection_message.setText("Device Not Connect, Start Connecting the device")

        # Creating MenuBar
        menubar = self.menuBar()
        options_menu = menubar.addMenu('Options')
        monitor_menu = menubar.addMenu('Monitor')
        record_menu = menubar.addMenu('Record')

        self.connect_action = options_menu.addAction('Connect...', self.start_connection_wdg.show)
        options_menu.addAction('Create Register Profile', self.register_profile.show)
        options_menu.addAction('Close', self.close)

        monitor_menu.addAction('Monitor', self.monitor_start)
        monitor_menu.addAction('Monitor Settings', self.monitor_settings.show)

        monitor_menu.addAction('Lead-Off Monitor', self.leadoff_status_monitor.show)

        record_menu.addAction('Create Data Capture Profile', self.data_capture_setup.show)
        record_menu.addAction('Record Data', self.initialize_record)

        # Setup monitor
        self.monitor_timer = qtc.QTimer()
        self.monitor_timer.timeout.connect(self.monitor.update)
        self.monitor.stopUpdate.connect(self.monitor_timer.stop)
        self.monitor.stopRecord.connect(self.data_capture.finalize_record)

        # End main UI code
        self.show()

    def initiate_tcp_connection(self):
        # Starting tcp connection, getting ip and port from start_connection_widget
        tcp_ip = self.start_connection_wdg.start_connection_form.ipLineEdit.text()
        tcp_port = int(self.start_connection_wdg.start_connection_form.portLineEdit.text())
        self.start_connection_wdg.start_connection_form.statusLabel.setText('Initiating TCP Connection...')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((tcp_ip, tcp_port))
        self.s.listen(1)

        try:
            self.conn, self.addr = self.s.accept()
            self.connection_message.setText("Device Connected and ready to go")
            self.connect_action.setEnabled(False)
            self.start_connection_wdg.start_connection_form.statusLabel\
                .setText('Connection Successful Setting Default Registers')
            self.set_registers()
            self.start_connection_wdg.close()
        except socket.timeout:
            self.start_connection_wdg.start_connection_form.statusLabel\
                .setText('Connection Failed')
            self.s.close()

    def update_profile_combobox(self):
        self.profile_select_form.profileComboBox.clear()
        self.profile_select_form.profileComboBox.addItem("Default Profile")
        for prof in list(map(os.path.basename, iglob(self.profiles_path+"*.adsregprofile"))):
            self.profile_select_form.profileComboBox.addItem(prof.split('.')[0], prof)
        self.profile_select_form.profileComboBox.setCurrentIndex(0)

    def set_registers(self):
        target_dict = {}
        if self.profile_select_form.profileComboBox.currentIndex() == 0:
            target_dict = self.default_profile
        else:
            target_dict = self.create_dict_from_reg_file(self.profiles_path + self.profile_select_form.profileComboBox.currentData())

        # Waiting for device to get ready and receiving ready command
        self.conn.send(bytes("setreg", "utf-8"))
        rdycmd = self.conn.recv(3).decode("utf-8")
        if rdycmd == "rdy":
            while 1:
                regName = self.conn.recv(10).decode("utf-8")
                if regName == "done":
                    break
                self.conn.send(bytes(target_dict.get(regName), "utf-8"))

    def create_dict_from_reg_file(self, path):
        res = {}
        registers_string = ""
        with open(path) as fh:
            registers_string = fh.readline().strip()

        res = dict(map(lambda x: x.split(':'), registers_string.split(',')))
        return res

    def configure_profile(self):
        # Populating create register profile form with the selected profile values
        if self.profile_select_form.profileComboBox.currentIndex() == 0:
            return

        target_dict = self.create_dict_from_reg_file(self.profiles_path + self.profile_select_form.profileComboBox.currentData())
        self.register_profile.registration_form.config1_field.setText(target_dict.get('CONFIG1'))
        self.register_profile.registration_form.config2_field.setText(target_dict.get('CONFIG2'))
        self.register_profile.registration_form.config3_field.setText(target_dict.get('CONFIG3'))
        self.register_profile.registration_form.loff_field.setText(target_dict.get('LOFF'))
        self.register_profile.registration_form.ch1_field.setText(target_dict.get('CH1SET'))
        self.register_profile.registration_form.ch2_field.setText(target_dict.get('CH2SET'))
        self.register_profile.registration_form.ch3_field.setText(target_dict.get('CH3SET'))
        self.register_profile.registration_form.ch4_field.setText(target_dict.get('CH4SET'))
        self.register_profile.registration_form.ch5_field.setText(target_dict.get('CH5SET'))
        self.register_profile.registration_form.ch6_field.setText(target_dict.get('CH6SET'))
        self.register_profile.registration_form.ch7_field.setText(target_dict.get('CH7SET'))
        self.register_profile.registration_form.ch8_field.setText(target_dict.get('CH8SET'))
        self.register_profile.registration_form.biassensp_field.setText(target_dict.get('BIAS_SENSP'))
        self.register_profile.registration_form.biassensn_field.setText(target_dict.get('BIAS_SENSN'))
        self.register_profile.registration_form.loffsensn_field.setText(target_dict.get('LOFF_SENSN'))
        self.register_profile.registration_form.loffsensp_field.setText(target_dict.get('LOFF_SENSP'))
        self.register_profile.registration_form.loffflip_field.setText(target_dict.get('LOFF_FLIP'))
        self.register_profile.registration_form.misc1_field.setText(target_dict.get('MISC1'))
        self.register_profile.registration_form.misc2_field.setText(target_dict.get('MISC2'))
        self.register_profile.registration_form.gpio_field.setText(target_dict.get('GPIO'))
        self.register_profile.registration_form.config4_field.setText(target_dict.get('CONFIG4'))
        self.register_profile.registration_form.name_field.setText(self.profile_select_form.profileComboBox.currentText())

        self.register_profile.show()

    def record_start(self):
        if self.conn:
            self.monitor.set_connection(self.conn)
            self.conn.send(bytes('datalog', "utf-8"))
            count_high = 0
            while count_high < 20:
                if self.conn.recv(10).decode("utf-8") == "drdyhigh":
                    count_high += 1
                    continue
                else:
                    self.data_capture.data_capture_form.statusLabel.setText('Recording...')
                    self.monitor.show()
                    self.monitor_timer.start()
                    lim = self.data_capture.data_limit
                    channels = self.data_capture.selected_channels
                    loc = ''
                    path = self.data_capture.save_location + '\\' + self.data_capture.data_capture_form.categoryComboBox.currentText()
                    if not os.path.exists(path):
                        os.makedirs(path)
                    if self.data_capture.save_type == 'xlsx':
                        loc = path + '\\' + str(self.data_capture.data_count) + '.xlsx'

                    elif self.data_capture.save_type == 'csv':
                        loc = path + '\\' + str(self.data_capture.data_count) + '.csv'

                    self.monitor.start(record=True, limit=lim, loc=loc, stype=self.data_capture.save_type, channels=channels)
                    return
            self.conn.send(bytes('stopdata', "utf-8"))

    def monitor_start(self):
        if self.conn:
            self.monitor.set_connection(self.conn)
            self.conn.send(bytes('datalog', "utf-8"))
            count_high = 0
            while count_high < 20:
                if self.conn.recv(10).decode("utf-8") == "drdyhigh":
                    count_high += 1
                    continue
                else:
                    self.monitor.show()
                    self.monitor_timer.start(0)
                    self.monitor.start()
                    return
            self.conn.send(bytes('stopdata', "utf-8"))

    def initialize_record(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(
            self,
            "Select a Record Profile to open...",
            qtc.QDir.homePath(),
            'ADS Record Profile (*.adsrecprofile)',
            'ADS Record Profile (*.adsrecprofile)',
            qtw.QFileDialog.DontResolveSymlinks
        )

        if filename:
            try:
                self.data_capture.set_params(filename)
                self.data_capture.show()
            except Exception as e:
                qtw.QMessageBox.critical(f"Could not load Profile: {e}")

    def closeEvent(self, event):
        if self.conn:
            self.monitor.reset_plots_onclose = False
            if not self.monitor_timer.isActive():
                self.monitor.set_connection(None)
            self.leadoff_status_monitor.close()
            self.monitor_settings.close()
            self.monitor.close()
            self.data_capture.close()
            self.register_profile.close()
            self.conn.send(bytes('close', "utf-8"))
            self.s.close()
