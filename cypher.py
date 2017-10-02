# CTM Problem 1.5.1
from GF2 import one

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','']

def oneify(bit): return one if int(bit) == 1 else 0

def unoneify(bit): return 1 if bit == one else 0

def filter(textbit, keybit):
    result = ''
    for n in range(len(textbit)):
        result += str(unoneify(oneify(textbit[n]) + oneify(keybit[n])))
    return result

def decode(cyphertext, key): return [alphabet[int(filter(bit, key), 2)] for bit in cyphertext]

# cyphertext = ['10101','00100','10101','01011','11001','00011','01011','10101','00100','11001','11010']
# decode(cyphertext, '10001')
# ['E', 'V', 'E', '', 'I', 'S', '', 'E', 'V', 'I', 'L']