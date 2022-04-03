import socket
import requests
import whois
domain=input('input domain:')
ip=socket.getaddrinfo(domain,None)
print(ip[0][4][0])
info=whois.whois(domain)
print(info)


