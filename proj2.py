import math 
def greeting(): #prints greeting for the user
    print('Welcome to the bookstore program!')
    
def readDatabase(theInventory): # reads databse and fills the dictionary with lists of data
    flagg = True
    
    while flagg: #starts loop for function
        lastName = ''
        firstName = ''
        title = ''
        qty = 0
        price = 0
        dataList = []
        infoList = [] #lien 9-15 set up variables for the file reading
        try:
            fileName = input('Enter the name of the file: ') #takes file input from user 
            with open(fileName, 'r') as f:
                for line in f: #reads through lines within the given file
                    dataList = line.split(',') #pulls data from file and splits it along the commas
                    lastName = dataList[0]
                    firstName = dataList[1]
                    title = dataList[2]
                    qty = dataList[3]
                    price = dataList[4]    #lines 21-25 put the split data into the previously set up variable           
                    author = str(lastName + ',' + firstName) #combines the last and firstnames together for the dictionary key
                    infoList.append(title)
                    infoList.append(qty)
                    infoList.append(price.rstrip()) #three lines that append the data to a list to  key into the dictionary
                    theInventory.setdefault(author, []).append((infoList)) #adds keys and values while also adding onto the keys that have already been added if the author is the same
                    infoList = [] #resets list to prevent cross contamination
            flagg = False
            return theInventory #takes the inventory back to the main
        except: #if the file given is wrong in any way, informs the user
            print('Error reading database')
            flagg = True 
            
            
def printMenu(): #prints options for  the user and takes their choice
    print('----------------------------')
    print('Enter 1 to display the inventory')
    print('Enter 2 to display the books by one author')
    print('Enter 3 to add a book')
    print('Etner 4 to change the price')
    print('Enter 5 to change the qty on hand')
    print('Enter 6 to view the total number of books in the inventory')
    print('Enter 7 to see the total amount of the entire inventory')
    print('Enter 8 to exit')
    choice = input('Enter your choice: ')
    return choice
    
def displayInventory(theInventory): #in: theInventory. Prints the entire inventory of the store
    for key in sorted(theInventory):
        info = theInventory[key] #moves info taken from the key to a variable to search through
        print ('The author is:' , key) #prints author on top
        print(' ')
        for list in info: #moves through each item in key
            print ('           The title is: ' , list[0])
            print ('           The qty is: ' , list[1])
            print ('           The price is: ' , list[2])
            print ('           ---')
            print (' ')
   
def displayAuthorsWork(theInventory): #in: the inventory dictionary. displays the works of only one author
    firstName = (input("Enter the author's first name: ")).lower()
    firstName = firstName.capitalize()
    lastName = (input("Enter the author's last name: ")).lower()
    lastName = lastName.capitalize() #the four lines take in the names from the user and align with the capitlization within the system
    author = str(lastName + ',' + firstName)
    flagcheck = databaseAuthorCheck(theInventory, author) #calls program to check if author is in the dictionary
    if flagcheck:
        for list in theInventory[author]: #same as previous use but without author
                print ('           The title is: ' , list[0])
                print ('           The qty is: ' , list[1])
                print ('           The price is: ' , list[2])
                print ('           ---')
                print (' ')
    else: #informs user if author doesnt exist
        print('This author does not exist in the Iventory')
    
def databaseAuthorCheck(theInventory, author): #in: author and dictionary out: boolean
    if (author in theInventory): #checks if author is in dictionary
        return True
    else:
        return False
    
