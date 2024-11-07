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
def type_test(x,a=False):
    if(a==False):
        try:
            float(x)
            try:
                return(int(x))
            except ValueError:
                return(float(x))
        except ValueError:
            return(False)
    else:
        try:
            return(int(x))
        except ValueError: 
            return(False)
print(type_test(input("please enter a int or float: ")))
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
    
def point_slope(m,b,a,an):
    y_val=[]
    m=type_test(m)

    b=type_test(b)

    a=type_test(a,True)

    an=type_test(an,True)
 
    if((m==False and m !=0) or (b==False and b!=0) or (a==False and a!=0) or (an==False and an!=0)):
        return False
    else:
        x=a
        while x <= an:
            val=(m*x+b)
            y_val.append(round(val, 2))
            x+=1
    return(y_val)

def user_pythag():
    while True:
        user= (input("Please enter a string(slope,intercept,lower_x,upper_x) or use exit to exit: ")).lower()
        if(user=="exit"):
            break
        if("," in user):
            user=user.split(",")
            m=user[0]
            b=user[1]
            a=user[2]
            an=user[3]
            user=point_slope(m,b,a,an)
        else:
            user==False
        print(user)
        if(user==False):
            print("The string entered did not meet criteria")
        else:
            print(f"The x values from {a} to {an} for the equation y={m}x+{b} are:")
            for val in user:
                print(val)


user_pythag()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def user_quad():
    while True:
        user= (input("Please enter a,b,c for quadratic formula or use exit to exit: ")).lower()
        if(user=="exit"):
            break
        if "," in user:
            user=user.split(",")
            print(user)
            a=user[0]
            b=user[1]
            c=user[2]
            ans=quad_form(a,b,c)
        if(user==False):
            print("The string entered did not meet criteria")
        else:
            print(f"The quadradic form of {a}, {b}, {c} is:")
            for val in ans:
                print(val)

def quad_form(a,b,c):
    vals=[]
    a=type_test(a)
    b=type_test(b)
    c=type_test(c)
    if (a==False) or (b==False and b!=0) or (c== False and c!=0):
        print("error")
        return(False)
    else:
        disc= ((b**2) - (4 * a * c))**.5
        if (isinstance(disc, complex)==False):
            print(disc)
            top= -b + disc
            full=top / (2 * a)
            vals.append(round(float(full),3))
            top= -b - disc
            full=top / (2 * a)
            vals.append(round(float(full),3))

        else:
            vals.append("null")
        return(vals)
    
user_quad()