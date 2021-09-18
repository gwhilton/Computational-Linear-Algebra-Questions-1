import numpy as np
from cla_utils import *
import matplotlib.pyplot as plt
from tabulate import tabulate

x = np.arange(-1,1.1,0.2)
f = 0.0*x
f[3:6] = 1

def Qandb(m): #function with creates Q and b depedent on m
    Q = np.zeros((11,m+1)) #initialises Q based on m
    b = 1*f #initialise b
    #inserting x values into Q
    for i in range(11):
        for j in range(m+1):
            Q[i,j] = (x[i])**j
    return Q, b


#This function creates and plots the polynomial p (an approximation of F(x)), between 's' and 'e' which has degree m.
def poly_solve(m,s,e): 
    Q = Qandb(m)[0] #uses our prior defined function to create Q and b for solving Qy=b as explained in 2b
    b = Qandb(m)[1]
    y = householder_ls(Q,b) #performs least squares to give the polynomial coefficients a0, a1, ..., a10
    #create poly
    def p(z):
        p = 0
        m = len(y)
        for a in range(m):
            p += y[a]*(z**a)
        return p

    xrange = np.linspace(s,e,500,endpoint=True) #generating our x coordinates
    plt.plot(xrange, p(xrange)) #plotting
    return y, p, plt #returns the vector of coefficients, the polynomial and the plot


def twoc(m): #a function for 2(c) which plots our graph and adds the data points from the f vector.
    A = poly_solve(m,-1,1)
    plt.scatter(x, f, color='r', marker='x') #data points
    plt.xlabel('x')
    plt.ylabel('p(x)')
    plt.title('Plot of p(x) with the data points overlayed')
    cols = np.array([A[0]]).T
    print(tabulate(cols, headers=['p(x) coefficients'],tablefmt='pretty'))
    plt.show()
    return


#Below is a function which perturbs 'j' of the f values by 'dx' and returns a vector of the new coefficients.
def coeffperturbed(j, dx, m):
    fp = 1*f #creates a copy of the original f
    for i in range(j): #chooses first 'j' coefficients and perturbs them.
        fp[i] = fp[i] - dx
    bp = 1*fp
    Q = Qandb(m)[0]
    x = householder_ls(Q,bp) #peforms least squares on the new data sets to give the polynomials coefficients.
    return x

#The function below implements poly_solve but it also does the same for the perturbed polynomial and plots the
#perturbed and normal polynomial on the same graph.
def perturbed_poly_solve(j,dx,m,s,e): 
    yp = coeffperturbed(j,dx,m)
    Q = Qandb(m)[0]
    b = Qandb(m)[1]
    y = householder_ls(Q,b)
    def pp(z):
        pp = 0
        m = len(yp)
        for a in range(m):
            pp += yp[a]*(z**a)
        return pp
    def p(z): #recreating the polynomial is very time inexpensive and improves clarity so I included it again
        p = 0
        m = len(y)
        for a in range(m):
            p += y[a]*(z**a)
        return p
    xrange = np.linspace(s,e,500,endpoint=True) #x coordinates
    plt.plot(xrange, p(xrange), color='darkviolet')
    plt.plot(xrange, pp(xrange), color='deepskyblue')
    return yp, pp, y, p, plt #returns peturbed coefficients and polynomial as well as the original.


def twod(j ,dx, m, s, e): #function to implement question 2(d)
    A = perturbed_poly_solve(j, dx, m, s, e)
    plt.xlabel('x')
    plt.ylabel('p(x) (purple) and p(x) perturbed (blue)')
    plt.title('Plots of p(x) and perturbed p(x), j={} dx={} m={}'.format(j, dx, m))
    cols = np.array([A[2], A[0]]).T
    normdiff = np.linalg.norm(A[2] - A[0]) #A[0] = yp, A[2] = y
    #print the norm of the difference between the vector of coefficients to provide a comparison
    print(tabulate(cols, headers=['p(x) coefficients', 'Perturbed p(x) coefficients, m={}, j={}, dx={}'.format(m,j,dx)],tablefmt='pretty'))
    print(tabulate([[normdiff]], headers=['Norm of the distance between coefficients, m={}, j={}, dx={}'.format(m,j,dx)], tablefmt='pretty'))
    plt.show()
    return


def twoe(): #function to plot m=7 and m=10 as well as print both vectors of coefficients.
    seven = poly_solve(7, -1, 1) 
    plt.scatter(x, f,c='darkviolet', marker='x')
    ten = poly_solve(10, -1, 1)
    plt.xlabel('x')
    plt.ylabel('p(x), deg=10 (orange), deg=7 (blue)')
    plt.title('Plot of p(x) (deg=10) and p(x) (deg=7)')
    print(tabulate(np.array([[seven[0]]]), headers=['p(x) coefficients, m=7'],tablefmt='pretty'))
    print(tabulate(np.array([[ten[0]]]), headers=['p(x) coefficients, m=10'],tablefmt='pretty'))
    plt.show()
    return 


def twof(j, dx, m, s, e): #function to implement question 2(f)
    A = perturbed_poly_solve(j, dx, m, s, e)
    plt.xlabel('x')
    plt.ylabel('p(x) (purple) and p(x) perturbed (blue)')
    plt.title('Plots of p(x) and perturbed p(x), j={} dx={} m={}'.format(j, dx, m))
    cols = np.array([A[2], A[0]]).T
    normdiff = np.linalg.norm(A[2] - A[0])
    #print the norm of the difference between the vector of coefficients to provide a comparison
    print(tabulate(cols, headers=['p(x) coefficients', 'Perturbed p(x) coefficients, m={}, j={}, dx={}'.format(m,j,dx)],tablefmt='pretty'))
    print(tabulate([[normdiff]], headers=['Norm of the distance between coefficients'], tablefmt='pretty'))
    plt.show()
    return