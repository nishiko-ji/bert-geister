import socket


class Client:
    """ miyo/geister_serverとのtcp通信用client

    Attributes:
        ip (str): サーバのIPアドレス
        port (int): サーバのポート番号
        sock (socket): tcp通信ソケット
    """
    def __init__(self, ip: str = '127.0.0.1', port: int = 10000) -> None:
        """ 初期化

        IPアドレスとポート番号を格納し、ソケットを生成する

        Args:
            ip (str): サーバのIPアドレス
            port (int): サーバのポート番号
        """
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open(self) -> bool:
        """ ポートを開く
        """
        try:
            self.sock.connect((self.ip, self.port))
            print(f'{self.ip}に接続しました')
            return True
        except InterruptedError as e:
            print(e)
            print(type(e))
            print(f'{self.ip}に接続できませんでした')
            return False

    def close(self) -> None:
        """ ポートを閉じる
        """
        self.sock.close()

    def send(self, data: str) -> None:
        """ データの送信

        Args:
            data (str): 送信するデータ
        """
        self.sock.send(f'{data}\r\n'.encode('utf-8'))

    def recieve(self) -> str:
        """ データの受信

        Returns:
            str: 受信したデータ
        """
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
