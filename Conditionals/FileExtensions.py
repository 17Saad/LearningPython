
FileName = input("File Name: ").lower().strip()

if FileName.endswith('.jpg') or FileName.endswith('.jpeg'):
    print("image/jpeg")
elif FileName.endswith('.png'):
    print("image/png")
elif FileName.endswith('.gif'):
    print("image/gif")
elif FileName.endswith('.pdf'):
    print("application/pdf")
elif FileName.endswith('.txt'):
    print("text/plain")
elif FileName.endswith('.zip'):
    print("application/zip")
else:
    print("application/octet-stream")


