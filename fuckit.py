def fillWithAT(grid, theRow, theCol, display):
    print('ding')
    
def printGreeting():
    print('Hello user')
    print('This program will replace instances of "-" in a given file with the "@" symbol')


def testCharacter(fileData):
    print('ding1')
    charlist = list()
    charList = set('-I')
    for i in (fileData):
        for char in i:
            if not (char in charList):
                print('false')
                return False
    return True
    
def testRectangle(fileData):
    print('ding5')
    n = fileData
    for i in n:
        if len(i) != len(n[0]):
            return False
    return True

def countRows (fileData):
    print('ding6')
    sum1 = len(fileData)
    print(sum1)
    return sum1

def countColumns (fileData):
    print('ding7')
    sum2 = len(fileData[0])
    print(sum2)
    return sum2
    
def createMatrix(fileData , fileName):
    print('ding')
 
    
    


def getRow(fileName , fileData):
    print('ding9')
    flagrow = True
    rowcount = countRows(fileData)
    while (flagrow == True):
        theRow = int(input('Enter the row number: '))
        rowtest = testRow(theRow , rowcount)
        if (rowtest):
            flagrow = False
            return theRow
        else:
            flagrow = True
    
def testRow(theRow , rowcount):
    print('ding10')
    if ((theRow <= rowcount) and (theRow >= 0)):
        return True
    else:
        return False
    
def getCol(fileData):
    print('ding11')
    flagcolumn = True
    columncount = countColumns(fileData)
    while (flagcolumn == True):
        theCol = int(input('Enter the column number: '))
        coltest = testRow(theCol , columncount)
        if (coltest):
            flagcolumn = False
            return theCol
        else:
            flagcolumn = True    
    
def testCol(theCol , columncount):
    print('ding12')
    if ((theCol <= columncount) and (theCol >= 0)):
        return True
    else:
        return False    
def requestStep():
    print('ding13')
    displaychoice = input('Print out step by step? Enter yes: ')
    displaychoice = displaychoice.lower()
    if (displaychoice == 'yes'):
        return True
    else:
        return False
    
def main():
    flagmain = True
    printGreeting()
    fileData = list()
    while (flagmain == True):
        fileName = input('Enter the name of your file: ')
        with open(fileName) as textFile:
            lines = [line.split() for line in textFile]
            print(lines)
            for i in range (len(lines)):
                for j in range (len(lines[0])):
                    print (lines[i][j], end = ' ')
                print()
main()