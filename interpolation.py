import numpy as np
import matplotlib.pyplot as plt
from collections import deque
 
def calcCoefficinet(x_array,y_array):
    coefs = np.linalg.solve(x_array, y_array)
    return coefs

def f(x,coefs):
    result = 0
    for i in range(0,coefs.size):
        result+=pow(x,i)*coefs[coefs.size-1-i]
    return result

def plot(coefs):
    x=np.linspace(-10,10,100)
    y=f(x,coefs)

    plt.plot(x,y)
    plt.show()
    print(f(10,coefs))

def createMatrix(x):
    matrix = np.array([])
    matrix.resize((len(x),len(x)))
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

    
