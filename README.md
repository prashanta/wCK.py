#wCK.py
---

A python library to control wCK servo from [RoboBuilder](http://www.robobuilder.net/eng/index.asp). This is an attempt to replicate functions of wCK Programmer, which is available only for Microsoft Windows (darn it!).

You will need [pySerial](http://pyserial.sourceforge.net) library for this.

This is a work in progress!

---
####Usage

*Start python interpreter*

`$ python`

*Import servo*

`>>> from wck import servo`

*Create instance with serial port, baud rate and servo id*

`>>> a = servo("/dev/tty.SLAB_USBtoUART",115200,0)`

*Send servo position command*

`>>> a.pos(4.102)`

*Continuous run servo counter clockwise direction*

`>>> a.ccw(12)`

*Continuous run servo clockwise direction*

`>>> a.cw(12)`

*Stop servo*

`>>> a.cw(0)`

*Close serial port*

`>>> a.closeSerial()`

---
####Resources

[wCK User's Manual](http://robosavvy.com/RoboSavvyPages/Robobuilder/robobuilder-creator-users-manual.pdf)

[wCK Programmer User's Manual](http://www.tribotix.com/Downloads/RoboBuilder/wCK/User%20Manual%20_wCK%20programmer%20tool_%20v1.03%20EN.pdf)

[Understanding wCK module and 
C programming with RoboBuilder](http://ro-botica.com/img/Robobuilder/RoboBuilder%20C_tutorial%20.pdf)