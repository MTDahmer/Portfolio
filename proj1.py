def fillWithAT(grid, theRow, theCol, display, fileData):
    y = int(theRow)
    x = int(theCol)
    if(grid[y][x] == '-'):
        grid[y][x] = '@'
        if (display):
            for i in range (len(grid)):
                for j in range (len(grid[0])):
                    print (grid[i][j], end = ' ')
                print()
    try:
        fillWithAT( grid , y-1 , x , display)
        fillWithAT( grid , y+1 , x , display)
        fillWithAT( grid , x-1 , y , display)
        fillWithAT( grid , x+1 , y , display)
    except:
        print('ding')
    
def printMatrix(fileName):
    with open(fileName) as textFile:
        grid = [line.split() for line in textFile]
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                print (grid[i][j], end = ' ')
            print()
        return grid
def printGreeting():
    print('This program will replace instances of "-" in a given file with the "@" symbol')
    print('along with the instaces of "-" surrounding the chosen instance')
    print('The file must contain only the characters "-" and "I" and must be rectangular')

    
def testCharacter(fileData):
    charlist = list()
    charList = set('-I')
    for i in (fileData):
        for char in i:
            if not (char in charList):
                print('false')
                return False
    return True
    
def testRectangle(fileData):
    n = fileData
    for i in n:
        if len(i) != len(n[0]):
            return False
    return True

def countRows (fileData):
    sum1 = len(fileData)
    print(sum1)
    return sum1

def countColumns (fileData):
    sum2 = len(fileData[0])
    print(sum2)
    return sum2
    
  

def getRow(fileName , fileData):
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
    if ((theRow <= rowcount) and (theRow >= 0)):
        return True
    else:
        return False
    
def getCol(fileData):
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
    if ((theCol <= columncount) and (theCol >= 0)):
        return True
    else:
        return False    
def requestStep():
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
        try:
            fileName = input('Enter the name of your file: ')
            infile = open(fileName , 'r')
            for line in infile:
                fileData.extend(line.strip().split('\n'))
            bool1 = testCharacter(fileData)
            bool2 = testRectangle(fileData)
            if ((bool1 == True) and (bool2 == True)):
                grid = printMatrix(fileName)
                flagmain = False
            elif (bool1 == False):
                print('Your input has a character other than "-" and "I"')
                fileData = list()
            elif (bool2 == False):
                print('Your input was not rectangular')
                fileData = list()
            else:
                flagmain = True 
                fileData = list()
        except:
            flagmain = True
            fileData = list()
    theRow = getRow(fileName , fileData)
    theCol = getCol(fileData)
    display = requestStep()
    fillWithAT(grid, theRow, theCol, display, fileData)
    continueChoice = input('Go again? Enter yes: ')
main()
    
    
