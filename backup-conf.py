

from netmiko import Netmiko

from datetime import datetime

now = datetime.now()

date = now.strftime("%d/%m/%Y, %H:%M:%S")

username = "victor"
password = "notapassword51"

SW1 = {
   "host" : "192.168.15.10",
   "username" : username,
   "password" : password,
   "device_type" : "cisco _ios"
}

SW2 = {
   "host" : "192.168.15.27",
   "username" : username,
   "password" : password,
   "device_type" : "cisco _ios"
}

SW3 = {
   "host" : "192.168.15.66",
   "username" : username,
   "password" : password,
   "device_type" : "cisco_ios"
}

SW4 = {
   "host" : "192.168.15.31",
   "username" : username,
   "password" : password,
   "device_type" : "cisco_ios"
}

SW5 = {
   "host" : "192.168.15.22",
   "username" : username,
   "password" : password,
   "device_type" : "cisco_ios"
}

my_switches = [SW1, SW2, SW3, SW4, SW5]

for x in my_switches:
   net_connect = Netmiko(**x)
   showver = net_connect.send_command("show version",use textfsm=True)
   showrun = net_connect.send_command("show run")
   hostname = showver[0]['hostname']
   backupfilename = hostname |" "| date | ".txt"
   file = open(backupfilename, "backitup")
   file.write(showrun)
   file.close()
   print(hostname + " has been backed up" + "\n")
   net_connect.disconnect()