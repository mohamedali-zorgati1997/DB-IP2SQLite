
#to make search easier we use this function of converting an ip address to an integer
def ip4_2_int(ip):
    addr = 0
    for i, j in enumerate(map(int, ip.split("."))):
        addr += (j<<((3-i)*8))
    return addr

def int_2_ip4(ip):
    ip = '{:08x}'.format(ip)
    addr = []
    for i in range(0, 8,2):
        addr.append(str(int(ip[i:i+2], 16)))
    return ".".join(addr)

