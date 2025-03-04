from PIL import Image
import numpy as np


def encrypt(i, o, k):
    try:
        image = Image.open(i)
        iarray = np.array(image)

        earray = (iarray + k) % 256

        eimage = Image.fromarray(earray.astype(np.uint8))
        eimage.save(o)
        print("Encrpted image saved as", o)
    except:
        print("***Error in opening or saving the image***")


def decrypt(i, o, k):
    try:
        eimage = Image.open(i)
        earray = np.array(eimage)

        darray = (earray - k) % 256

        dimage = Image.fromarray(darray.astype(np.uint8))
        dimage.save(o)
        print("Decrypted image saved as", o)
    except:
        print("***Error in opening or saving the image***")


k = 150
print("enter 0 to exit\nenter 1 for encryption \nenter 2 for decryption")
while True:
    c = int(input("enter your choice: "))
    if c == 1:
        i = input("enter the image name :")
        o = input("enter the image name to be saved with :")
        encrypt(i, o, k)
    elif c == 2:
        i = input("enter the image name :")
        o = input("enter the image name to be saved with :")
        decrypt(i, o, k)
    elif c == 0:
        break
    else:
        print("enter a valid number....")