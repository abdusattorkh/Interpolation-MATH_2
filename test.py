import timeit
from interpolation import *
import math
import matplotlib.pyplot as plt



def plot(coefs,x_space): 
    y=f(x_space,coefs)

    plt.plot(x_space,y)
    plt.show()
    
def main(x,y):
    mat=createMatrix(x)
    coefs = calcCoefficinet(mat,y)

    plot(coefs,x)


    

