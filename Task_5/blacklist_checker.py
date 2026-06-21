blacklist = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.1.100",
    "192.168.0.50"
]

ip = input("Enter an IP Address: ")

found = False

for blocked_ip in blacklist:
    if blocked_ip == ip:
        found = True
        break

if found:
    print("IP Found in Blacklist")
else:
    print("IP Not Found")