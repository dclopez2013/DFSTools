import os
import hashlib
import sys
from functools import partial




def hashItOut(file):
    hashObj = hashlib.md5()

    done= False;
    with open(file, 'rb') as file:

        while not done:
            block = file.read(1024)
            if block:
                hashObj.update(block)
            else:
                hashValue = hashObj.hexdigest().upper()
                done = True
    return hashValue


def main():
    # get file to hash and verifies it exists
    inputFile = input("Enter the path and file you wish to hash")

    # hash type MD5
    hashType = None


    hashValueFinal = None
    done = False

    inputFile = inputFile.lstrip().strip()

    hashValueFinal = hashItOut(inputFile)

    print("File >> ", inputFile, " > hash value: ", hashValueFinal)

    print("Creating image file")

    outputFile = input("Enter the name of the ouput file: ")

    print("writing bytes to new file")
    # with open(inputFile, "rb") as f1, open (outputFile, "wb") as f2:
    #
    #     size= f1.__sizeof__()
    #     print("Bytes in inputfile >> ", size)
    #
    #     bytesLeft = size
    #     print("Both files opened in binary form")
    #     for _bytes in iter(partial(f1.read, 1024), ''):
    #
    #         #print("Bytes Left >> ",bytesLeft)
    #         print("copying bytes")
    #         f2.write(_bytes)
    #         print(f2.__sizeof__())
    #        # bytesLeft -= 1024
    #     f2.close()
    with open(inputFile, "rb") as f1:
        with open(outputFile, "wb") as f2:
            while True:
                b = f1.read(1024)
                if b:
                    f2.write(b)
                else:
                    break

    f1.close()
    f2.close()
    secondHash = hashItOut(outputFile)

    print("First file >> ",inputFile, " MD5 >> ",hashValueFinal)
    print("Second file >> ",outputFile," MD5 >> ",secondHash)

    if hashValueFinal == secondHash:
        print("Hash values match")

    else:
        print("Hash values dont match")

if __name__ == '__main__':
    main()