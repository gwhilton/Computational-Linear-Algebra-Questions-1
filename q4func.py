import numpy as np
from cla_utils import *
import matplotlib.pyplot as plt
from tabulate import tabulate

W = np.loadtxt('pressure.dat')

#W([50,0]) = 1  I computed this so I knew the index of the depth value=1 

m, n = W.shape
z = W[:,0] #depth vector, used said as x is our solution vector we defined in the question
Y = W[:,1] #pressure vector

def rock_solve(p):
    A = np.zeros((m, 2*p + 2)) #initialising A, B, b, d
    B = np.zeros((2, 2*p + 2))
    b = 1*Y
    d = np.array([[0],[5]])

    #inserting values into A
    for i in range(50):
        for j in range(p+1):
            A[i,j] = z[i]**j
    for i in range(50,100):
        for j in range(p+1,2*p+2):
            A[i,j] = z[i]**(j-(p+1))

    #inserting values into B
    for i in range(p+1):
        B[0,i] = 1
        B[1,i] = -1*i
    for i in range(p+1,2*p+2):
        B[0,i] = -1
        B[1,i] = i - (p+1)

    Ahat = np.concatenate((B, A), axis=0).T #vertical concatenation of B and A, then transpose.

    Q, R = householder_qr(Ahat)
    Rhat = R.T #tranpose of R so we can extra information encoded within

    C = Rhat[:2,:2]
    A1 = Rhat[2:,:2]
    A2 = Rhat[2:,2:]

    y1 = householder_ls(C,d) #solving Cy1=d for y1
    M = b - np.dot(A1, y1) 
    y2 = householder_ls(A2,M) #solving A2y2 = b - A1y1

    y = np.concatenate((y1, y2), axis=0) #vertically concatenating y1 and y2
    x = np.dot(Q, y) #obtaining x

    def p1(z): #polynomial for depth less than or equal to 1
        p1 = 0
        for a in range(p+1):
            p1 += x[a]*(z**a)
        return p1

    def p2(z): #polynomial for depth greater than 1
        p2 = 0
        for a in range(p+1):
            p2 += x[a+p+1]*(z**a)
        return p2

    xr1 = np.linspace(0,1,500,endpoint=True) #range of x for p1(z)
    xr2 = np.linspace(1, 1.98,500,endpoint=True) #range of x for p2(z)
    plt.plot(xr1, p1(xr1), color ='r') #plotting p1(z) and p2(z) with the original data points.
    plt.plot(xr2, p2(xr2), color ='b')
    plt.scatter(z[:50], Y[:50], color='r', marker='x')
    plt.scatter(z[50:], Y[50:], color='b', marker='x')
    plt.xlabel('Depth')
    plt.ylabel('Pressure')
    plt.title('Plot of interpolating polynomials and the data points, red=p1(x) blue=p2(x) p={}'.format(p))
    norm = np.linalg.norm(np.concatenate((p1(z[:50]),p2(z[50:])),axis=0) - Y) #norm of p(z) - Y to calculate 'deviation'
    cols = np.array([x[:p+1],x[p+1:]]).T
    print(tabulate(cols, headers=['p1(x) coefficients p={}'.format(p), 'p2(x) coefficients p={}'.format(p)],tablefmt='pretty'))
    print(tabulate([[norm]], headers=['Norm of the distance between p(x) and data points, p={}'.format(p)], tablefmt='pretty'))
    return p1, p2, x