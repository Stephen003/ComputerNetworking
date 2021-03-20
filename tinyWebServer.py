# 参考 https://zhuanlan.zhihu.com/p/34880601

from socket import *
import sys

# prepare a socket
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))  # 套接字与某一端口绑定
serverSocket.listen(1)
print ("The server is ready to receive")

while True:
    # establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode() # 对收到的套接字进行解码
        filename = message.split(' ')[1]
        f = open(filename[1:])
        outputdata = f.read() # 读取IO
        # Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\r\n\r\n"  # 发生http首部
        connectionSocket.send(header.encode())
        # Send the content of the requestd file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    
    except IOError:
        # Send response message for file not found
        header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.close()

        # close client socket

    serverSocket.close()

    sys.exit() # terminate the program after sending the corresponding data