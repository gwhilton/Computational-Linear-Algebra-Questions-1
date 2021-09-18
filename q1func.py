import numpy as np
from cla_utils import *
import matplotlib.pyplot as plt
A = np.load('values.npy')

def one(): #defining function to implement Q1
    Q, R = GS_modified(A) #use modified for stability and speed

    m1, n1 = Q.shape
    m2, n2 = R.shape

    m = int(m1/2)

    #plotting heat maps of subsections of Q
    plt.imshow(Q[n1:2*n1,:], cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.xlabel('Column Number')
    plt.ylabel('Rows {} to {}'.format(n1, 2*n1))
    plt.title('Heat map of a subsection of Q')
    plt.show()
    plt.close()
    plt.imshow(Q[m:m+100,:], cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.xlabel('Column Number')
    plt.ylabel('Rows {} to {}'.format(m, m + 100))
    plt.title('Heat map of a subsection of Q')
    plt.show()
    plt.close()
    plt.imshow(Q[m1-100:,:], cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.xlabel('Column Number')
    plt.ylabel('Rows {} to the end'.format(m1-100))
    plt.title('Heat map of a subsection of Q')
    plt.show()
    plt.close()

    #plotting a heat map of R
    plt.imshow(R, cmap='viridis', interpolation='nearest')
    plt.xlabel('Rows')
    plt.ylabel('Columns')
    plt.title('Heat map of R')
    plt.colorbar()
    plt.show()
    return Q, R