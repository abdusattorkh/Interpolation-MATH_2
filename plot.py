import interpolation as pol
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import *

def update(para):
    print(para)

def plot_all(x,nev,lag,new,x_int):
    figure, axis = plt.subplots(4)
    
    axis[0].plot(x,nev.f(x,nev.coefs))
    axis[0].set_title("Neville-Interpolation")
    
    axis[1].plot(x,lag.interpolate(x))
    axis[1].set_title("Lagrange-Interpolation")
    
    axis[2].plot(x,new.evaluate(new.coefs,new.x_array,x))
    axis[2].set_title("Newton-Interpolation")
    
    
    axis[3].plot(x,np.sin(x))
    axis[3].set_title("Sinus-Kurve")
    plt.setp(axis,xlim=x_int,ylim=(-1.5,1.5))
    figure.tight_layout()
    
    plt.show()
    
def main():
    xy_intervall = [-2,2]
    amount_dtp=20 
    x = np.linspace(xy_intervall[0],xy_intervall[1],amount_dtp)
    y = np.empty(amount_dtp,dtype=float) 
    for i,ele in enumerate(x):
        y[i]=np.sin(ele)
    """ Resolution of Plot (last number)"""
    x_eval = np.linspace(xy_intervall[0],xy_intervall[1],2000)
    
    nev = pol.NevillePoly(x,y)
    new = pol.NewtonPolynom(x,y)
    lag = pol.LagrangePoly(x,y)
    plot_all(x_eval,nev,lag,new,xy_intervall)
    
if __name__ == "__main__":
    main()