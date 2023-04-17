import numpy as np
from collections import deque
 
def calcCoefficinet(x_array,y_array):
    coefs = np.linalg.solve(x_array, y_array)
    return coefs

def f(x,coefs):
    result = 0
    for i in range(0,coefs.size):
        result+=pow(x,i)*coefs[coefs.size-1-i]
    return result

def createMatrix(x):
    matrix = np.array([])
    matrix.resize((len(x),len(x)),refcheck=False)
    help = []
    list = deque()
    for element in x:
        for i in range(len(x)-1,-1,-1):
            help.append(pow(element,i))
        list.append(help)
        help=[]
    result = np.array(list)
    return result
    ###END

    
