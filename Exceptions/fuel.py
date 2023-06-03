def main():

    fuel()

def fuel():
    while True:
        fracIn = input("Fraction: ")

        try:
            num, den = fracIn.split('/')
            num = int(num)
            den = int(den)
            percentFuel = num/den*100
        except ZeroDivisionError:
            print("ZeroDivisionError")
            continue
        except ValueError:
            print("ValueError")
            continue

        if (num > den) or (den == 0) or (not(isinstance(num, int))) or (not(isinstance(den, int))):
            continue
        elif percentFuel >= 99:
            print('F')
            break
        elif percentFuel <= 1:
            print('E')
            break
        else:
            print(str(round(percentFuel)) + '%')
            break

main()