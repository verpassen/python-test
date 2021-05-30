#!/usr/bin/env python
import numpy as np 
import pandas as pd 

def add_rowj2i(A,k,i,j):
    A [i] = A[j]*k + A[i]
    return A
def scalar_row(A,i,k):
    A[i] = A[i]*k
    return A 
def switch_row(A,i,j):
    A[[i ,j]] = A[[j,i]]
    return A
def gassian_elim(M):
    (row,col) = M.shape
    for i in range(row-1):	
        Ms = scalar_row(M,i,1/M[i][i])
        k = [s for s in np.arange(row) if s!= i]
        for j in k:
            Ms = add_rowj2i(Ms,-M[j][i],j,i)    
    return Ms

file_path = './test_data/Q_data.csv'
df = pd.read_csv(file_path)
print(df.keys())
print(df.describe())
#===========================================

A = np.array([[2,4,3],[2,-1,0],[3,3,2]])
B = np.array([[15],[10],[-5]])
M = np.hstack([A,B]).astype(float)
C = np.array([[20,607.7,618.8],[607.7,18775.15,19073.12],[618.8,19073.12,19569.94]])#.astype(float)

D = np.array([[1,33.5,30.7],[1,29,25],[1,34.9,37.3],[1,32.5,37.3],[1,25.2,24.8],[1,31.7,27.3],
[1,23.4,22],[1,33.6,35],[1,37.5,38.7],[1,31,29.7],[1,27.6,34.4],[1,32.5,32.7],[1,22.8,27.2],[1,27.5,30.6],[1,31.7,35.6],
[1,36.7,32.6],[1,29.9,30.9],[1,30.9,33.7],[1,26.8,26],[1,29,27.3]])
M = np.dot(D.transpose(),D)
print("+===========================+")
print(M)
print(gassian_elim(M))


'''
        Ms = scalar_row(M,0,1/M[0][0])
	    Ms = add_rowj2i(Ms,-M[1][0],1,0)
	    Ms = add_rowj2i(Ms,-M[2][0],2,0)

	    Ms = scalar_row(Ms,1,1/M[1][1])
	    Ms = add_rowj2i(Ms,-M[0][1],0,1)
	    Ms = add_rowj2i(Ms,-M[2][1],2,1)
	
	    Ms = scalar_row(Ms,2,1/M[2][2])
	    Ms = add_rowj2i(Ms,-M[0][2],0,2)
	    Ms = add_rowj2i(Ms,-M[1][2],1,2)
'''