
GreetType = input("Greeting: ").lower().strip()

if GreetType.startswith('h'):
    if GreetType.startswith('hello'):
        print("$0")
    else:
        print("$20")
else:
    print("$100")



