# Pinging AWS EC2 public IPv4.

# I worked with # Pinging AWS EC2 public IPv4.
# # I worked with Vlado, Dorin and Igor, Mohammad and Seid on this code.
#

# Liviu Patrisco (Liviu_patrisco@hotmail.com) helped us to write the cod

# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by yours")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    ec2_ip_address = "3.128.180.44"
    server = Server(ec2_ip_address)
    result = server.ping()
    print(result)
    if result == 0:
        print("Server with ip [%s] is up." % ec2_ip_address)
    else:
        print("Server with ip [%s] is down." % ec2_ip_address)
