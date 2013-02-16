#!/usr/bin/python

# ** wck.py **
# - Move to Pos, Read Pos, Rotate CW, Rotate CCW
# - Set ID, Set Baudrate, Set Gain
#
# Copyright (C) 2013 Prashanta Man Shrestha

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import serial
import struct
import time
import array

class servo:
        port = "/dev/tty.SLAB_USBtoUART"
        baud = 115200
        HEADER = 255
        sid = 0
        ser = 0
        
	def __init__(self, port, baud, id):
	    self.data = []
	    if port:
	    	self.port = port
	    if baud:
	    	self.baud = baud
	    if id:
	    	self.sid = id
	    self.ser = serial.Serial(self.port,115200,timeout=3)		
			
	# SEND SET COMMAND TO SERVO		
	def sendSetCmd(self, data1, data2, data3, data4):	
		chksum = (data1^data2^data3^data4)&0x7f
		self.ser.flushInput();
		print "SENDING:" + hex(self.HEADER) + " " + hex(data1) + " " + hex(data2) + " " + hex(data3) + " " + hex(data4) + " " + hex(chksum)		
		self.ser.write(struct.pack("<B",self.HEADER))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",data3))
		self.ser.write(struct.pack("<B",data4))
		self.ser.write(struct.pack("<B",chksum))		
	
	# SEND COMMAND TO SERVO
	def sendCmd(self, data1, data2):
		chksum = (data1 ^ data2) & 0x7F
		self.ser.flushInput();
		print "SENDING:" + hex(self.HEADER) + " " + hex(data1) + " " + hex(data2) + " " + hex(chksum)		
		self.ser.write(struct.pack("<B",self.HEADER))
		self.ser.write(struct.pack("<B",data1))
		self.ser.write(struct.pack("<B",data2))
		self.ser.write(struct.pack("<B",chksum))
		
	# READ FEEDBACK
	def readStatus(self):
		time.sleep(0.5)
		print self.ser.inWaiting();
		data = self.ser.read(1)
		print data.encode('hex')
		data = self.ser.read(1)
		print data.encode('hex')
        		
	# READ CURRENT SERVO POSITION
	def readPos(self):
		data1 = 0xa0 | self.sid
		data2 = 0x00
		self.sendCmd(data1, data2)		
		self.readStatus()
		
	# MOVE SERVO TO SPECIFIED TARGET POSITION (1-254)
	def pos(self, torque, target):
		data = (torque<<5) | self.sid
		self.sendCmd(data, target)
		self.readStatus()
		
	# ROTATE WHEEL IN CLOCKWISE DIRECTION AT GIVEN SPEED (1-15, 0: stop)
	def cw(self, speed):
		data1 = (6<<5) | self.sid
		data2= (4<<4)| speed
		self.sendCmd(data1, data2)
		
	# ROTATE WHEEL IN COUNTER-CLOCKWISE DIRECTION AT GIVEN SPEED (1-15, 0: stop)	
	def ccw(self, speed):  	
		data1 = (6<<5) | self.sid
		data2= (3<<4)| speed
		self.sendCmd(data1, data2,)

	# CLOSE SERIAL PORT
	def closeSerial(self):
		self.ser.close();