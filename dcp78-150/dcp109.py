from math import log
from math import ceil
#Swap even-odd bits
#-Swap bits[0] with bits[1], bits[2] and bits [3], etc
#01 -> 10
#To get the odd bits, let's bitwise-and the byte with a byte only with odd bits == 1
#To get even bits, bitwise-and for every 2^n bit where n % 2 == 1

def swap_bits(bitlist):
    #So let's assume bitlist is any positive integer
    #The hex of odd bits is 0xaa... and even bits is 0x55... (10101010 and 01010101 respectively)
    oddbits = 0xa
    evenbits = 0x5
    while(oddbits < bitlist):
        oddbits = (oddbits<<4) + 0xa
        evenbits = (evenbits<<4) + 0x5
    bitlist = (bitlist & oddbits) + (bitlist & evenbits)
    return bitlist

def swap_byte(byte):
    #Assuming that the given integer is a byte (unsigned 8bit int)
    return (byte & 0x55) + (byte & 0xaa)

if __name__ == "__main__":
    base = 0xe2
    print(swap_byte(base))