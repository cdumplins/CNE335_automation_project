import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):
        response = os.system("ping -c 1 " + self.server_ip)
        if response == 0:
            return "Server is up!"
        else:
            return "Server is down!"

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Calvin")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    server = Server("35.86.106.84")
    result = server.ping()
    print(result)
