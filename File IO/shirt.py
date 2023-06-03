import sys
import os
from PIL import Image, ImageOps

def main():

        checkCLIArgs()
        #Open the Image
        try:
              imagefile = Image.open(sys.argv[1])
        except FileNotFoundError:
              sys.exit("Input does not exist")
        #Open shirt
        shirtfile = Image.open("shirt.png")
        #Get the size of the shirt
        size = shirtfile.size
        #Resize muppet image to fit shirt
        muppet = ImageOps.fit(imagefile, size)
        #Paste shirt in muppet
        muppet.paste(shirtfile, shirtfile)
        #Create output image
        muppet.save(sys.argv[2])

def checkCLIArgs():

    #Check how many elements in the command line
    if len(sys.argv) < 3:
           sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
           sys.exit("Too many command-line arguments")
    file1 = os.path.splitext(sys.argv[1])
    file2 = os.path.splitext(sys.argv[2])
    print(file1)
    print(file2)

    #Check if it is an image file
    if check_extension(file1[1]) == False:
           sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
           sys.exit("Invalid output")
    #Check if extension of both files are the same
    if file1[1].lower() != file2[1].lower():
           sys.exit("Input and output have different extensions")

def check_extension(file):
       if file in [".jpg", ".jepg", ".png"]:
              return True
       return False

if __name__ == "__main__":
        main()