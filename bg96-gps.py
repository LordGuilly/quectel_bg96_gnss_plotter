import serial
import time

#################################
#settings
comm_port = 'COM5'
baudrate = 115200
sleep_period = 2
#################################

ser = serial.Serial(comm_port, baudrate, timeout=1)  # open serial port


ser.write("AT+QGPS=1\r")     # write a string
for response in ser.readlines():
	if response.startswith("ERROR"):
		print response.rstrip()
		exit()



try:
	while True:
		ser.write("AT+QGPSLOC?\r")     # write a string
		for response in ser.readlines():
			if response.startswith("+QGPSLOC") or response.startswith("+CME"):
				print response.rstrip()

		time.sleep(sleep_period)

except KeyboardInterrupt:
    # quit
    ser.close()         
    

