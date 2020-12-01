#abdirizak kulmiyee
#CNA337 Fall 2020


import os
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by abdirizak")
# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()


public_ec2= "3.128.180.44"
responce = os.system('ping -n 4 ' + public_ec2)
# TODO - Create a Server object
# TODO - Call Ping method and print the results
if responce == 0:
    print()
    print(public_ec2, 'is up!')
else:
    print(public_ec2, 'is down!')