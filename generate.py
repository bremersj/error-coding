# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:57:46 2018

@author: steve

Functions to generate random matrices and files with random characters.
"""

import numpy as np

AZ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def gen_rand_matrix(output_fn, row, col, low, high):
    result = []
    print('Starting...')
    
    for i in range(row):
        line = ''
        for j in range(col):
            line += str(np.random.randint(low, high+1))
        result.append(line)
    
    with open(output_fn, 'w') as f:
        f.write('\n'.join(result))
    
    print('Done. Ouput file: %s' % (output_fn))
    return result

def gen_rand_chars(output_fn, row, col, charset):
    result = []
    print('Starting...')
    set_size = len(charset)
    
    for i in range(row):
        line = ''
        for j in range(col):
            rindex = np.random.randint(0, set_size)
            line += charset[rindex]
        result.append(line)
        
    with open(output_fn, 'w') as f:
        f.write('\n'.join(result))
    
    print('Done. Output file: %s' % (output_fn))
    return result

if __name__ == '__main__':
    #gen_rand_matrix('r40x104.txt', 40, 100, 0, 1)
    gen_rand_matrix('r5d.txt', 2000, 5, 0, 9)
    #gen_rand_chars('r4c.txt', 400, 4, AZ)