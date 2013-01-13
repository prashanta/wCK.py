import sys
import serial
import struct
import time
import array

class servo:
	port = "/dev/tty.SLAB_USBtoUART"
	baud = 115200
	id = 0
	ser = 0
	def __init__(self, port, baud, id):
	    self.data = []
	    if port:
	    	self.port = port
	    if baud:
	    	self.baud = baud
	    if id:
	    	self.id = id
	    self.ser = serial.Serial(self.port,115200,timeout=2)		
	
	# Read current servo position
	def readPos(self):
		header =  255  	
		data1 = 0xa0 | self.id
		data2 = 0x00
		chksum = (data1 ^ data2) & 0x7F
		#chksum = 0x03
		print hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)
		self.ser.write(struct.pack("<B",header))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",chksum))
		data = self.ser.readline()
		data = data.split()
		print data

	# Move servo to specified target position (1-254) 	
	def pos(self, torque, target):
		header =  255  	
		data = (torque<<5) | self.id
		chksum = (data ^ target) & 0x7F
		print hex(header) + " " + hex(data) + " " + hex(target) + " " + hex(chksum)
		self.ser.write(struct.pack("<B",header))
		self.ser.write(struct.pack("<B",data))
		self.ser.write(struct.pack("<B",target))
		self.ser.write(struct.pack("<B",chksum))
		
	# Rotate wheel in cloclwise direction at given speed  	
	def cw(self, speed):
		ser = serial.Serial(self.port,115200,timeout=1)
		header =  255  	
		data1 = (6<<5) | self.id
		data2= (4<<4)| speed
		chksum = (data1 ^ data2) & 0x7F
		print hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)
		self.ser.write(struct.pack("<B",header))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",chksum))
		
	def ccw(self, speed):
		header =  255  	
		data1 = (6<<5) | self.id
		data2= (3<<4)| speed
		chksum = (data1 ^ data2) & 0x7F
		print hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)
		self.ser.write(struct.pack("<B",header))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",chksum))

	# Close the serial port
	def closeSerial(self):
		self.ser.close();