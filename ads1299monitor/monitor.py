# -----------------------------------------------------------
# ads1299 GUI monitoring software v-1.0
#
#
# (C) 2020 Aryan Akbarpour, Sheffield, UK
# Released under MIT License
# Email aryan.akr@yahoo.com
# -----------------------------------------------------------

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import pyqtgraph as qtgr
import socket
import csv
import xlsxwriter


class MonitorWindow(qtgr.GraphicsWindow):
    stopUpdate = qtc.pyqtSignal()
    stopRecord = qtc.pyqtSignal()
    setStatus = qtc.pyqtSignal(str)

    def __init__(self, conn):
        super().__init__()

        self.reset_plots_onclose = True

        self.conn = conn
        self.BUFFER_SIZE = 99

        qtgr.setConfigOptions(antialias=False)
        self.traces = dict()

        proxy = qtw.QGraphicsProxyWidget()
        self.resize(1200, 800)

        self.x = list(range(0, 1000))
        self.ch1data = [0] * 1000
        self.ch2data = [0] * 1000
        self.ch3data = [0] * 1000
        self.ch4data = [0] * 1000
        self.ch5data = [0] * 1000
        self.ch6data = [0] * 1000
        self.ch7data = [0] * 1000
        self.ch8data = [0] * 1000

        self.ch1recdata = []
        self.ch2recdata = []
        self.ch3recdata = []
        self.ch4recdata = []
        self.ch5recdata = []
        self.ch6recdata = []
        self.ch7recdata = []
        self.ch8recdata = []

        # Record Settings
        self.save_location = ''
        self.limit = 0
        self.data_count = 0
        self.save_type = ''
        self.record_channel1 = False
        self.record_channel2 = False
        self.record_channel3 = False
        self.record_channel4 = False
        self.record_channel5 = False
        self.record_channel6 = False
        self.record_channel7 = False
        self.record_channel8 = False
        self.record = False

        # Plot Settings
        self.update_channel1 = True
        self.update_channel2 = True
        self.update_channel3 = True
        self.update_channel4 = True
        self.update_channel5 = True
        self.update_channel6 = True
        self.update_channel7 = True
        self.update_channel8 = True
        self.show_leadoff_status = False

        self.graph_ch1 = self.addPlot(title='Channel1', row=1, col=1)
        self.graph_ch2 = self.addPlot(title='Channel2', row=2, col=1)
        self.graph_ch3 = self.addPlot(title='Channel3', row=3, col=1)
        self.graph_ch4 = self.addPlot(title='Channel4', row=4, col=1)
        self.graph_ch5 = self.addPlot(title='Channel5', row=1, col=2)
        self.graph_ch6 = self.addPlot(title='Channel6', row=2, col=2)
        self.graph_ch7 = self.addPlot(title='Channel7', row=3, col=2)
        self.graph_ch8 = self.addPlot(title='Channel8', row=4, col=2)

    def start(self, record=False, limit=0, loc='', stype='', channels=[]):
        if record:
            self.record = record
            self.limit = int(limit)
            self.save_location = loc
            self.save_type = stype
            self.record_channel1 = False if channels[0] == '0' else True
            self.record_channel2 = False if channels[1] == '0' else True
            self.record_channel3 = False if channels[2] == '0' else True
            self.record_channel4 = False if channels[3] == '0' else True
            self.record_channel5 = False if channels[4] == '0' else True
            self.record_channel6 = False if channels[5] == '0' else True
            self.record_channel7 = False if channels[6] == '0' else True
            self.record_channel8 = False if channels[7] == '0' else True

        if (sys.flags.interactive != 1) or not hasattr(qtc, 'PYQT_VERSION'):
            qtg.QApplication.instance().exec_()

    def set_settings(self, settings):
        self.update_channel1 = False if settings[0] == 0 else True
        self.update_channel2 = False if settings[1] == 0 else True
        self.update_channel3 = False if settings[2] == 0 else True
        self.update_channel4 = False if settings[3] == 0 else True
        self.update_channel5 = False if settings[4] == 0 else True
        self.update_channel6 = False if settings[5] == 0 else True
        self.update_channel7 = False if settings[6] == 0 else True
        self.update_channel8 = False if settings[7] == 0 else True
        self.show_leadoff_status = False if settings[8] == 0 else True

    def set_plotdata(self, name, data_x, data_y):
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            if name == 'Channel1':
                self.traces[name] = self.graph_ch1.plot(pen='c', width=3)
            if name == 'Channel2':
                self.traces[name] = self.graph_ch2.plot(pen='m', width=3)
            if name == 'Channel3':
                self.traces[name] = self.graph_ch3.plot(pen='m', width=3)
            if name == 'Channel4':
                self.traces[name] = self.graph_ch4.plot(pen='m', width=3)
            if name == 'Channel5':
                self.traces[name] = self.graph_ch5.plot(pen='m', width=3)
            if name == 'Channel6':
                self.traces[name] = self.graph_ch6.plot(pen='m', width=3)
            if name == 'Channel7':
                self.traces[name] = self.graph_ch7.plot(pen='m', width=3)
            if name == 'Channel8':
                self.traces[name] = self.graph_ch8.plot(pen='m', width=3)

    def update(self):
        data = self.conn.recv(self.BUFFER_SIZE)
        if data:
            # TODO: Massage validation check
            msg = data.decode("utf-8")
            if msg[0] == 't':
                elems = msg.split(',')
                # Update LeadOff status Monitor
                if self.show_leadoff_status:
                    self.setStatus.emit(elems[1])

                for q in range(len(elems) - 1):
                    try:
                        elems[q + 1] = float(int(elems[q + 1])) * (5 / 24) / 2 ** 24
                    except ValueError as ve:
                        return

                self.x = self.x[1:]
                self.x.append(self.x[-1] + 1)

                if self.update_channel1:
                    self.ch1data = self.ch1data[1:]
                    self.ch1data.append(elems[2])
                if self.record and self.record_channel1:
                    self.ch1recdata.append(elems[2])

                if self.update_channel2:
                    self.ch2data = self.ch2data[1:]
                    self.ch2data.append(elems[3])
                if self.record and self.record_channel2:
                    self.ch2recdata.append(elems[3])

                if self.update_channel3:
                    self.ch3data = self.ch3data[1:]
                    self.ch3data.append(elems[4])
                if self.record and self.record_channel3:
                    self.ch3recdata.append(elems[4])

                if self.update_channel4:
                    self.ch4data = self.ch4data[1:]
                    self.ch4data.append(elems[5])
                if self.record and self.record_channel4:
                    self.ch4recdata.append(elems[5])

                if self.update_channel5:
                    self.ch5data = self.ch5data[1:]
                    self.ch5data.append(elems[6])
                if self.record and self.record_channel5:
                    self.ch5recdata.append(elems[6])

                if self.update_channel6:
                    self.ch6data = self.ch6data[1:]
                    self.ch6data.append(elems[7])
                if self.record and self.record_channel6:
                    self.ch6recdata.append(elems[7])

                if self.update_channel7:
                    self.ch7data = self.ch7data[1:]
                    self.ch7data.append(elems[8])
                if self.record and self.record_channel7:
                    self.ch7recdata.append(elems[8])

                if self.update_channel8:
                    self.ch8data = self.ch8data[1:]
                    self.ch8data.append(elems[9])
                if self.record and self.record_channel8:
                    self.ch8recdata.append(elems[9])

                # Update Monitor Plots
                if self.update_channel1 and not(self.record and not self.record_channel1):
                    self.set_plotdata(name="Channel1", data_x=self.x, data_y=self.ch1data)
                if self.update_channel2 and not(self.record and not self.record_channel2):
                    self.set_plotdata(name="Channel2", data_x=self.x, data_y=self.ch2data)
                if self.update_channel3 and not(self.record and not self.record_channel3):
                    self.set_plotdata(name="Channel3", data_x=self.x, data_y=self.ch3data)
                if self.update_channel4 and not(self.record and not self.record_channel4):
                    self.set_plotdata(name="Channel4", data_x=self.x, data_y=self.ch4data)
                if self.update_channel5 and not(self.record and not self.record_channel5):
                    self.set_plotdata(name="Channel5", data_x=self.x, data_y=self.ch5data)
                if self.update_channel6 and not(self.record and not self.record_channel6):
                    self.set_plotdata(name="Channel6", data_x=self.x, data_y=self.ch6data)
                if self.update_channel7 and not(self.record and not self.record_channel7):
                    self.set_plotdata(name="Channel7", data_x=self.x, data_y=self.ch7data)
                if self.update_channel8 and not(self.record and not self.record_channel8):
                    self.set_plotdata(name="Channel8", data_x=self.x, data_y=self.ch8data)

                self.data_count += 1

                if self.record and self.data_count >= self.limit:
                    self.end_record()

    def end_record(self):
        # end recording
        if self.conn:
            self.conn.send(bytes('stopdata', "utf-8"))
            self.stopUpdate.emit()
            self.stopRecord.emit()
        # save data in excel
        if self.save_type == 'xlsx':
            workbook = xlsxwriter.Workbook(self.save_location)
            worksheet = workbook.add_worksheet()

            row = 0
            column = 0
            for d in self.ch1recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch2recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch3recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch4recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch5recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch6recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch7recdata:
                worksheet.write(row, column, d)
                row += 1
            column += 1
            row = 0
            for d in self.ch8recdata:
                worksheet.write(row, column, d)
                row += 1
            workbook.close()

        elif self.save_type == 'csv':
            with open(self.save_location, 'w', newline='') as file:
                writer = csv.writer(file)
                header = []
                header.append("Channel1") if self.record_channel1 else None
                header.append("Channel2") if self.record_channel2 else None
                header.append("Channel3") if self.record_channel3 else None
                header.append("Channel4") if self.record_channel4 else None
                header.append("Channel5") if self.record_channel5 else None
                header.append("Channel6") if self.record_channel6 else None
                header.append("Channel7") if self.record_channel7 else None
                header.append("Channel8") if self.record_channel8 else None
                writer.writerow(header)

                for n in range(self.limit):
                    row = []
                    row.append(self.ch1recdata[n]) if self.record_channel1 else None
                    row.append(self.ch2recdata[n]) if self.record_channel2 else None
                    row.append(self.ch3recdata[n]) if self.record_channel3 else None
                    row.append(self.ch4recdata[n]) if self.record_channel4 else None
                    row.append(self.ch5recdata[n]) if self.record_channel5 else None
                    row.append(self.ch6recdata[n]) if self.record_channel6 else None
                    row.append(self.ch7recdata[n]) if self.record_channel7 else None
                    row.append(self.ch8recdata[n]) if self.record_channel8 else None
                    writer.writerow(row)
        # reset and close
        self.reset_monitor()

    def set_connection(self, connection):
        self.conn = connection

    def reset_monitor(self):
        # Clearing TCP pipeline
        while 1:
            try:
                data = self.conn.recv(1024)
            except socket.timeout:
                break
        self.x = list(range(0, 1000))
        self.ch1data = [0] * 1000
        self.ch2data = [0] * 1000
        self.ch3data = [0] * 1000
        self.ch4data = [0] * 1000
        self.ch5data = [0] * 1000
        self.ch6data = [0] * 1000
        self.ch7data = [0] * 1000
        self.ch8data = [0] * 1000

        self.ch1recdata = []
        self.ch2recdata = []
        self.ch3recdata = []
        self.ch4recdata = []
        self.ch5recdata = []
        self.ch6recdata = []
        self.ch7recdata = []
        self.ch8recdata = []

        if self.reset_plots_onclose:
            self.set_plotdata(name="Channel1", data_x=[], data_y=[])
            self.set_plotdata(name="Channel2", data_x=[], data_y=[])
            self.set_plotdata(name="Channel3", data_x=[], data_y=[])
            self.set_plotdata(name="Channel4", data_x=[], data_y=[])
            self.set_plotdata(name="Channel5", data_x=[], data_y=[])
            self.set_plotdata(name="Channel6", data_x=[], data_y=[])
            self.set_plotdata(name="Channel7", data_x=[], data_y=[])
            self.set_plotdata(name="Channel8", data_x=[], data_y=[])

        self.save_location = ''
        self.limit = 0
        self.data_count = 0
        self.save_type = ''

        self.record = False

    def closeEvent(self, event):
        if self.conn:
            self.conn.send(bytes('stopdata', "utf-8"))
            self.reset_monitor()
            self.stopUpdate.emit()
