# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:38:08 2018

@author: Steve Bremer

Blog author Jeremy Kun (j2kun) provided a lot of useful sample code that 
helped me write this PolyF2 class. His work is probably much more robust and
useful than what I have here. Here's the link to his better work:
    https://jeremykun.com/2014/03/13/programming-with-finite-fields/
"""

def simplify(C, l):
    if len(C) == 0:
        return C
    if 1 not in C:
        return []
    i = 0
    while(C[i] == l):
        i += 1
    
    return C[i:]

def addF2(a, b):
    return (a+b)%2

def bin_val(n):
    if n.isZero():
        return 0
    v = ''.join([str(x) for x in n])
    return int(v, 2)

class PolyF2:
    def __init__(self, C):
        self.coefficients = simplify(C, 0)
    
    def __iter__(self): 
        return iter(self.coefficients) 
    def __len__(self):
        return len(self.coefficients)
    
    def iter(self):
        return self.__iter__()
    
    def isZero(self): 
        return self.coefficients == []
 
    def __repr__(self):
        if self.isZero():
            return '0'
 
        return ' + '.join(['%s x^%d' % (x,i) if i > 0 else '%s'%x
                           for i,x in enumerate(reversed(self.coefficients))]) 
    
    def __add__(self, other):
        slen = len(self)
        olen = len(other)
        if slen > olen:
            diff = slen-olen
            other = [0]*diff + other.coefficients
        elif olen > slen:
            diff = olen-slen
            self = [0]*diff + self.coefficients
        newC = ([addF2(a, b) for a,b in zip(self, other)])
        return PolyF2(newC)
    def __sub__(self, other):
        return self+other
    def __mul__(self, other):
        m = int(''.join(str(x) for x in other.coefficients), 2)
        mul_sum = 0
        len_self = len(self)
        for i in range(len_self):
            if self.coefficients[i] == 1:
                mul_sum = mul_sum^(m << (len_self-i-1))
        result = [int(x) for x in bin(mul_sum)[2:]]
        return PolyF2(result)
                
    def __truediv__(self, other):
        divisor = other
        dividend = self
        if bin_val(dividend) < bin_val(divisor):
            return(PolyF2([]), PolyF2([]))
        elif bin_val(dividend) == bin_val(divisor):
            return(PolyF2([1]), PolyF2([]))
        quotient = []
        while (bin_val(dividend) >= bin_val(divisor)):
            deg = len(dividend)
            div_add = PolyF2(divisor.coefficients)
            div_add.coefficients += [0]*(len(dividend) - len(divisor))
            dividend += div_add
            quotient += [1]
            quotient += [0]*(deg - len(dividend) - 1)
        if dividend.isZero():
            remainder = PolyF2([])
        else:
            remainder = dividend
        return (PolyF2(quotient), remainder)
            
            
            

if __name__ == '__main__':
    A = PolyF2([1,0,0,1,1])
    B = PolyF2([1,1])
    M = A*B
    print(M)