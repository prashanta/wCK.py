import sys
import serial
import struct

def test():
	print "Hello"

# Move servo to specified target position (1-254) 
def pos(torque, target):
  	ser = serial.Serial("/dev/tty.usbmodem411",115200,timeout=1)
  	header =  255  	
  	data = (torque<<5) | 0
  	chksum = (data ^ target) & 0x7F
  	print hex(header) + " " + hex(data) + " " + hex(target) + " " + hex(chksum)
  	ser.write(struct.pack("<B",header))
  	ser.write(struct.pack("<B",data))
  	ser.write(struct.pack("<B",target))
  	ser.write(struct.pack("<B",chksum))
  	ser.close()
  	
# Rotate wheel in cloclwise direction at given speed  	
def cw(speed):
  	ser = serial.Serial("/dev/tty.usbmodem411",115200,timeout=1)
  	header =  255  	
  	data1 = (6<<5) | 0
  	data2= (4<<4)| speed
  	chksum = (data1 ^ data2) & 0x7F
  	print hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)
  	ser.write(struct.pack("<B",header))
  	ser.write(struct.pack("<B",data1))
  	ser.write(struct.pack("<B",data2))
  	ser.write(struct.pack("<B",chksum))
  	ser.close()  	

# Rotate wheel in anti-cloclwise direction at given speed  	
def ccw(speed):
  	ser = serial.Serial("/dev/tty.usbmodem411",115200,timeout=1)
  	header =  255  	
  	data1 = (6<<5) | 0
  	data2= (3<<4)| speed
  	chksum = (data1 ^ data2) & 0x7F
  	print hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)
  	ser.write(struct.pack("<B",header))
  	ser.write(struct.pack("<B",data1))
  	ser.write(struct.pack("<B",data2))
  	ser.write(struct.pack("<B",chksum))
  	ser.close()  	 