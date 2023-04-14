import timeit
from interpolation import *


def sub(x,y):
    mat=createMatrix(x)
    coefs = calcCoefficinet(mat,y)


def test():
    size=100
    x= np.empty(size,dtype=int)
    for i in range(0,size):
        x[i]=i

    y = np.empty(size,dtype=int)
    for i,ele in enumerate(x):
        y[i]=pow(ele,2)
    time=timeit.timeit(lambda:sub(x,y),number=10)
    print(time)
    print(y)

if __name__=="__main__":
    test()
