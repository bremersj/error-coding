# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:58:05 2017

@author: steve
"""

from data import get_data

from GF2Matrix import GF2Matrix

ASCII = {'0':'00110000',
         '1':'00110001',
         '2':'00110010',
         '3':'00110011',
         '4':'00110100',
         '5':'00110101',
         '6':'00110110',
         '7':'00110111',
         '8':'00111000',
         '9':'00111001',
         ':':'00111010',
         ';':'00111011',
         '<':'00111100',
         '=':'00111101',
         '>':'00111110',
         '?':'00111111',
         '@':'01000000',
         'A':'01000001',
         'B':'01000010',
         'C':'01000011',
         'D':'01000100',
         'E':'01000101',
         'F':'01000110',
         'G':'01000111',
         'H':'01001000',
         'I':'01001001',
         'J':'01001010',
         'K':'01001011',
         'L':'01001100',
         'M':'01001101',
         'N':'01001110',
         'O':'01001111',
         'P':'01010000',
         'Q':'01010001',
         'R':'01010010',
         'S':'01010011',
         'T':'01010100',
         'U':'01010101',
         'V':'01010110',
         'W':'01010111',
         'X':'01011000',
         'Y':'01011001',
         'Z':'01011010',
         'a':'01100001',
         'b':'01100010',
         'c':'01100011',
         'd':'01100100',
         'e':'01100101',
         'f':'01100110',
         'g':'01100111',
         'h':'01101000',
         'i':'01101001',
         'j':'01101010',
         'k':'01101011',
         'l':'01101100',
         'm':'01101101',
         'n':'01101110',
         'o':'01101111',
         'p':'01110000',
         'q':'01110001',
         'r':'01110010',
         's':'01110011',
         't':'01110100',
         'u':'01110101',
         'v':'01110110',
         'w':'01110111',
         'x':'01111000',
         'y':'01111001',
         'z':'01111010'}
         
ASCIIR = {code:letter for letter, code in ASCII.items()}
         
ASCII7 = {'0':'0110000',
         '1':'0110001',
         '2':'0110010',
         '3':'0110011',
         '4':'0110100',
         '5':'0110101',
         '6':'0110110',
         '7':'0110111',
         '8':'0111000',
         '9':'0111001',
         ':':'0111010',
         ';':'0111011',
         '<':'0111100',
         '=':'0111101',
         '>':'0111110',
         '?':'0111111',
         '@':'1000000',
         'A':'1000001',
         'B':'1000010',
         'C':'1000011',
         'D':'1000100',
         'E':'1000101',
         'F':'1000110',
         'G':'1000111',
         'H':'1001000',
         'I':'1001001',
         'J':'1001010',
         'K':'1001011',
         'L':'1001100',
         'M':'1001101',
         'N':'1001110',
         'O':'1001111',
         'P':'1010000',
         'Q':'1010001',
         'R':'1010010',
         'S':'1010011',
         'T':'1010100',
         'U':'1010101',
         'V':'1010110',
         'W':'1010111',
         'X':'1011000',
         'Y':'1011001',
         'Z':'1011010',
         'a':'1100001',
         'b':'1100010',
         'c':'1100011',
         'd':'1100100',
         'e':'1100101',
         'f':'1100110',
         'g':'1100111',
         'h':'1101000',
         'i':'1101001',
         'j':'1101010',
         'k':'1101011',
         'l':'1101100',
         'm':'1101101',
         'n':'1101110',
         'o':'1101111',
         'p':'1110000',
         'q':'1110001',
         'r':'1110010',
         's':'1110011',
         't':'1110100',
         'u':'1110101',
         'v':'1110110',
         'w':'1110111',
         'x':'1111000',
         'y':'1111001',
         'z':'1111010'}

AA =    {'A':'00001',
         'B':'00010',
         'C':'00011',
         'D':'00100',
         'E':'00101',
         'F':'00110',
         'G':'00111',
         'H':'01000',
         'I':'01001',
         'J':'01010',
         'K':'01011',
         'L':'01100',
         'M':'01101',
         'N':'01110',
         'O':'01111',
         'P':'10000',
         'Q':'10001',
         'R':'10010',
         'S':'10011',
         'T':'10100',
         'U':'10101',
         'V':'10110',
         'W':'10111',
         'X':'11000',
         'Y':'11001',
         'Z':'11010'}

DD = {'0':'0001',
      '1':'1000',
      '2':'0101',
      '3':'1001',
      '4':'0011',
      '5':'1010',
      '6':'1011',
      '7':'0111',
      '8':'0010',
      '9':'1101',
      ' ':'0110',
      '?':'1111',
      '.':'0100',
      ',':'1110',
      '/':'1100'}
         
def char_enc(fn, cmap):
    data = get_data(fn)
    result = []
    out_fn = fn[:-4] + '_enc.txt'

    print('Starting.')
    for line in data:
        new_line = ''
        for char in line:
            new_line += cmap[char]
        result.append(new_line)

    with open(out_fn, 'w') as f:
        f.write('\n'.join(result))

    print('Done. Output file:', out_fn)
    
def chan_enc_by_char(fn, G_fn, P_fn, charmap):
    data = get_data(fn)
    out_fn = fn[:-4] + '_enc.txt'
    
    M = GF2Matrix(get_data(G_fn))
    P = GF2Matrix(get_data(P_fn))
    G = M*P
    result= []

    for line in data:
        enc_line = ''
        for char in line:
            W = GF2Matrix([charmap[char]])
            C = W*G
            enc_line += C.data[0]
        result.append(enc_line)
    
    with open(out_fn, 'w') as f:
        f.write('\n'.join(result))
        
    print('Output file:', out_fn)

def chan_enc_by_line(fn, G_fn, P_fn=0):
    out_fn = fn[:-4] + '_enc.txt'
    
    W = GF2Matrix(get_data(fn))
    M = GF2Matrix(get_data(G_fn))
    if P_fn != 0:
        P = GF2Matrix(get_data(P_fn))
        G = M*P
    else:
        G = M
    G.display()
    C = W*G
    #C.display()
    
    with open(out_fn, 'w') as f:
        f.write('\n'.join(C.data))
    print('Output file:', out_fn)
    
def char_line_encode(fn, G_fn, charmap):
    print('Starting...')
    out_fn = fn[:-4] + '_enc.txt'

    # char encode from file fn
    words = get_data(fn)
    char_enc = []
    for line in words:
        enc_line = ''
        for char in line:
            enc_line += charmap[char]
        char_enc.append(enc_line)
        
    # encode char encoded words
    G = GF2Matrix(get_data(G_fn))
    W = GF2Matrix(char_enc)
    
    CW = W*G

    with open(out_fn, 'w') as f:
        f.write('\n'.join(CW.data))
                 
    print('Done. Output file: %s' % (out_fn))
        
def interleave(fn, num_rows):
    data = get_data(fn)
    result = []
    out_fn = fn[:-4] + '_inter.txt'
    for i in range(0, len(data), num_rows):
        new_line = ''
        for j in range(0, len(data[i])):
            for row in range(num_rows):
                try:
                    new_line += data[i+row][j]
                except:
                    break

        result.append(new_line)
    
    with open(out_fn, 'w') as f:
        f.write('\n'.join(result))
        
    print('Output file:', out_fn)

    
if __name__ == '__main__':
    char_enc('r5d.txt', DD)
    