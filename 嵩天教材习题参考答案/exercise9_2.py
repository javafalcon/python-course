# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:51:16 2018

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

def heart(x):
    y = ( np.power(x**2,1/3) + np.sqrt( np.power(x**4, 1/3) - 4* x**2 + 4))/2
    return y

x = np.linspace(-2,2, 100)
y = heart(x)
plt.plot(x,y)
