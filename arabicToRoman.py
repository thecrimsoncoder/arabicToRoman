import time


def title():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+    a r a b i c T o R o m a n . p y   +")
    print("+     Created By: Sean McElhare        +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")
def decode():
    arabicInput =  input("Please enter a number: ")
    arabicRomanMapping = {
                                1000 : "M",
                                900 : "CM",
                                500 : "D",
                                400 : "CD",
                                100 : "C",
                                90 : "XC",
                                40 : "XL",
                                10 : "X",
                                9 : "IX",
                                5 : "V",
                                4 : "IV",
                                1 : "I"

                            }

    if arabicInput.isnumeric():


    else:
        print("Please enter something that acutally makes sense kthxbye")
        time.sleep(2)
        decode()

title()
decode()