def addBook(theInventory): #adds books to the inventory with author, title, price and qty
    dataList = []
    firstName = (input("Enter the author's first name: ")).lower()
    firstName = firstName.capitalize()
    lastName = (input("Enter the author's last name: ")).lower()
    lastName = lastName.capitalize()#same as line 68
    author = str(lastName + ',' + firstName) #same as line 26
    title = (input("Enter the title: ")).lower() 
    title = title.capitalize() #normalizes title capitilization
    flagcheck = databaseChecker(theInventory, author, title) #runs function to check if book already in dictionary
    if flagcheck:
        print('This book already exists in the Inventory and cannot be added again.')  
    else:
        flagqty = True
        flagprice = True
        while flagqty: #starts loop for checking qty valid
            qty = input('Enter the qty: ')
            if (qty.isnumeric()):
                flagqty = False
            else:
                print('Invalid Quantity')
                flagqty = True
      
        price = input('Enter the price: ')
        try:
            '{:.2f}'.format(float(price)) #checks for float
            dataList.append(title)
            dataList.append(qty)
            dataList.append(price)
            theInventory.setdefault(author, []).append((dataList))
            dataList = [] #113-116 same as 27-30
        except ValueError: #catch for invalid price
            print('Invlid Price')
                    
def databaseChecker(theInventory, author, title): #in:theInventory,author and title. out: boolean. checks if the book is in the the dictionary already
    if (author in theInventory):
        for list in theInventory[author]:
            if list[0] == title: #searches inbdividual lists within the keys
                return True
        return False #returns false if book not within
    else:
        return False #returns false if author is not within
def changePrice(theInventory): #Changes price on selected books
    firstName = (input("Enter the author's first name: ")).lower()
    firstName = firstName.capitalize()
    lastName = (input("Enter the author's last name: ")).lower()
    lastName = lastName.capitalize()
    author = str(lastName + ',' + firstName)
    title = (input("Enter the title: ")).lower()
    title = title.capitalize() 
    flagPriceChange = databaseChecker(theInventory, author, title)
    if flagPriceChange:
        for list in theInventory[author]:
            if list[0] == title: #searches for specific title to change
                price = input('Enter the price: ')
                try:
                    '{:.2f}'.format(float(price)) #checks if float
                    for i in theInventory[author]:
                        if i[0] == title:
                            i[-1] = price                    
                except ValueError:
                    print("Invalid Price")
    else:
        print("No such author or book in your database.  So you cannot change the price")
def changeQty(theInventory): #works the same as the price changer but moves to a different item in the list
    firstName = (input("Enter the author's first name: ")).lower()
    firstName = firstName.capitalize()
    lastName = (input("Enter the author's last name: ")).lower()
    lastName = lastName.capitalize()
    author = str(lastName + ',' + firstName)
    title = (input("Enter the title: ")).lower()
    title = title.capitalize() 
    flagQtyChange = databaseChecker(theInventory, author, title)
    if flagQtyChange:
        for i in theInventory[author]:
            if i[0] == title:
                qty = input('Enter the qty: ')
                if qty.isnumeric():
                    for i in theInventory[author]:
                        if i[0] == title:
                            i[1] = qty
                else:
                    print('invalid price')
        
    else:
        print("No such author or book in your database.  So you cannot change the qty")    
    
def totalQty(theInventory): #totals up the number of copies of every book together
    total = 0
    for key in theInventory: #moves through every key in the dicitonary
        info = theInventory[key]
        for list in info:
            total = total + int(list[1]) #adds to running total
    print('The total number of books is: %d' % total) #prints total
    
def calculateTotalAmount(theInventory): #works same as the total quantity but with the price
    total = 0
    for key in theInventory:
        info = theInventory[key]
        for list in info:
            total = total + float(list[2])
    print('The total value of the inventory is: %.2f' % total)

def main():
    #print greeting
    greeting()
    #dictionary to hold the inventory
    theInventory ={}
    #put the data in the file into the dictionary+
    readDatabase(theInventory)
    flag = True
    #keep looping till flag is set to False
    while flag:
        choice = printMenu()
        if choice=="1":
            displayInventory(theInventory)
        elif choice=="2":
            displayAuthorsWork(theInventory)
        elif choice=="3":
            addBook(theInventory)
        elif choice=="4":
            changePrice(theInventory)
        elif choice=="5":
            changeQty(theInventory)
        elif choice=="6":
            totalQty(theInventory)
        elif choice=="7":
            calculateTotalAmount(theInventory)
        elif choice=="8":
            print ("Thank you for using this program")
            flag = False
        else:
            print ("Invalid choice")
main() 