from ipaddress import *

net = ip_network('178.176.0.0/255.240.0.0', 0)
mx = 0
a = []
for ip in net:
    if bin(int(ip))[2:].count('1') == bin(int(ip))[2:].count('0'):
        a.append(sum([int(x) for x in str(ip).split('.')]))

print(max(a))




