import numpy as np
#define function
def f(x):
    return np.cos(x) - x * np.exp(x)
#Re-writing f(x)=0 to x = g(x)
def g(x):
    return np.cos(x) / np.exp(x)


#initializing basic parameters
x_old = -2  
x_new = g(x_old)
step = 0
condition = True
esp = 1e-5

# Implementing Fixed Point Iteration Method

while condition:
    x_new = g(x_old)
    
    x_old = x_new
    
    print(step,x_new,f(x_new))
    step = step + 1
    
    condition = abs(f(x_new)) > esp
    
print("root is :",x_new )
  
    
    