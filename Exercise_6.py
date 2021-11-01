# Write a program that receives an input from the terminal (using input()).
# The input needs to be an integer. The program will print on the terminal the difference between
# 24 and this input. If the input is greater than 24, then the program will compute the cube of the absolute
# value of the difference between 24 and the input.
# Example 1: input = 5, output = 19
# Example 2: input = 26, output = 8

x = int(input())

if x > 24:
    print(abs(24-x)**3)
else:
    print (24-x)
