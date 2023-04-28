import timeit
import interpolation as pol
import matplotlib.pyplot as plt
import random
import numpy as np


def plot_error(e_new,e_nev,e_lag,dtp_p,xy_intervall):
    
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        }
    all_error = [e_new,e_nev,e_lag]
    labels = ["Newton - ","Neville - ","Lagrange - "]
    amount_eval = 2000
    x_eval = np.linspace(xy_intervall[0],xy_intervall[1],amount_eval)
    fig, axs = plt.subplots(3, 3)
    for it1,ele in enumerate(dtp_p):
        for it2 in range(len(dtp_p)):
            x = np.linspace(xy_intervall[0],xy_intervall[1],dtp_p[it2])
            y = [0]*len(x)
            axs[it1][it2].plot(x_eval,all_error[it1][it2])
            axs[it1][it2].set_title(labels[it1]+str(dtp_p[it2]),y=-0.3,fontdict=font)
            axs[it1][it2].scatter(x,y,s=9,c="darkred")
    fig.tight_layout()
    plt.show()
    
def test():
    plt.figure(1)
    
    " Interval for x values "
    xy_intervall = [-10,10] 
    
    " Number of Datapoints "
    dtp_p = [5,10,25] 
    
    
    t_new = [0]*len(dtp_p) 
    t_nev = [0]*len(dtp_p)
    t_lag = [0]*len(dtp_p)
    
    e_new = [0]*len(dtp_p) 
    e_nev = [0]*len(dtp_p)
    e_lag = [0]*len(dtp_p)
    
    
    """ We overwrite the template for the timeit function so we can get the time it took and the result of the function call (get return value retval)"""
    timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

    amount_eval = 2000
    x_eval = np.linspace(xy_intervall[0],xy_intervall[1],amount_eval)
    y_eval = np.empty(amount_eval,dtype=float)
    
    for i,ele in enumerate(x_eval):
            y_eval[i]=np.sin(ele)
    for l,amount_dtp in enumerate(dtp_p):
        x = np.linspace(xy_intervall[0],xy_intervall[1],amount_dtp)
        
        y = np.empty(amount_dtp,dtype=float)
        for i,ele in enumerate(x):
            y[i]=np.sin(ele)
        """ Call timeit function for corresponding interpolation, "number" only changes amount of times called (not recommended), + get results for error calculation"""
        t_new[l],result_new = timeit.timeit(lambda: timed_test_newton(x,y,x_eval),number=1)
        t_nev[l],result_nev = timeit.timeit(lambda: timed_test_neville(x,y,x_eval),number=1)
        t_lag[l],result_lag = timeit.timeit(lambda: timed_test_lagrange(x,y,x_eval),number=1)
        
        " Calculate absolute error for each interpolation"
        
        e_nev[l] = np.absolute(y_eval-result_nev)
        e_lag[l] = np.absolute(y_eval-result_lag)
        e_new[l] = np.absolute(y_eval-result_new)
        
        
    
    plt.plot(dtp_p,t_new,color="r",label="Newton")
    plt.plot(dtp_p,t_nev,color="g",label="Neville")
    plt.plot(dtp_p,t_lag,color="b",label="Lagrange")
    plt.legend()
    plot_error(e_new,e_nev,e_lag,dtp_p,xy_intervall)
    
    
    
def timed_test_lagrange(x,y,x_eval):
    polynom = pol.LagrangePoly(x,y)
    y= polynom.interpolate(x_eval)
    return y
    
def timed_test_neville(x,y,x_eval):
    polynom = pol.NevillePoly(x,y)
    y = polynom.f(x_eval,polynom.coefs)
    return y
    
def timed_test_newton(x,y,x_eval):
    polynom = pol.NewtonPolynom(x,y)
    y = polynom.evaluate(polynom.coefs,polynom.x_array,x_eval)
    return y

if __name__=="__main__":
    test()
    
    

