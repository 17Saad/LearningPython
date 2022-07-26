# Ask user for their name
name = input("What's your name? ")

#What if you add spaces in before and after in input?
#Remove white space from str
name = name.strip()

#capitalize user name (only capitalize the first name)
#name = name.capitalize()

#Capitalize user's name
name = name.title()

#We can strip and captalize in the same function
#name = name.strip().title()

#We can even shorten it further to 1 line of code: combine functions
#name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

print(f"hello, {first}")

#Say hello to user
print ("hello, ")
print(name)

#The following is one big argument
print ("hello " + name)

# Multiple arguments to print
print ("hello, ", name)

#docs.python.org
#learn to read the documentation

#The following is print function
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#Here end is used for removing the line, which is be default
print ("hello, ", end="")
print(name)

#Here we are changing the default behavior of sep
print("hello,",name, sep='???')


#positional parameters
#named parameters

#Quotes inside quotes
print("hello, \"friend\"")

#Special strings: f-string
print(f"hello, {name}")







"""
This is a comment
"""


