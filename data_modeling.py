#y=af(x)+bg(x)+ch(x)

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,7)
y=np.arange(2,8)

def f(x):
    return x+3
def g(x):
    return x**2
def h(x):
    return x                # M=A*Atranspose , MX=P


def data_model(f,g,h,x,y):
    P=np.zeros((3,1))
    M=np.zeros((3,3))
    for i in range(len(x)):
        A=np.mat([[f(x[i])],[g(x[i])],[h(x[i])]])
        M+=A*np.transpose(A)
        N=y[i]*A
        P+=N
    X=np.matmul(np.linalg.inv(M),P)
    a=X[0,0]           #X will contain values of constants a,b,c
    b=X[1,0]
    c=X[2,0]
    return a,b,c

a,b,c=data_model(f,g,h,x,y)


def linefit(x):
  return a*f(x)+b*g(x)+c*h(x)
  
plt.plot(x,linefit(x))
plt.show()
