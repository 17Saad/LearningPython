
Expression = input("Expression: ")

x, y, z = Expression.split(" ")

match y:
    case "+":
        print(float(x)+float(z))
    case "-":
        print(float(x)-float(z))
    case "*":
        print(float(x)*float(z))
    case "/":
        print(float(x)/float(z))
