# File: homework6.py
# Author: Mitchell Dahmer
# Date: 10/17/17
# Section: 503
# Email: mtdahmer@tamu.edu
# Description: This program will take a number given in hexidecimal, binary or octal and convert it into decimal form based on the choice of the user. 
# It will then print the sonversion and when the program is stopped, it will print a summary for the user


import math
#this function verifies that verifies the users input to make sure its binary
#input : base 2; integer given by user
#output : boolean
def isBase2(base2):
    flagBase2 = True
    if (base2.isdigit()): #verifies input is digit to make sure correct format is used
        newList = list(base2) #converts input to list
        newList.sort() #sorts list into numerical order
        newIndex = int(newList[-1]) #makes whatever the now highest number is an integer for easier verification
        while (flagBase2 == True): #loop for determining if the last digit is less higher than one, meaning it is wrong
            if ( newIndex > 1):
                print('Invalid choice')
                return False
            else:
                flagBase2 = False
                return True
    else:
        return False
    
#exact same purpose and techniques as previous function except for inputs for octal  
def isBase8(base8):
    flagBase8 = True
    if (base8.isdigit()):
        newList = list(base8)
        newList.sort()
        newIndex = int(newList[-1])
        while (flagBase8 == True):
            if ( newIndex > 8):
                return False
            else:    
                flagBase8 = False
                return True
    else:
        return False
    
#verifies that the input for the hexiedecimal conversion is in the proper format
def isBase16(base16):
    base16Lower = base16.lower() #sets the input to lower case to make verification of the letter easier
    hexDigits = set("0123456789abcdef") #creates a set of characters to check for in the input
    for char in base16Lower: #checks the input for the predetermined characters
        if not (char in hexDigits):
            return False
    return True

#converts a binary input to base ten 
#input: user input of binary
#output: newly converted base ten number
def base2TO10(base2):
    newList = list(base2) #changes input to a list
    listCount = len(newList) #counts the number of items in the new list
    listIndex = 0 
    powerof2 = listCount - 1
    newSum = 0
    for i in range (listCount): #starts a loop for conversion
        binaryNumber = (int(newList[listIndex]))*(pow(2 , powerof2)) #multiplies the elements of the list one by one by descending exponential two
        binaryNumber = int(binaryNumber)
        newSum = newSum + binaryNumber #adds previously found number to the total
        listIndex = listIndex + 1 #two lines that change the outcome of the next loop by increasing the index of the element changed and decreasing the exponential on the 2
        powerof2 = powerof2 - 1
    return newSum #returns converted number

#exact same purpose and techniques as the previous function but for octal
def base8TO10(base8):
    newList = list(base8)
    listCount = len(newList)
    listIndex = 0
    powerof8 = listCount - 1
    newSum = 0
    for i in range (listCount):
        octalNumber = (int(newList[listIndex]))*(pow(8 , powerof8))
        octalNumber = int(octalNumber)
        newSum = newSum + octalNumber
        listIndex = listIndex + 1
        powerof8 = powerof8 - 1
    return newSum 

#same purpose and technique as the last two functions except convertes hexidecimal and defines any instance of letters into their corresponding number in base 10
def base16TO10(base16):
    base16 = base16.lower()
    newList = list(base16)
    for n,i in enumerate(newList):
        if (i =='a'):
            newList[n]=10
        elif (i =='b'):
            newList[n]=11
        elif (i =='c'):
            newList[n]=12
        elif (i =='d'):
            newList[n]=13
        elif (i =='e'):
            newList[n]=14
        elif (i =='f'):
            newList[n]=15 
    listCount = len(newList)
    listIndex = 0
    powerof16 = listCount - 1
    newSum = 0
    for i in range (listCount):
        hexidecimalNumber = (int(newList[listIndex]))*(pow(16 , powerof16))
        binaryNumber = int(hexidecimalNumber)
        newSum = newSum + hexidecimalNumber
        listIndex = listIndex + 1
        powerof16 = powerof16 - 1
    return newSum 

#calls print instructions 
def menu():
    
    print('Enter 2 for base 2')
    print('Enter 8 for base 8')
    print('Enter 16 for base 16')   

#prints summary for when the program is stopped    
def summary(list2, list8, list16):
    print('Summary')
    print('---------------')
    list2 = ''.join(str(e) for e in list2)
    print(list2)
    list8 = ''.join(str(e) for e in list8)
    print(list8)
    list16 = ''.join(str(e) for e in list16)
    print(list16) 
    print('End of program')    

def main():
    newSum = 0
    flagmain = True
    list2 = list()
    list8 = list()
    list16 = list()
    print('This program will convert a base 2, base 8, or base 16 number into base 10')
    while (flagmain == True): #starts main loop
        menu() #calls menu function
        choice = input('Enter 0 to stop: ')
        if (choice == '2'): #starts loop for if user chooses binary
            choice2flag = True
            while (choice2flag == True): #loop for choice 2
                base2 = input('Enter a base 2 number: ') 
                binaryVerification = isBase2(base2) #calls function for verification 
                if (binaryVerification): #starts conversion if number verified
                    newSum = base2TO10(base2) #calls converter function
                    print('Base 2 number: ' , base2 , 'is base 10 number: ', newSum)
                    list2.extend(['Base2 number: ', base2,  ' ------> ', newSum, '\n']) #appends a list with both inputted number and conversion for later summary
                    choice2flag = False
        elif (choice == '8'): #same as previous iteration of if loop but for octal
            choice8flag = True
            while (choice8flag == True):
                base8 = input('Enter a base 8 number: ')
                octalVerification = isBase8(base8)
                if (octalVerification):
                    newSum = base8TO10(base8)
                    print('Base 8 number: ' , base8 , 'is base 10 number: ', newSum)
                    list8.extend(['Base 8 number: ', base8,  ' ------> ', newSum, '\n'])
                    choice8flag = False
        elif (choice == '16'): #same as previous two iteration but for hexidecimal
            choice16flag = True
            while (choice16flag == True):
                base16 = input('Enter a base 16 number: ')
                hexidecimalVerification = isBase16(base16)
                if (hexidecimalVerification):
                    newSum = base16TO10(base16)
                    print('Base 16 number: ' , base16 , 'is base 10 numer: ', newSum )
                    list16.extend(['Base16 number: ', base16,  ' ------> ', newSum, '\n'])
                    choice16flag = False
        elif (choice == '0'): #stops the program and prints the summary when user types 0
            summary(list2, list8, list16)
            flagmain = False
        else:
            print('invalid choice') #tells user if input doesnt meet standards
         
main()
    


    