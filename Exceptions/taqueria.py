def main():

    taqueria()

def taqueria():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    TotalCost = 0
    while True:
        try:
            Item = input("Item: ").title()
#            Item = Item.title()

#            if Item in menu:
#                print(True)
            TotalCost = TotalCost + menu[Item]
            #print("Total: $" + str(round(TotalCost,2)))
            print("Total: $%.2f" % TotalCost)

        except EOFError:
            print("\nNo more input\n")
            break
        except KeyError:
            print(f"{Item} is unknown")
        except KeyboardInterrupt:
            print("Keyboard Interrupt received, exiting")
            break

main()