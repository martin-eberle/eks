import socket
import time
import codecs

class Response:
    def __init__(self, status, payload):
        self.status = status
        self.payload = payload

class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock = None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def close(self):
        self.sock.close()

    def mysend(self, msg):
        print('Send command: ' + str(msg))
        bytes_sent = self.sock.send(msg)
        return bytes_sent
        # totalsent = 0
        # while totalsent < len(msg):
        #     sent = self.sock.send(msg[totalsent:])
        #     if sent == 0:
        #         raise RuntimeError("socket connection broken")
        #     totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        msglen = 123
        command = ''
        status = -1

        while bytes_recd < msglen:
            chunk = codecs.decode(self.sock.recv(1), 'ASCII')
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)

            if bytes_recd == 0:
                msglen = ord(chunk)
            if bytes_recd == 1:
                command += chunk
            if bytes_recd == 2:
                command += chunk
            if bytes_recd == 6:
                status = ord(chunk)

            bytes_recd = bytes_recd + len(chunk)
            print("(" + str(bytes_recd - 1) + ") \t" + str(ord(chunk)) + "\t" + str(msglen))

        # if bytes_recd > 3:
        # print command + "/" + str(status)
        # print ''.join(chunks)
        if command == "Ek":
            if status == 1:
                return Response("EKS_KEY_IN", None)
            if status == 2:
                return Response("EKS_KEY_OUT", None)
            if status == 3:
                return Response("EKS_KEY_OTHER", None)
        else:
            return Response(command, ''.join(chunks))

mysock = mysocket()
mysock.connect("192.168.1.1", 2444)
status = ''

while True:
    # hex code for reading key status: 07 45 6B 01 00 00 74 = 7 E k 1 0 0 0
    byteCode = codecs.decode('07456B01000000', 'hex')
    mysock.mysend(byteCode)
    new_status = mysock.myreceive().status

    if new_status != status:
        print('old status:')
        print(status)
        print('new status:')
        status = new_status
        print(status)

    if status == "EKS_KEY_IN":
        # hex code for reading key payload: 07 54 4C 01 00 00 74 = 7 T L 1 0 0 t ?
        byteCode = codecs.decode('07544C01000074', 'hex')
        mysock.mysend(byteCode)
        print(mysock.myreceive().payload)
