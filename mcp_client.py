import socket

class MCPClient:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print(f'Connected to {self.host}:{self.port}')

    def send_request(self, request):
        if self.sock is None:
            raise Exception('Client is not connected.')
        self.sock.sendall(request.encode('utf-8'))
        response = self.sock.recv(4096)
        return response.decode('utf-8')

    def close(self):
        if self.sock:
            self.sock.close()
            print('Connection closed.')
