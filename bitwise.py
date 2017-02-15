'''
masking bits to find and turn bits on or off, can be used with OR or XOR operators too.
'''
#AND checks to see if the forth bit in given number is on or off
def check_bit4(inputs):
    input = bin(inputs)
    check = 0b1000
    forth = inputs & check
    if forth > 0:
        return "on"

    elif forth == 0:
        return "off"

print check_bit4(8)

#OR (turning on third bit from the right by using OR operator
a = 0b10111011
mask = 0b100
desired = a | mask
print bin(desired)

#XOR to flip all bits in a
a = 0b011101110
b = 0b11111111
c = a ^ b
print bin(c)