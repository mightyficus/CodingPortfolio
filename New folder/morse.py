#morse.py
"""
Created by: Cooper Hopkin
2/23/2018
Program whose purpose is to blink an LED light
(connected to the raspberry pi by GPIO pins) in
morse translated from a user inputted string.
Psuedocode:
1. Ask for user input (as a string)
    a. Check for unsupported characters
2. Translate into morse
3. Output in dits and dahs to LED connected to
    GPIO pin 2
4. When done, press <Enter> without a string

Tests:
"HELLO WORLD STOP"
"TESTING TESTING 123 STOP"
"THIS IS CALL SIGN ABK PLEASE RESPOND STOP"

Morse Code translation chart curtesy of:
https://morsecode.scphillips.com/morse2.html

Possible future iterations:
1. Receive input from file
2. Punctuation
3. Prosigns
4. LED and Beeper
5. Q Codes
6. Non-english characters
"""

from gpiozero import LED, Buzzer
import time

def dit(led):
    led.on()
    time.sleep(.35)
    led.off()
    time.sleep(.15)

def dah(led):
    led.on()
    time.sleep(.7)
    led.off()
    time.sleep(.15)

def convertString(message, led):
    for s in message:
        if s == " ":
            time.sleep(.35)
        elif s == "A":
            dit(led)
            dah(led)
        elif s == "B":
            dah(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "C":
            dah(led)
            dit(led)
            dah(led)
            dit(led)
        elif s == "D":
            dah(led)
            dit(led)
            dit(led)
        elif s == "E":
            dit(led)
        elif s == "F":
            dit(led)
            dit(led)
            dah(led)
            dit(led)
        elif s == "G":
            dah(led)
            dah(led)
            dit(led)
        elif s == "H":
            dit(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "I":
            dit(led)
            dit(led)
        elif s == "J":
            dit(led)
            dah(led)
            dah(led)
            dah(led)
        elif s == "K":
            dah(led)
            dit(led)
            dah(led)
        elif s == "L":
            dit(led)
            dah(led)
            dit(led)
            dit(led)
        elif s == "M":
            dah(led)
            dah(led)
        elif s == "N":
            dah(led)
            dit(led)
        elif s == "O":
            dah(led)
            dah(led)
            dah(led)
        elif s == "P":
            dit(led)
            dah(led)
            dah(led)
            dit(led)
        elif s == "Q":
            dah(led)
            dah(led)
            dit(led)
            dah(led)
        elif s == "R":
            dit(led)
            dah(led)
            dit(led)
        elif s == "S":
            dit(led)
            dit(led)
            dit(led)
        elif s == "T":
            dah(led)
        elif s == "U":
            dit(led)
            dit(led)
            dah(led)
        elif s == "V":
            dit(led)
            dit(led)
            dit(led)
            dah(led)
        elif s == "W":
            dit(led)
            dah(led)
            dah(led)
        elif s == "X":
            dah(led)
            dit(led)
            dit(led)
            dah(led)
        elif s == "Y":
            dah(led)
            dit(led)
            dah(led)
            dah(led)
        elif s == "Z":
            dah(led)
            dah(led)
            dit(led)
            dit(led)
        elif s == "0":
            dah(led)
            dah(led)
            dah(led)
            dah(led)
            dah(led)
        elif s == "1":
            dit(led)
            dah(led)
            dah(led)
            dah(led)
            dah(led)
        elif s == "2":
            dit(led)
            dit(led)
            dah(led)
            dah(led)
            dah(led)
        elif s == "3":
            dit(led)
            dit(led)
            dit(led)
            dah(led)
            dah(led)
        elif s == "4":
            dit(led)
            dit(led)
            dit(led)
            dit(led)
            dah(led)
        elif s == "5":
            dit(led)
            dit(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "6":
            dah(led)
            dit(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "7":
            dah(led)
            dah(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "8":
            dah(led)
            dah(led)
            dah(led)
            dit(led)
            dit(led)
        elif s == "9":
            dah(led)
            dah(led)
            dah(led)
            dah(led)
            dit(led)
        elif s == ".":
            dit(led)
            dah(led)
            dit(led)
            dah(led)
            dit(led)
            dah(led)
        elif s == ",":
            dah(led)
            dah(led)
            dit(led)
            dit(led)
            dah(led)
            dah(led)
        elif s == ":":
            dah(led)
            dah(led)
            dah(led)
            dit(led)
            dit(led)
            dit(led)
        elif s == "?":
            dit(led)
            dit(led)
            dah(led)
            dah(led)
            dit(led)
            dit(led)
        elif s == "'":
            dit(led)
            dah(led)
            dah(led)
            dah(led)
            dah(led)
            dit(led)
        elif s == "-":
            dah(led)
            dit(led)
            dit(led)
            dit(led)
            dit(led)
            dah(led)
        elif s == "/":
            dah(led)
            dit(led)
            dit(led)
            dah(led)
            dit(led)
        elif s == "(" or s == ")":
            dah(led)
            dit(led)
            dah(led)
            dah(led)
            dit(led)
            dah(led)
        elif s == '"':
            dit(led)
            dah(led)
            dit(led)
            dit(led)
            dah(led)
            dit(led)
        elif s == "@":
            dit(led)
            dah(led)
            dah(led)
            dit(led)
            dah(led)
            dit(led)
        elif s == "=":
            dah(led)
            dit(led)
            dit(led)
            dit(led)
            dah(led)
        else:
            print("Character", s, "not currently supported!")
            
        
            
        
    

def main():
    led = LED(2)
    led.off()

    print("This program converts user input into morse code.")
    print("Please make sure to have the required Raspberry Pi")
    print("setup attached, with an LED interfaced to GPIO pin 2.\n")
    print("NOTICE: v0.0.1 currently only supports standard English")
    print("characters.")

    while True:
        message = str(input("Enter your message: "))
        convertString(message.upper(), led)
        cont = str(input("Enter 'yes' to continue, or 'no' to exit..."))
        if cont[0].lower == "y":
            continue
        else:
            break


main()
    

