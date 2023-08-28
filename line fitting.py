import numpy as np
import matplotlib.pyplot as plt


def LSFit_line(x,y):
  n=len(x)
  a=(n*sum(x*y)-sum(y)*sum(x))\
  /(n*sum(x**2)-(sum(x))**2)
  b=(sum(y)-a*sum(x))/n
  return a,b


x=np.array([1,2,3,4,5])
y=np.array([3.1,4.85,7.05,9.39,11.1])
a,b=LSFit_line(x,y)
y1=a*x+b
plt.plot(x,y,'bs',x,y1)
plt.text(2,10, r'$y='+'%5.3f'%a+'x+'+'%5.3f'%b+'$')
plt.show()
