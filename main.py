#Abdirizak kulmiye
#updating and upgading server
#I got the resource from stackoverflow
# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by abdirizak")
    print("&"*50)

# This is the entry point to our program
if __name__ == '__main__':

    print_program_info()

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='3.139.104.78', username='ubuntu', key_filename='C:\\Users\\kulmi\\.ssh\\id_rsa')

stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')

for line in stdout.read().splitlines():
    print(line)
