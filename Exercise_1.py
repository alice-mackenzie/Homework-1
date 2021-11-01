# Write a program that receives an input from the terminal (using input()).
# This input needs to be an integer. Assign it to a variable named "n". The program will 
# compute the product n*nn*nnn and print it on the screen.
# example: n = 5 output = 5*55*555 = 152625

#n = int(input())

#output = (n*n*(11)*n*(111))

#print(output)

n = input()
nn = int(n*2)
nnn = int(n*3)
n = int(n)

print(n*nn*nnn)

#print(n)
#print(nn)
#print(nnn)