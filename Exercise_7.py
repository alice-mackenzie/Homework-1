# Write a program that receives one input from the terminal (using input()).
# The input needs to be an integer. The program will compute the factorial of 
# this number and print it on the screen. If the number is negative the program will print 
# "Factorial does not exist for negative numbers". Remember that the factorial of 0 is 1.
# Example: input = 5, output = 5*4*3*2*1 = 120
import math

x = int(input())

if x<0:
    print("Factorial does not exist for negative numbers.")
else:
    print(math.factorial(x))