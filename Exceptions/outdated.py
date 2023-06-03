def main():

    outdated()

def outdated():

    Months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            InDate = input("Date: ")

            if '/' in InDate:
                Month, Day, Year = InDate.split('/')
                if int(Month) > 12:
                    print("wrong format")
                    #prompt again and throw exception
                elif int(Day) > 31:
                    print("wrong format")
                    #prompt again and throw exception
                else:
                    print(f"{Year:04}-{int(Month):02}-{int(Day):02}")
                    break
            elif ',' in InDate:
                MonthDay, Year = InDate.split(',')
                Month, Day = MonthDay.split(' ')
                if Month not in Months:
                    print('wrong1 format')
                    #prompt again and throw exception
                elif int(Day) > 31:
                    print('wrong1 format')
                    #prompt again and throw exception
                else:
                    i = 0
                    while i < 12:
                        if Month == Months[i]:
                            Month = i+1
                        i = i + 1
                    print(f"{Year:04}-{int(Month):02}-{int(Day):02}")
                    break

        except EOFError:
            print("\nNo more input\n")
            break
        except KeyboardInterrupt:
            print("Keyboard Interrupt received, exiting")
            break



main()
