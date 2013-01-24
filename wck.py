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
	    self.ser = serial.Serial(self.port,115200,timeout=3)		
	
	# SEND COMMAND TO SERVO
	def sendCmd(self, header, data1, data2):
		chksum = (data1 ^ data2) & 0x7F
		self.ser.flushInput();
		print "SENDING:" + hex(header) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)		
		self.ser.write(struct.pack("<B",header))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",chksum))
		
	# READ CURRENT SERVO POSITION
	def readPos(self):
		header =  255  	
		data1 = 0xa0 | self.id
		data2 = 0x00
		self.sendCmd(header, data1, data2)		
		time.sleep(0.5) 
		print self.ser.inWaiting();
		data = self.ser.read(1)
		data = self.ser.read(1)
		print data.encode('hex')

	# MOVE SERVO TO SPECIFIED TARGET POSITION (1-254)
	def pos(self, torque, target):
		header =  255  	
		data = (torque<<5) | self.id
		self.sendCmd(header, data, target)
		
	# ROTATE WHEEL IN CLOCKWISE DIRECTION AT GIVEN SPEED
	def cw(self, speed):
		ser = serial.Serial(self.port,115200,timeout=1)
		header =  255  	
		data1 = (6<<5) | self.id
		data2= (4<<4)| speed
		self.sendCmd(header, data1, data2)
		
	# ROTATE WHEEL IN COUNTER-CLOCKWISE DIRECTION AT GIVEN SPEED	
	def ccw(self, speed):
		header =  255  	
		data1 = (6<<5) | self.id
		data2= (3<<4)| speed
		self.sendCmd(data1, data2,)

	# CLOSE SERIAL PORT
	def closeSerial(self):
		self.ser.close();