import numpy as np
from collections import deque
import matplotlib.pyplot as plt

class NevillePoly:
    """ Constructor, assign + call functions to calculate coefficients"""
    def __init__(self,x,y):
        self.x_array=x
        self.y_array=y
        self.mat=self.createMatrix(x)
        self.coefs = self.calcCoefficinet(self.mat,y)
    
    def calcCoefficinet(self,x_array,y_array):
        coefs = np.linalg.solve(x_array, y_array)
        return coefs

    """ Get values of functiond """
    def f(self,x,coefs):
        result = 0
        for i in range(0,coefs.size):
            result+=pow(x,i)*coefs[coefs.size-1-i]
        return result
    """ Convert given array to matrix form (maybe too complicated?)"""
    def createMatrix(self,x):
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
    
        
class LagrangePoly:
    """ Constructor, only assign"""
    def __init__(self, X, Y):
        self.n = len(X)
        self.X = np.array(X)
        self.Y = np.array(Y)
    """ Function to give single lagrange polynomial for corresponding x,j"""
    def basePoly(self, x, j):
        b = [(x - self.X[m]) / (self.X[j] - self.X[m])
             for m in range(self.n) if m != j]
        return np.prod(b, axis=0) * self.Y[j]
    """ Call for lagrange polonomials and return expected y values"""
    def interpolate(self, x):
        b = [self.basePoly(x, j) for j in range(self.n)]
        return np.sum(b, axis=0)

class NewtonPolynom:
    
    """ Constructor, assign + call to calculate coefficients"""
    def __init__(self,x,y):
        self.x_array=x
        self.y_array=y
        self.coefs = self.coef(self.x_array,self.y_array)
        
    """ Returns array of coefficients through divided differences"""
    def coef(self,x, y):
        n = len(x)
        coefs_array= []
        for i in range(n):
            coefs_array.append(y[i])
        for j in range(1, n):
            for i in range(n-1, j-1, -1):
                coefs_array[i] = (coefs_array[i]-coefs_array[i-1])/(x[i]-x[i-j])
        return np.array(coefs_array) 
    """ Returns expected y values """
    def evaluate(self,coefs, x_datapoints, to_eval):
        n = len(coefs) - 1
        temp = coefs[n] + (to_eval - x_datapoints[n])
        for i in range( n - 1, -1, -1 ):
            temp = temp * (to_eval - x_datapoints[i] ) + coefs[i]
        return temp 
