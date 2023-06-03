def main():
    twttr()


def twttr():
    prep_In = input("Input: ")
#    prep_In = In.lower()

    i = -1
    while i < len(prep_In)-1:
        i += 1
        if prep_In[i] == 'a' or prep_In[i] == 'e' or prep_In[i] == 'i' or prep_In[i] == 'o' or prep_In[i] == 'u' \
        or prep_In[i] == 'A' or prep_In[i] == 'E' or prep_In[i] == 'I' or prep_In[i] == 'O' or prep_In[i] == 'U':
            continue
        print(prep_In[i], end="")

    print("\n")

main()



