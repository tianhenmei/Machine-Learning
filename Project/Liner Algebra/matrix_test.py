# -*- coding: UTF-8 -*-
from matrix import Matrix

v = [5, 10, 2, 6, 1]
mv = Matrix([
    [5, 10, 2, 6, 1]
])

vT = Matrix([
    [5], 
    [10], 
    [2], 
    [6], 
    [1]])

m = Matrix([
    [8, 7, 1, 2, 3], 
    [1, 5, 2, 9, 5], 
    [8, 2, 2, 4, 1]
])

r = Matrix([
    [40, 35, 5, 10, 15], 
    [5, 25, 10, 45, 25], 
    [40, 10, 10, 20, 5]
])

r = Matrix([
    [3, 1, -1, 2], 
    [-5, 1, 3, -4], 
    [2, 0, 1, -1],
    [1, -5, 3, -3]
])

# print v
print mv
print vT
print m
print r

print m * vT
print r.transpose()

print r.getDet()

r1 = Matrix([
    [1,2,3],
    [2,2,1],
    [3,4,3]
])
print r1.inverse()



