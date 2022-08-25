
def main():
    Time = input("What time is it? ")
    newTime = convert(Time)

    if 7.00 <= newTime <= 8.00:
        print("breakfast time")
    elif 12.00 <= newTime <= 13.00:
        print("lunch time")
    elif 18.00 <= newTime <= 19.00:
        print("dinner time")
    else:
        print("")

def convert(time):
    hrs, min = time.split(":")
    newTime = float(hrs) + float(min)/60
    return newTime

main()