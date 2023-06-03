import sys

def main():

    checkCLIarguments()

    try:
         with open(sys.argv[1], "r") as file:
            counter = 0
            for line in file:
                if checkLine(line) == False:
                    counter += 1
            print(counter)

    except FileNotFoundError:
        sys.exit("File does not exist")

def checkLine(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

def checkCLIarguments():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

if __name__ == "__main__":
    main()