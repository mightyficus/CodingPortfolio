#caesarCipher.py
"""
Program meant to take an input and output the 26 different Ceasar
Cipher Solution.
Author: John Cooper Hopkin
10/17/26
"""

def caesarShift(inChr, places):
    newstr = ""
    text = inChr.lower().replace(' ', '')
    for char in text:
        x = ord(char)
        x = x - places
        if (x < 97):
            x = x + 26

        newstr = newstr + chr(x)

    return newstr
        
    #return ''.join(chr(ord(char) + places) )


def main():
    toCode = input("Enter the text to shift: ")
    wrdList = toCode.split(" ")
    for i in range(0, 27):
        for word in wrdList:
            print(caesarShift(word, i), end=" ")
        print()

if __name__ == "__main__":
    main()
