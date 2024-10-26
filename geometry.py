#creating our own module
def circleArea():  #def stands for define it is keyword
       radius =float(input("enter a radius"))
       area=3.14*radius*radius
       print("area of circle = %.2f" %area)

#call the function
#circleArea()


def RectangleArea(length,breadth):
      
       area=length*breadth
       print("area of rectanlge =%.2f"%area)

 
#functio for trinagle
def  TriangleArea():
       
       base=int(input("enter the base"))
       heigth=int(input("enter the heigth"))
       area=0.5*base*heigth
      # print(" area will be =%.2f"%area)
       return area


# ABstract function
def Rohmbus():
       pass

#p>>>5
def local_scope_example():
       x=10    #local variable
       print(f" inside function ,x={x}")
local_scope_example()
print()  # this will raise a numerror bcz is not define outside the function
   


#p>>>7
x=10
def example_function():
       print(f"inside function,x={x}")
example_function()
print(f"outside fuct")   



#p>>8
y=20 #globl variable
print(f"intitally value of y={y}")
def modify_global_variable():
       global y
       y=30  #modify the global variable 
       print(f"inside function ,y={y}")
modify_global_variable()
print(f"outside function y={y}")


# consider list:-
# sampleno=[24,67,36,20,56,81,49,39,25]
# implement a function so that whole list can be passed as a parameter
# and we can calculat the sq.root of all these nos


# import math
# def sqroot(sampleno):
#        for  num in sampleno: 
#        sampleno=[24,67,36,20,56,81,49,39,25]
import math

def calculate_square_roots(numbers):
    # Calculate square root for each number in the list
    square_roots = [math.sqrt(num) for num in numbers]
    return square_roots

# List of numbers
sampleno = [24, 67, 36, 20, 56, 81, 49, 39, 25]

# Call the function and print the result
square_roots = calculate_square_roots(sampleno)
print("Square roots: " %square_roots)



#use of lambda
import math
sampleno=[24,67,36,20,56,81,49,39,25]

mylambda =lambda x:math.sqrt(x)
result=map(mylambda,sampleno)
print(result)


country_name="INDIA"
myit=iter(country_name)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))