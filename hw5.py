# File: homework5.py
# Author: Mitchell Dahmer
# Date: 10//17
# Section: 503
# Email: mtdahmer@tamu.edu
# Description: A program to take base 10 integers from the user and convert them into a different base of the 
# users choosing, either base 2, base 8, or base 16.


import math
#function to convert base 10 number to base 16
def hexidecimalconverter(userinteger , base):
    userinteger = int(userinteger) #changes userinput to integer to facilitate math commands
    numberlist = list() #creates list for the new number
    while userinteger > 0 : #starts a loop for the math and append process until the user integer cannot be divided anymore
        digit = userinteger % base #finds the remainder of the user integer
        if (digit == 10): #lines 17 - 28 find when the remainder is over 10 and appends the list with the corresponding letter
            numberlist.append('A')
        elif (digit == 11):
            numberlist.append('B') 
        elif (digit == 12):
            numberlist.append('C') 
        elif (digit == 13):
            numberlist.append('D') 
        elif (digit == 14):
            numberlist.append('E') 
        elif (digit == 15):
            numberlist.append('F')  
        else:
            numberlist.append(digit) #appends the list with any number under 9
        userinteger = userinteger // base #finds the new number to be divided by the base 
    numberlist.reverse()    #flips the list
    string = ''.join(str(e) for e in numberlist) #removes the brackets and commas from the list
    print(string) #prints the new number in base 16
def binaryandoctalconverter(userinteger , base): #converts the user integer to base 2 or base 8
    userinteger = int(userinteger) #changes userinput to integer to facilitate math commands
    numberlist = list() #creates list for the new number
    while userinteger > 0 : #starts a loop for the math and append process until the user integer cannot be divided anymore
        digit = userinteger % base #finds the remainder of the user integer
        numberlist.append(digit) #appends the list with the digit
        userinteger = userinteger // base #finds the new number to be divided by the base 
    numberlist.reverse() #flips the list
    string = ''.join(str(e) for e in numberlist) #removes the brackets and commas from the list
    print(string) #prints the new number in base 2or base 8
def main():
    flagmain = True #flag for the main loop
    flagchoice = True #flag for the choice loop
    flaginteger = True #flag for the integer determination loop
    userinteger = ''
    print('This program will convert a base 10 number into another base')
    while (flagmain == True): #begins programs loop
        while (flaginteger == True): #starts loop for integer verification
            userinteger = input('Enter an unsigned integer: ')  #takes integer from the user
            if (userinteger.isdigit() == True): #checks if input is an integer and closes the loop if it is
                flaginteger = False
            elif (userinteger.isalpha() == True): #checks if the input is a string
                userinteger=userinteger.lower() #sets string the lower case for easier verification
                if (userinteger == 'stop'): #checks if the string user entered is stop and ceases the program if it is
                    print('Thank for using this program')
                    flaginteger = False
                    flagmain = False 
                    flagchoice = False
                else:
                    print('invalid') #tells user if string entered is anything but 'stop'
            else:
                print('Invalid') #tells user if input is neither string nore integer
        while (flagchoice == True): #starts loop for the choice of base
            choice = input('B for binary, O for octal, H for hexadecimal: ') #takes one character input for choice of base
            choice = choice.lower() #sets input lower case for easier verification
            if (choice == 'b'): #checks if choice is b and runs the binary and octal converter with base 2
                base = 2
                binaryandoctalconverter(userinteger , base) #calls binary and octal converter
                flagchoice = False #stops loop after converter is complete
            elif (choice == 'o'): #checks if choice is o and runs the binary and octal converter with base 8
                base = 8
                binaryandoctalconverter(userinteger , base) #calls binary and octal converter
                flagchoice = False #stops loop after converter is complete
            elif (choice == 'h'): #checks if choice is h and runs the hexidecimal converter with base 16
                base = 16
                hexidecimalconverter(userinteger , base) #calls hexidecimal converter 
                flagchoice = False #stops loop after converter is complete
            else:
                print('Invalid choice') #tells user if choice was not b,o, or h                   
main()