def main():
    CCase = input("camelCase: ")
    camel_to_snake(CCase)

def camel_to_snake(st):
        i = 0
        while i < len(st):
            if st[i].isupper():
                st = st.replace(st[i], "_" + st[i].lower())
            i += 1

        print("snake_case: ", st)

main()