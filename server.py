import socket

#서버 ip & port
server_ip = '127.0.0.1'
port = 9999

#서버 소켓 준비
server = socket.socket()

server.bind((server_ip, port))
server.listen(1)
print('---- Server is ready ----')

#클라이언트 접속 수락
client, adder = server.accept()
print('---- Client is connected ----')

#메세지 수신
msg = client.recv(1024)
print('---- Message received ----')
print(msg)

#메세지 송신
client.send(b'Hi Hi i\'m server.You\'re name if :' + msg)
print('---- Message send ----')

#해제
client.close()
server.close()