import numpy as np

def func(x): 
    return 0.1972 - x * np.exp((-x**2)/2) 
  
def regulaFalsi( a , b): 
    if func(a) * func(b) >= 0: 
        print("You have not assumed right a and b") 
        return -1
      
     
    for i in range(100): 
        # Find the point that touches x axis 
        c = (  (  a*func(b) - b*func(a)  )/ 
             ( func(b) - func(a) ) )
        
        print(i,a,b,c)
        # Check if the above found point is root 
        if func(c) == 0: 
            break
        
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
        
    print("The value of root is : " , c) 
    
regulaFalsi(4,2)

