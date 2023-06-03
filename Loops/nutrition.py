def main():
    UserIn = input("Item: ")
    Cal = nutrition(UserIn)


def nutrition(inp):

    fruit_dict = {'Apple': 130,
                  'Avocado': 50,
                  'Banana': 110,
                  'Cantoloupe': 50,
                  'Grapefruit': 60,
                  'Grapes': 90,
                  'Honeydew Melon': 50,
                  'Kiwifruit': 90,
                  'Lemon': 15,
                  'Lime': 20,
                  'Nectarine': 60,
                  'Orange': 80,
                  'Peach': 60,
                  'Pear': 100,
                  'Pineapple': 50,
                  'Plums': 70,
                  'Strawberries': 50,
                  'Sweet Cherries': 100,
                  'Tangerine': 50,
                  'Watermelon': 80}

    #Converting dictionary key values to lowercase
    new_dict = dict((k.lower(), v)  for k, v in fruit_dict.items())

    if inp in new_dict:
        print("Calories: ", new_dict[inp])
    elif inp in fruit_dict:
        print("Calories: ", fruit_dict[inp])
    else:
        print("")

main()