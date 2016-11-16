import subprocess
import shlex

class Default:

    def __init__(self, mmip, bay):
	
	self.mmip = mmip
	self.bay = bay

    @staticmethod
    def __runcmd(cmd):
        args = shlex.split(cmd)
        subprocess.Popen(args)

    def poweron(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> power on".format(self.mmip)
        args = self.__runcmd(cmd)

    def poweroff(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> power soft".format(self.mmip)
        args = self.__runcmd(cmd)
 
    def powerrestart(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> power reset".format(self.mmip)
        args = self.__runcmd(cmd)

    def powerstatus(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> power status".format(self.mmip)
        args = shlex.split(cmd)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for LINE in  proc.stdout:
            if "on" in LINE.lower() : return "On"
            if "off" in LINE.lower() : return "Off"

    def uidon(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> chassis identify force".format(self.mmip)
        args = self.__runcmd(cmd)

    def uidoff(self):
        cmd = "ipmitool -I lan -H {0} -U <user> -P <user> chassis identify 0".format(self.mmip)
        args = self.__runcmd(cmd)
