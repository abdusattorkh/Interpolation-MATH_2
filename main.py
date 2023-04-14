import numpy as np
import matplotlib.pyplot as plt
import timeit
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

def main():
    x = [0, 0.5, 1, 1.5, 2, 2.5, 3]
    y = [0, 2, 4, 6, 8, 10, 12]
    
    ####CREATE matrix (rough script)
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
    coefs = calcCoefficinet(result,y)
    plot(coefs)
    
    ###END

    
#Execute main    
if __name__== "__main__":
    main()
