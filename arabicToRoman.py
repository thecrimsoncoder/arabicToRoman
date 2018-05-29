import time


def title():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+    a r a b i c T o R o m a n . p y   +")
    print("+     Created By: Sean McElhare        +")
    print("+     github.com/thecrimsoncoder       +")
    print("++++++++++++++++++++++++++++++++++++++++")
def promptInput():
    arabicInput =  input("Please enter a number: ")
    if arabicInput.isnumeric():
        romanNumerals = decode(arabicInput)
        print("Roman Numerals Conversion: " + str(romanNumerals))
    else:
        print("Please enter something that actually makes sense!")
        time.sleep(2)
        promptInput()
def decode(input):

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
    romanString = ""
    input = int(input)
    for divisor in arabicRomanMapping.keys():
        print("Input: " + str(input))
        print("Divisor: " + str(divisor))
        quotient, remainder = divmod(input,divisor)
        print("Quotient: " + str(quotient))
        print("Remainder: " + str(remainder))
        romanString = romanString + str(arabicRomanMapping[divisor] * quotient)
        input = input - (divisor * quotient)

    return romanString
title()1993
promptInput()
