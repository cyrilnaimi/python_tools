import struct

def floatTo2Short(f):
    listi = []
    bf = struct.pack('f', f)
    listf = list(struct.unpack('HH', bf))
    return listf[::-1]

print(floatTo2Short(725.730))
