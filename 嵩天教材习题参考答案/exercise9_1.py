import numpy as np
import matplotlib.pyplot as plt

def squareWave(x,n):
    f = np.zeros(( x.shape[0],))
    
    k = 1
    while k <= n:
        f = f + (8*np.sin((2*k-1)*x)/((2*k-1)*np.pi))
        k = k + 1
   
    return f
     
x = np.linspace(0.0,24.0,100)
y = squareWave(x, 20)

plt.plot(x,y)
