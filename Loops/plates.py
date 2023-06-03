def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def containsNumber(AStr):
    for ch in AStr:
        if ch.isdigit():
            return True
    return False

def is_valid(s):
    slicedString = s[2:len(s)]
    if len(s) < 2 or len(s) > 6:
        return False
    elif not(s[0:2].isalpha()):
        return False
    elif '.' in s or ',' in s or ' ' in s:
        return False
    elif containsNumber(slicedString):
        if slicedString[len(slicedString)-1].isalpha():
            return False
        i = -1
        while i < len(slicedString)-1:
            i += 1
            if slicedString[i].isdigit():
                if slicedString[i] == '0':
                    break
                    return False
                elif slicedString[i].isdigit() and (slicedString[-1].isalpha() or slicedString[-2].isalpha()):
                    return False
                else:
                    return True

    else:
        return True


main()