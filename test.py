import timeit
from interpolation import *


def sub(x,y):
    mat=createMatrix(x)
    coefs = calcCoefficinet(mat,y)


def main():
    x = [0, 0.5, 1, 1.5, 2, 2.5, 3]
    y = [0, 2, 4, 6, 8, 10, 12]
    print(timeit.timeit(lambda:sub(x,y),number=1000000))


if __name__=="__main__":
    main()
