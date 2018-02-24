# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:28:15 2017

@author: steve

A class to implement certain linear algebra operations over GF(2).
"""

def bitwise_XOR(a, b):
    bitstream = ''
    for i in range(0, len(a)):
        bitstream += str(int(a[i], 2) ^ int(b[i], 2))
    return bitstream

def min_row_pivot(matrix, col, used):
    pivots = len(matrix[0])
    for i in range(0, pivots):
        if (matrix[i][col] == '1') and (used[i] != 1):
            used[i] = 1
            return i
    return -1

def gauss_elim_gf2(matrix):
    num_col = len(matrix[0])
    num_row = len(matrix)
    pivot_matrix = ['']*num_col
    used = [0]*(num_col+1)
    
    for j in range(0, num_col):
        row = min_row_pivot(matrix, j, used)

        if (row != -1):
            pivot_matrix[j] = matrix[row]
            for i in range(0, num_row):
                if i != row:
                    if (matrix[i][j] == '1'):
                        trow = bitwise_XOR(matrix[row], matrix[i])
                        matrix[i] = trow
    return matrix

class GF2Matrix:

    def __init__(self, data):
        self.num_rows = len(data)
        try:
            self.num_cols = len(data[0])
        except:
            raise ValueError('Attempting to define an empty matrix')
        for i in range(self.num_rows):
            if len(data[i]) != self.num_cols:
                raise ValueError('matrix rows must have the same number of columns')
        self.data = data

    def __str__(self):
        return str([row for row in self.data])

    def __mul__(self, other):
        #Check that operation is valid
        try:
            if self.num_cols != other.num_rows:
                raise ValueError('Attempting invalid matrix multiplication')
        except:
            raise ValueError('Multiplying by non-matrix type')
        result = ['']*self.num_rows

        otherT = other.transpose()
        for i in range(self.num_rows):
            new_row = ''
            for j in range(otherT.num_rows):
                bit = 0
                for b in range(self.num_cols):
                    bit = (bit + int(self.data[i][b]) * int(otherT.data[j][b]))%2
                new_row += str(bit)
            result[i] = new_row
        return GF2Matrix(result)

    def append(self, other):
        if type(other) != GF2Matrix:
            print('Type error: appending with', type(other), 'not defined')
            return -1
        if self.num_rows != other.num_rows:
            raise ValueError('attempting invalid matrix multiplication')
        for i in range(self.num_rows):
            self.data[i] += other.data[i]

    def transpose(self):
        new_matrix = ['']*self.num_cols
        for j in range(self.num_cols):
            new_row = ''
            for i in range(self.num_rows):
                new_row += self.data[i][j]
            new_matrix[j] = new_row
        return GF2Matrix(new_matrix)

    def get_col(self, j):
        col_data = ''
        for i in range(self.num_rows):
            col_data += self.data[i][j]
        return col_data

    def remove_col(self, j):
        for i in range(self.num_rows):
            self.data[i] = self.data[i][0:j] + self.data[i][j+1:]

    def insert_col(self, col_data, j):
        for i in range(self.num_rows):
            self.data[i] = self.data[i][0:j] + col_data[i] + self.data[i][j:]

    def move_row(self, fm, to):
        if fm < to:
            self.data.insert(to, self.data[fm])
            del self.data[fm]
        elif fm > to:
            self.data.insert(to, self.data[fm])
            del self.data[fm+1]

    def move_col(self, fm, to):
        if fm < to:
            col_data = self.get_col(fm)
            self.insert_col(col_data, to)
            self.remove_col(fm)
        if fm > to:
            col_data = self.get_col(fm)
            self.remove_col(fm)
            self.insert_col(col_data, to)

    def xor_row(self, a, b):
        new_row = ''
        bit = 0
        for j in range(self.num_cols):
            bit = (int(self.data[a][j]) + int(self.data[b][j])) % 2
            new_row += str(bit)
        self.data[a] = new_row

    def display(self):
        for row in self.data:
            print(row)

    def rref(self):
        rref = gauss_elim_gf2(self.data[:])
        rref.sort(reverse=True)
        return rref

