# Write a program that receives an input from the terminal (using input()).
# This input needs to be a string. If the string is "This is the right string." the program ends.
# Otherwise it keeps printing "Please provide the right string" until the string "This is the right string." 
# is provided.

isCorrectString = False
correctString = "This is the right string."

while isCorrectString == False:
    inputString = str(input())
    if inputString == correctString:
        isCorrectString = True
    else:
        print ("Please provide the right string:")
