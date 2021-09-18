import numpy as np 
from cla_utils import *
import matplotlib.pyplot as plt

def V(M,p): #vandermonde matrix construction, only discovered np.vander a long time after implementing so choose to keep mine as the functions still run quikcly.
    x = np.zeros((2*M,p+1))
    for i in range(2*M):
        for j in range(p+1):
            x[i,j] = (((i-M)+(1/2))/M)**j
    return x


def householder_plot_5(M): #function which plots the columns of Q for my householder QR.
    v = V(M,5) #construct the Vandermonde matrix fixing P=5
    Q, R = householder_qr(v)
    m1,n1 = Q.shape
    m2, n2 = R.shape
    xrange = range(0,m1) #range of x values
    for i in range(n2):
        plt.plot(xrange, Q[:,i]) #plotting the columns
    plt.title('Plot of the columns of Q using my Householder function, M={} p=5'.format(M))
    plt.xlabel('x')
    plt.ylabel('Column values of Q')
    plt.show()
    plt.close()
    return


def HH_QR_plot(M,p): #plot of the final 5 columns of the reduced Q matrix from Householder, can vary both M and p
    v = V(M,p) #constructing the Vandermonde matrix
    Q, R = householder_qr(v)
    m1,n1 = Q.shape
    m2,n2 = R.shape
    Q = Q[:,:n2] #obtained reduced Q
    xrange = np.linspace(-1,1,m1)
    for i in range(n2-6,n2):
        plt.plot(xrange,Q[:,i]) #plotting final 5 columns
    plt.title('Plot of the final 5 columns of Q (reduced) using Householder Reflectors, M={}, p={}'.format(M, p))
    plt.xlabel('x')
    plt.ylabel('Column values of Q')
    plt.show()
    plt.close()
    return


def GSM_QR_plot(M,p): #plot of the final 5 columns of the Q matrix obtained using modified Gram Schmidt
    v = V(M,p) #constructing the Vandermonde matrix
    Q, R = GS_modified(v)
    m,n = Q.shape
    xrange = np.linspace(-1,1,m)
    for i in range(n-6,n):
        plt.plot(xrange,Q[:,i]) #plotting final 5 columns
    plt.title('Plot of the final 5 columns of Q using Modified Gram Schmidt, M={}, p={}'.format(M, p))
    plt.xlabel('x')
    plt.ylabel('Column values of Q')
    plt.show()
    plt.close()
    return


def GSC_QR_plot(M,p): #plot of the final 5 columns of the Q matrix obtained using classical Gram Schmidt
    v = V(M,p) #constructing the Vandermonde matrix
    Q, R = GS_classical(v)
    m, n = Q.shape
    xrange = np.linspace(-1,1,m)
    for i in range(n-6,n):
        plt.plot(xrange,Q[:,i]) #plotting final 5 columns
    plt.title('Plot of the final 5 columns of Q using Classical Gram Schmidt, M={}, p={}'.format(M, p))
    plt.xlabel('x')
    plt.ylabel('Column values of Q')
    plt.show()
    plt.close()
    return