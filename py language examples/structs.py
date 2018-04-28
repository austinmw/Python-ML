from struct import *

# Usage example (pack and unpack):

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73) # convert to byte format
print(packed_data)

print(calcsize('i')) # number of bytes in value
print(calcsize('f'))
print(calcsize('iif'))

# To get byte data back to normal
orginal_data = unpack('iif', packed_data)
print(orginal_data)

# or
print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00)\\\x97@'))