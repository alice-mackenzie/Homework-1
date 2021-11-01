# Write a program that receives two inputs from the terminal (using input()).
# One input is an integer, the other is a string. If the length of the string is equal to the
# value of the integer, the program terminates. Otherwise the program will ask the user to provide
# another integer. The program will keep asking for a number, until the length of the string and the value
# of the integer match each other.
# Example: string = "hello", integer = 4, output --> "Please provide another number"

string = input("please provide a string: ")

x = len(string)
#print ("x is " + str(x))



same = False
while same == False:
    intager = int(input("please provide a number: "))
    if x != intager:
        #print ("x is " + str(x))
        same = False
        #intager = (int(input("Please provide another number: ")))
    if x == intager:
        same = True
        break
