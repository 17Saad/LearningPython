def main():

    grocery()

def grocery():

    Groc = {}

    i = 0
    while True:
        try:
            value = input("")
            Groc[i] = value.upper()
            i = i+1

        except EOFError:
            #Groc[i] = value.upper()
            #i = i+1
            print("\n")
            sorted_values = sorted(Groc.values())
            i = 0
            while i < len(sorted_values):
                print(sorted_values.count(sorted_values[i]), sorted_values[i])
                if sorted_values.count(sorted_values[i]) > 1:
                    #pop all the occurrences of the item
                    temp_count = sorted_values.count(sorted_values[i])
                    j = 1
                    while j < temp_count:
                        sorted_values.pop(j)
                        j = j + 1

             #       sorted_values.pop(i)
                i += 1

            break

            #print(sorted_values[0])
'''
            i = 0
            while i < len(sorted_values):
                temp = sorted_values[i]
                counter = 0
                while counter < len(sorted_values):
                    if temp == sorted_values[counter]:
                        counter = counter + 1
                    else:
                        break
                print(counter, temp)
                i = i + 1

            break

        except KeyboardInterrupt:
            print("Keyboard Interrupt received, exiting")
            break
'''
main()


