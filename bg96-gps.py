import serial
import time

#################################
#settings
comm_port = 'COM5'
baudrate = 115200
sleep_period = 2
#################################

ser = serial.Serial(comm_port, baudrate, timeout=1)  # open serial port
print(ser.name)         # check which port was really used


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
    

