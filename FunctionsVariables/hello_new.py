def main():
    hello()
    name = input("What's your name? ")
    hello(name)


#The =world is the default value
def hello(to="world"):
    print("hello,", to)

main()

