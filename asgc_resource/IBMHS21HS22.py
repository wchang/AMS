import telnetlib
import socket
import sys


class Default:

    def __init__(self, mmip, bay):
        self.mmip = mmip
        self.bay = bay

    def __telnetmm(self, command):
        try:
            tn = telnetlib.Telnet(self.mmip, 23)
        except socket.error:
            print "Connecting to " + self.mmip + " error!"
            tn.close()
        tn.read_until("username: ")
        tn.write("<username>" + "\r")
        tn.read_until("password: ")
        tn.write("<password>" + "\r")
        tn.read_until("system> ")
        target = " -T system:blade[{0}]".format(self.bay)
        tn.write(command + " " + target + "\r")
        tn.read_until("system> ")
        tn.write("exit"+"\r")
        tn.close()

    def poweron(self):
        self.__telnetmm("power -on")

    def poweroff(self):
        self.__telnetmm("power -off")
 
    def powerrestart(self):
        self.__telnetmm("power -cycle")

    def powerstatus(self):
        try:
            tn = telnetlib.Telnet(self.mmip, 23, 5)
        except socket.error:
            STATUS = "Connection Error"
            tn.close()
        tn.read_until("username: ")
        tn.write("<username>" + "\r")
        tn.read_until("password: ")
        tn.write("<password>" + "\r")
        tn.read_until("system> ")
        target = " -T system:blade[{0}]".format(self.bay)
        tn.write("power -state" + " " + target + "\r")
        STATUS = "On" if tn.expect(['On', 'Off'])[-1].split("\r\n")[-1] == "On" else "Off"
        tn.read_until("system> ")
        tn.write("exit"+"\r")
        tn.close()
        return STATUS

    def uidon(self):
        self.__telnetmm("led -loc on") 

    def uidoff(self):
        self.__telnetmm("led -loc off")

