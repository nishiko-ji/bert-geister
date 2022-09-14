import socket


class Client:
    def __init__(self, ip='127.0.0.1', port=10000):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self):
        self.sock.connect((self.ip, self.port))

    def close(self):
        self.sock.close()

    def send(self, data):
        self.sock.send(f'{data}\r\n'.encode('utf-8'))

    def recieve(self):
        return self.sock.recv(1024).decode('utf-8').replace('\r\n', '')

if __name__ == '__main__':
    ip = input('IPアドレス＞')
    port = int(input('ポート＞'))
    cl = Client(ip, port)
    cl.open()
    print(cl.recieve())
    cl.send("SET:ABCD")
    print(cl.recieve())

    print(cl.recieve())
