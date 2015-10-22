'''
Created on Oct 22, 2015

@author: tomas
'''
L = [2 ** i for i in range(7)]

print(L)
X = 5

if 2 ** X in L:
    print(2 ** X, 'at index', L.index(2 ** X))
else:
    print(X, 'not found')
