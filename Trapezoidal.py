# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:54:56 2020

@author: hrushikesh.bhosale
"""

#import numpy as np
#import matplotlib.pyplot as plt

def trapz(f,a,b,N=50):

    h = (b - a)/N
    s= 0
    for i in range(1,N):
        s +=  h/2 * (f(a + i*h) + f(a + (i-1)*h))
        
    return s

#trapz(np.sin,0,np.pi/2,1000)
trapz(lambda x : 3*x**2,0,1,10000)

trapz(lambda x : x,0,1,100)

f = lambda x : 1/(1 + x**2)
trapz(f,0,5,100)








