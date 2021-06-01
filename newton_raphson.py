def func( x ): 
    f = (x+5)**2
    return f
  
def derivFunc( x ): 
    df =  2*(x+5)
    return df

# Function to find the root 
def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    i = 0
    x_old = x
    while True: 
        h = func(x_old)/derivFunc(x_old) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x_new = x_old - h 
        i = i + 1 
        
        print(i , x_new, h)
        
        
        if abs(x_new-x_old) < 0.0001:
            break
        
        x_old = x_new
      
    print("The value of the root is : ", 
                             "%.4f"% x_new) 
    
    
x0 = -20 # Initial values assumed 
newtonRaphson(x0) 