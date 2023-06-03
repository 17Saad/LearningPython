def main():
    cokeFunc()

def cokeFunc():
    coins = 0; due = 50
    while(coins < 50):
        coin = int(input("Insert Coin: "))
        if coin==25 or coin==10 or coin==5:
            due = due - coin
            coins = coins + coin
            if due <= 0:
                break
            print("Amount Due: ", due)
        else:
            print("Amount Due: ", due)

    change = abs(due)
    print("Change Owed: ", change)
main()
