import socket

domain = input('input domain:\n')

with open('subdomain.txt','r') as f:
    for i in f:
        i = i.strip()
        subdomain = i + '.'+domain
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"\033[1;31m{subdomain} : {ip}\033[0m")
        except:
            print("loading...")