import timeit
from interpolation_naiv import *
import math
import matplotlib.pyplot as plt



def plot(coefs,x_space): 
    y=f(x_space,coefs)
    plt.ylim([-1.5, 1.5])
    plt.xlim([-5, 5])
    plt.plot(x_space,y)
    plt.show()
   
def plotsin(x_space):
    y_space=math.sin(x_space)
    plt.plot(x_space,y_space)
    plt.show()
def main(x,y):
    mat=createMatrix(x)
    coefs = calcCoefficinet(mat,y)

    plot(coefs,x)

def test():
    xy_intervall = [-5,5] ##CHANGABLE INTERVALL
    amount_dtp=100 ##CHANGABLE DTP AMOUNT
    x = np.linspace(xy_intervall[0],xy_intervall[1],amount_dtp)
    #x= np.empty(amount_dtp,dtype=float) ##CHANGABLE DATATYPE

    y = np.empty(amount_dtp,dtype=float) ##CHANGABLE DATATYPE
    for i,ele in enumerate(x):
        y[i]=math.cos(ele*math.pi/2) ##CHANGABLE FUNCTION
    print(y.size,x.size)
    time=timeit.timeit(lambda:main(x,y),number=1)
    plotsin(x)
    
if __name__=="__main__":
    test()
    
    

