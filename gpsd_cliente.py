# Client gpsd_nmea
# Python 3.6.6
# Windows 10
# Noviembre 2018
# Correr pip install pynmea2

import socket       
import sys        
import time
import pynmea2
import os

 
remote_ip   = '192.168.43.47';  #Cambiar a ip del servidor propio
port        = 9001;             #Cambiar al puerto del servidor

line_data   = ''
s = ''

def connect_server_gpsd(host,port):
    try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
                print  ('Falla al crear Socket')
                return -1
                sys.exit()
    print ('Socket Creado')

    s.connect((host , port))
    print ('Socket Conectado a ip: ' + remote_ip + '  puerto: ' + str(port))
    return s
    pass

s = connect_server_gpsd(remote_ip,port)

try:
    while 1:
        data = s.recv(1)                        # Leer un dato por recorrido
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

            line_data = ''                      # Limpiamos linea de sentencia procesada
except(KeyboardInterrupt, SystemExit):
    s.close()
    
print('\nTerminado por Usuario.\n')

time.sleep(1)
