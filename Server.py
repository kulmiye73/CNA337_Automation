# Pinging AWS EC2 public IPv4.
#Abdirizak kulmiye
# I got the resource from stackoverflow



class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        import os
        hosts = ["3.139.104.78"]
        for host in hosts:
            os.system('ping ' + host)

            return hosts
#TODO - Use os module to ping the server

x = Server('server_ip')

x.ping()