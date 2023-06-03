def main():
    GreetType = input("Greeting: ").lower().strip()
    print(value(GreetType))


def value(greeting):
    if greeting.startswith('h'):
        if greeting.startswith('hello'):
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()

