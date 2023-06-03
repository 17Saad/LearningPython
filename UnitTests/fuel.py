def main():

    fracIn = input("Fraction: ")
    convOut = convert(fracIn)
    output = gauge(convOut)
    print(output)

def convert(fracIn):
    while True:
        try:
            num, den = fracIn.split("/")
            new_num = int(num)
            new_den = int(den)

            Fuel = new_num/new_den

            if Fuel <= 1:
                 p = int(Fuel*100)
                 return p
            else:
                 fracIn = input("Fraction: ")
                 pass
        except (ValueError, ZeroDivisionError):
             raise

def gauge(Z):
     if Z <= 1:
          return "E"
     elif Z >= 99:
          return "F"
     else:
          return str(Z) + "%"

if __name__ == "__main__":
    main()