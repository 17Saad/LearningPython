

x = input("What's x? ")
y = input("What's y? ")

#The following will concatenate strings
#z = x+y

#type convert strings to integers
z = int(x) + int(y)

print(z)


#To get rid of the variable z, we can do following

x = int(input("What's x? "))
y = int(input("What's y? "))
print(x+y)

#For numbers with decimel points
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x+y)
print(z)

#round(number[, ndigits])
#In Python documentation, anything within square brackets [] is optional

#The following adds a comma to number
print(f"{z:,}")

#Division
z = round(x / y, 2)
print(z)

#The following rounds to 2 digits using f-string
#print(f"{z:.2f}")






