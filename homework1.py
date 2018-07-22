# File: homework1.py
# Author: Mitchell Dahmer
# Date: 9/11/17
# Section: 503
# Email: mtdahmer@tamu.edu
# Description: A python program for taking user inputs of numbers and strings and modifying them based on predetermined qualifications.
# The numbers are run through a series of math functions and the string is modified and translated in various ways
import math
import cmath
def main():

    userValue = int(input('Please input your number: ')) #first section is the integer, which is taken from the user
    firstValue = userValue % 3 #divides the users integer by 3 and gives the remainder, then prints the outcome
    print('The remainder of your number after being divided by three is: %d' % firstValue) #not required but the inclusion of statements to explain what was happening to the user seemed better
    secondValue = pow(userValue, 3) #raises the integer to the power of three then prints the outcome
    print('Your number cubed is: %d' % secondValue)
    thirdValue = math.log(userValue,10) #takes the logarithmic base 10 function of the users integer and prints it with a float 5
    print('The log of your number is: %.5f' % thirdValue)

    userStrng = input('Please enter 5 letters: ') #second section is the string, which is five letters from the user
    print('The last three letter of your string are: %s' %  userStrng[-3]+userStrng[-2]+userStrng[-1]) # shows the last three characters of the submitted string through the use of negative index to find the end no matter how many characters are entered
    print('The ASCII code for the third letter of your string is: %d' % ord(userStrng[2])) #translates whatever the third character is into its ASCII code
    firstLttr=userStrng[0]
    newStr=userStrng.replace('%s' % firstLttr,'@')
    print('Your string with every instance of the first letter replaced with @: %s' % newStr) #finds the first character of the string and looks for other any other that are the same and replaces them with the @ symbol

main()







