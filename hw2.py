# File: hw2.py
# Author: Mitchell Dahmer 
# Date: 9/18/17
# Section: 503
# E-mail: mtdahmer@tamu.edu
# Description: a program that takes two operands from a user and then modifies them based on the operation given by the user in the form of a string

import math
def main():
    firstInteger = int(input("Please enter the first operand: "))   #these three lines take the desired inputs from the user in the form of two numbers and an operation respectively
    secondInteger = int(input("Please enter the second operand: "))
    userOper = str(input("Please enter the operation: "))
    operation= userOper.lower()  #turns the strin input by the user into all lowercase letters for easier identification
    print("Operand 1 is %.0f" % firstInteger) #three lines that print off the variables input by the user
    print("Operand 2 is %.0f" % secondInteger)
    print("The operation is %s" % userOper)    
    if (operation=='add'):  #adds the integers together if the input operation is add and then prints the total
        total = firstInteger+secondInteger       
        print("Your result is %.3f" % total)        
    elif (operation=='subtract'):  #subtracts the integers from each otherif the input operation is subtract and then prints the total
        total = firstInteger-secondInteger
        print("Your result is %.3f" % total)        
    elif (operation=='multiply'):  #multiplies the integers together if the input operation is multiply and then prints the total
        total = firstInteger*secondInteger
        print("Your result is %.3f" % total)        
    elif (operation=='divide'):  #divides the integers by each other if the input operation is divide and then prints the total
        if(secondInteger==0):  #gives the user and error if the second operand is a 0
            print("Division by zero is not allowed")
        else:
            total = firstInteger/secondInteger
            print("Your result is %.3f" % total)                    
    else:
        print("Invalid operation") #gives an error if the operation given is not one of the four
    total = abs(total) #three lines that take the absolute value of the total and turn the total into a string whose integers can be counted to find length
    strTotal = str(total)
    numb = len(strTotal) 
    if ((firstInteger>0) and (secondInteger>0)) or ((firstInteger<0) and (secondInteger<0)) or ((numb>2)): #prints a line between the total and the special conditions only if any exist
        print('------------------------------')
    if (firstInteger>0) and (secondInteger>0): #prints notifcation if both operand are positive
        print("Both operand are positive")
    elif(firstInteger<0) and (secondInteger<0): #prints notifcation if both operand are negative
        print("Both operand are negative")
    if (numb>2): #prints notification if the number has over three digits
        print("The result is has three or more digits")
        
main()