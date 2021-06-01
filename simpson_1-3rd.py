# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:34:27 2020

@author: hrushikesh.bhosale
"""


def f(x):
    return 1/(1 + x**2)

# Implementing Simpson's 1/3 
def simpson13(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    s = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            s = s + 2 * f(k)
        else:
            s = s + 4 * f(k)
    
    # Finding final integration value
    s = s * h/3
    return s

    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )


