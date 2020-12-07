# Pinging AWS EC2 public IPv4.
# # I worked with Vlado, Dorin and Igor, Mohammad and Seid on this code.
# i fixed myself the paramiko code and i found from the code in github
# Liviu Patrisco help us (Liviu_patrisco@hotmail.com) helped us to write the code

# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by abdirizak")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    ec2_ip_address = "3.135.203.215"
    server = Server(ec2_ip_address)
    result = server.ping()
    print(result)
    if result == 0:
        print("Server with ip [%s] is up." % ec2_ip_address)
    else:
        print("Server with ip [%s] is down." % ec2_ip_address)
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.135.203.215', username='ubuntu', key_filename='C:\\Users\\kulmi\\.ssh\\id_rsa')

stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')

for line in stdout.read().splitlines():
    print(line)

ssh.close()