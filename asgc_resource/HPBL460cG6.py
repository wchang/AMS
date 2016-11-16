import pyssh

class Default:

    def __init__(self, mmip, bay):
    	
	
	self.bay=bay
        self.session = pyssh.new_session(hostname=mmip, port="22", username="<username>", password="<password>")

    def poweron(self):
	cmd = "POWERON SERVER {}".format(self.bay)	
        self.session.execute(cmd)

    def poweroff(self):
	cmd = "POWEROFF SERVER {}".format(self.bay)
        self.session.execute(cmd)
 
    def powerrestart(self):
	cmd = "REBOOT SERVER {}".format(self.bay)
        self.session.execute(cmd)

    def uidon(self):
        cmd = "SET SERVER UID {} ON".format(self.bay)
        self.session.execute(cmd)

    def uidoff(self):
	cmd = "SET SERVER UID {} OFF".format(self.bay)
        self.session.execute(cmd)

    def powerstatus(self):
        cmd = "SHOW SERVER STATUS {} ".format(self.bay)
        command=self.session.execute(cmd)
        command_out="".join(command._data)
        if "Power: On" in command_out:
           return "On"
        else:
           return "Off"
