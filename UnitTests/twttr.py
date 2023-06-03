def main():
    prep_In = input("Input: ")
    print(shorten(prep_In))


def shorten(word):

    newWord = ""
    i = -1
    while i < len(word)-1:
        i += 1
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u' \
        or word[i] == 'A' or word[i] == 'E' or word[i] == 'I' or word[i] == 'O' or word[i] == 'U':
            continue
        newWord = newWord + word[i]

    return newWord

if __name__ == "__main__":
    main()




