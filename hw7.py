# File: homework7.py
# Author: Mitchell Dahmer
# Date: 10/24/17
# Section: 503
# Email: mtdahmer@tamu.edu
# Description: Program takes a file from the user and convberts all characters found within into either an ascii code
# if the character is alphanumeric or a .. if the character is not. It then translates the that ascii code into the base
#of the user's choosing, from 2-9

import math
#converts the file characters to ascii base ten then to the preferred base
#also changes any symbols to ..
#input: the file and the choice of base
#output: the list of ascii characters
def ASCIIbaseconverter(textFile, baseChoice):
    
    alphaNumeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz' #sets a list for checking if characters are symbols
    elementCount = 0
    i = 0
    asciiList = list()
    numberlist = list()
    while (i < len(textFile)): #starts loop that only runs for the count of the characters in the file
        for char in textFile: #starts chain to check if the character matches the above on the list
            if char in alphaNumeric:
                originalBase = ord(char) #takes the ascii of the character
                while (originalBase > 0) : #starts a loop for the math and append process until the ascii value cannot be divided anymore
                    digit = originalBase % baseChoice #finds the remainder of the ascii value
                    numberlist.append(digit) #appends the list with the digit
                    originalBase = originalBase // baseChoice #finds the new number to be divided by the base 
                numberlist.reverse() #flips the list 
                string = ''.join(str(e) for e in numberlist) #joins the list together to make one number
                
                asciiList.append(string) #adds the now string to the list of ascii values
                numberlist = [] #resets list
                elementCount += 1 #counts up to see when to put an \n
                i += 1 #counts up to see when to stop the whole loop
            else:
                asciiList.append('..') #adds .. to list if character not on above list
                elementCount += 1
                i += 1
            test = elementCount % 5 #checks wether or not 5 elements have passed since the last line break
            if (test == 0):
                asciiList.append('\n') #adds line break if 5 elements have been added
    
    return asciiList
            
def baseChooser (): #takes user base input and determins if it is usable
    flagBase = True
    baseChoice = int(input('Enter a base between 2 to 9: '))
    while (flagBase == True):
        if ((baseChoice >= 2) and (baseChoice <= 9)):
            flagBase = False
            return baseChoice
        else:
            flagBase = True
    

    
    
    
def main():
    flagmain = True
    dataList = list()
    print('This is a filter program that will convert your text file into ASCII valus') #greeting
    while (flagmain == True): #starts main loop for program
        filename = input('Enter the name of the file: ') #takes file name from user
        baseChoice = baseChooser() #calls verifier for base choice
        try:
            infile = open(filename, 'r') #opens user files
            textFile = list(infile.read()) #truns contents into lists
            infile.close #close file after proper info taken
            conversion = ASCIIbaseconverter(textFile , baseChoice) #calls converter function with text and base choice
            outFileName = str(baseChoice) + '_' + str(filename) #creates the custom file name for new file
            outFile = open('{0}.txt'.format(outFileName) , 'w+')
            for element in conversion: #adds newly converted ascii into the new file 1 by 1
                outFile.write(element)
                outFile.write(' ')
            print('Your new files name is ' , outFileName)
            outFile.close() #closes file
            flagmain = False
        except FileNotFoundError:
            flagmain = True #gives input again if users filename does not exist
            
        
            
main()
    

  