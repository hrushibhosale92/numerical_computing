import numpy as np

#define the funtion 
def func(x): 
    return (x-5)*(x+3)

#initialise the guess
left_guess = 11
right_guess = 0

# check initial guess is valid or not 
if (func(right_guess)*func(left_guess)>= 0):
    print("Initial guess is not correct ")
else:    
    while (abs(left_guess-right_guess)>= 1e-5):
        #find the midpoint
        midpoint = (left_guess+right_guess)/2
        #Check if middle point is root 
        if (func(midpoint) == 0):
            break
        #Decide the interval where the root lies to repeat the steps
        if (func(midpoint)*func(left_guess)<0):
            right_guess = midpoint
        else:
            left_guess = midpoint
        print(left_guess,right_guess,midpoint)
    
print('the root of the equation is ',midpoint)
        
    