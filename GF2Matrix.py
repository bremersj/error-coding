# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 22:28:15 2017

@author: steve

A class to implement certain linear algebra operations over GF(2).
"""

def row_swap(matrix, to_index, fm_index):
    row = matrix.pop(fm_index)
    matrix.insert(to_index, row)

def xor(a,b):
    assert len(a) == len(b)
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def reduce(matrix, index):
    comp = matrix[index]
    for i, line in enumerate(matrix):
        if (index != i):
            if line[index] == '1':
                matrix[i] = xor(line, comp)

def find_rref(matrix):
    """ Calculates the reduced row echelon form of a matrix over a binary
    Galois field.
    Arg: A list of binary strings representing the matrix. For example, 
    ['1001', '1101', '1000'] would represent the following matrix:
        1001
        1101
        1000
    Returns: A list of binary strings reprenting the RREF matrix.
    """
    num_pivots = len(matrix[0])
    
    for i in range(0, num_pivots):
        for j in range(i+1, len(matrix)):
            if matrix[j][i] == '1':
                row_swap(matrix, i, j)
                reduce(matrix, i)
                break
    for line in matrix:
        if '1' in line:
            print(line)
        
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
        return '\n'.join([row for row in self.data])
    
    def __repr__(self):
        return '\n'.join([row for row in self.data])

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
        rref = find_rref(self.data[:])
        rref.sort(reverse=True)
        return rref

if __name__ == '__main__':
    A = GF2Matrix(['11001', '01101', '11000', '01001', '00011', '00010', '11000'])
    print(A)
    Arref = GF2Matrix(A.rref())
    print(Arref)