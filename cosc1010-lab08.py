# Kaleb Moler
# UWYO COSC 1010
# 11/06/24
# Lab 08
# Lab Section:15
# Sources, people worked with, help given to:
# Jay Trujio, Jhett Carr



# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def Checker(string):
    dot=0
    letter=False
    for char in string:
        numb=False
        for num in range(0,10):
            #print(numb)
            if(char==str(num)):
                numb=True
                break
        if(numb==False):
            if(char=="."):
                dot=+1
            else:
                letter=True
            if(dot>1 or letter==True):
                return(False)
    if(dot==1):
        return(float(string))
    else:
        return(int(string))

print(Checker(input("str: ")))
print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def mb_test(mb):
    try:
        return(float(mb))
    except ValueError:
        return False
    
def a_test(a):
    try:
        return(int(a))
    except ValueError:
        return False
    
def point_slope(m,b,a,an):
    y_val=[]
    m=mb_test(m)
    b=mb_test(b)
    a=a_test(a)
    an=a_test(an)
    if(m==False or b==False or a==False or an==False):
        return False
    else:
        for x in range(a,an+1):
            val=(m*x+b)
            if isinstance(val, int):
                y_val.append(int(val))
            else:
                 y_val.append(round(val, 2))
    return(y_val)

  def user_input():
    user=input("Please enter a string(slope,intercept,lower x,upper x) or use exit to exit: ")
    while(user!="exit"):
        m=""
        b=""
        a=""
        an=""
        var=0
        y_val=[]
        for part in user:
            if(part==","):
                var+=1
            elif(var==0):
                m+=part
            elif(var==1):
                b+=part
            elif(var==2):
                a+=part
            else:
                an+=part
        user=point_slope(m,b,a,an)
        if(user=False):
            print("The string entered did not meet criteria")
        else:
            print(f"The x values from {a} to {an} for the equation y={m}x+{b} are:")
            for val in y_val:
                print(val)
        user=input("Please enter a string(slope,intercept,lower x,upper x) or use exit to exit: ")




print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
