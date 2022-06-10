import socket

res = socket.getaddrinfo("www.naver.com", 80)
print(res)