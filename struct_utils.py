import struct
def type2bin(num, fmt):
    ll = [bin(ord(c)) for c in struct.pack(fmt, num)]
    res = []
    for item in ll:
        res.append(item.replace('0b', '').rjust(8, '0'))
    return ''.join(res)

def bin2type(bits, fmt):
    return struct.unpack(fmt, struct.pack(fmt, int(bits, 2)))[0]


def float2bin(num):
    return type2bin(num, '>f')

def bin2float(bits):
    return bin2type(bits, '>f')

def int2bin(num):
    return type2bin(num, '>i')

def bin2int(bits):
    return bin2type(bits, '>i')

def bin2long(bits):
    return bin2type(bits, '>q')

def long2bin(num):
    return type2bin(num, '>q')

def unpack_int(bytes):
    return struct.unpack('>i', bytes)[0] 

def unpack_long(bytes):
    return struct.unpack('>q', bytes)[0]


