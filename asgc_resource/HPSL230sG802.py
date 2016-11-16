import pyssh

class Default:

    def __init__(self, mmip, bay):
    
        self.session = pyssh.new_session(hostname=mmip, port="22", username="<username>", password="<password>")

    def poweron(self):
        self.session.execute("power on")

    def poweroff(self):
        self.session.execute("power off")
 
    def powerrestart(self):
        self.session.execute("power reset")

    def uidon(self):
        self.session.execute("uid on")

    def uidoff(self):
        self.session.execute("uid off")

    def powerstatus(self):
        command=self.session.execute("power")
        command_out="".join(command._data)
        if "On" in command_out:
           return "On"
        else:
           return "Off"        
