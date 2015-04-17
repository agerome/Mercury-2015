import socketserver
import socket
import time

class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    
    Example from the Python UDP Example
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
#        print("{} wrote:".format(self.client_address))
        print(chr(data[0]))
#        print("length = {}".format(len(data)))
#        socket.sendto(data.upper(), (self.client_address[0], 5001))
#        print("sent: ", data.upper()[4:9])
#        print("length = {}".format(len(data)))

if __name__ == "__main__":
    #Former ports
    #HOST, PORT = "192.168.43.232", 5001
    HOST, PORT = "localhost", 5001
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
