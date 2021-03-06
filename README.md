#wCK.py


A python library to control wCK servo from [RoboBuilder](http://www.robobuilder.net/eng/index.asp). This is an attempt to replicate functions of wCK Programmer, which is available only for Microsoft Windows (darn it!).

You will need [pySerial](http://pyserial.sourceforge.net) library for this.


####Usage

*Start python interpreter*

`$ python`

*Import servo*

`>>> from wck import servo`

*Create instance with serial port, baud rate and servo id*

`>>> a = servo("/dev/tty.SLAB_USBtoUART",115200,0)`

*Scan to determine Servo ID and Baudrate*

`>>> a.scan()`

*Send servo position command*

`>>> a.pos(4,102)`

*Read sevo position*

`>>> a.readPos()`

*Continuous run servo counter clockwise direction*

`>>> a.ccw(12)`

*Continuous run servo clockwise direction*

`>>> a.cw(12)`

*Stop servo*

`>>> a.cw(0)`

*Set new ID to servo*

`>>> a.setID(12)`

*Close serial port*

`>>> a.close()`


####Resources

[wCK User's Manual](http://robosavvy.com/RoboSavvyPages/Robobuilder/robobuilder-creator-users-manual.pdf)

[wCK Programmer User's Manual](http://www.tribotix.com/Downloads/RoboBuilder/wCK/User%20Manual%20_wCK%20programmer%20tool_%20v1.03%20EN.pdf)

[Understanding wCK module and 
C programming with RoboBuilder](http://ro-botica.com/img/Robobuilder/RoboBuilder%20C_tutorial%20.pdf)

---

The MIT License (MIT)

Copyright (C) 2013 Prashanta Shrestha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
