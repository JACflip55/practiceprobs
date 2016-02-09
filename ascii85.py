#implement the Acsii85 encoding/deconding in python


import struct
def toAscii85(data):
    #add padding
    padding = 0
    while len(data)%4 != 0:
        data+='\0'
        padding += 1
    #init offsets
    foffset = 0
    loffset = 4
    encodedtext = ''
    while len(data) >= loffset:   
        binary = struct.unpack('>I', data[foffset:loffset])
        inttext = binary[0]
        encoded4b = ''
        #encode 4 bytes into 5 chars
        for x in range(0, 5):
            encoded4b = str(unichr(inttext%85+33))+encoded4b
            inttext /= 85
        foffset += 4
        loffset += 4
        encodedtext += encoded4b
    # Encode data to ASCII85
    if padding != 0:
        encodedtext = encodedtext[:-padding]
    return '<~'+encodedtext+'~>'
    
def fromAscii85(data):
    # Decode data from ASCII85
    return
