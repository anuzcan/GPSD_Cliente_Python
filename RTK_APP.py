import sys,time
import socket       #for sockets
import time
import pynmea2
import os

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import pyqtSlot
from MainWindow import Ui_main_Dialog
from threading import Thread

remote_ip   = '192.168.43.47';
port        = 9001;
_buffer     = ''
line_data   = ''
tcpClientA	= None


class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.dlg = Ui_main_Dialog()
		self.dlg.setupUi(self)
		self.initUI() #Funcion donde se inician todas las confuguraciones previas
		self.show()

	def initUI(self):
		self.dlg.ip_QlineEdit.setText(remote_ip)
		self.dlg.port_QlineEdit.setText(str(port))
		self.dlg.connect_server.clicked.connect(self.on_click)
		self.dlg.stop_server.clicked.connect(self.off_click)

	@pyqtSlot()
	def on_click(self):
		
		remote_ip = self.dlg.ip_QlineEdit.text()
		port = self.dlg.port_QlineEdit.text()
		
		clientThread=ClientThread(self)
		clientThread.start()
		
		self.dlg.statusLabel.setText('Socket Conectado a ip: ' + remote_ip + '  puerto: ' + port)

	def off_click(self):
		pass


class ClientThread(Thread):
	def __init__(self,parent):
		Thread.__init__(self)
		self.parent = parent

	def run(self):
		global tcpClientA
		global remote_ip
		global port
		global line_data

		tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		tcpClientA.connect((remote_ip, port))
        
		while True:
			data = tcpClientA.recv(1)                        # Leer un dato por recorrido
			_buffer = str(data)                     # Almacena dato en variable auxiliar
			if _buffer[2] != '\\':                  # Si dato direfente a sentencia de separacion lo agrega a la cadena a comando recibido
				line_data += _buffer[2]         
			else:                                   # Si dato de separacion recibo
				if line_data.find('$GNGGA') != -1:  # Busca sentencia coordenadas nmea
                	#print(line_data)
					msg = pynmea2.parse(line_data)  # Extancion de informacion de sentencia nmea
					os.system('cls')
					total = msg.altitude + float(msg.geo_sep)
            
					print('GPSD cliente')
					print ('Socket Conectado a ip: ' + remote_ip + '  puerto: ' + str(port) + '\n')
					print('Lat:       ' + str(msg.latitude))
					print('Lon:       ' + str(msg.longitude))
					print('Ele:       ' + str(total))
					print('Sat n:     ' + str(msg.num_sats))
					print('Gps Qual:   ' + str(msg.gps_qual))
					print('')

					self.dlg.eleve_QlineEdit.setText(str(total))

				line_data = ''

		tcpClientA.close() 

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = AppWindow()
	window.show()
	sys.exit(app.exec_())
