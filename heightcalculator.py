import math
bookcase = 82
wardrobe = 72
chest = 54
cabinet = 32
table = 29
bedbetween1 = 24
bedbetween2 = 22
chairs = 16
coffeetable = 18
averageheight = 69
debug = True
def tallerthan69heightconverter(height):
    if (debug):
        print('ding6')
        print(height)
    furniture = input('What peice of furniture are you buidling? ')
    furniture = furniture.lower()
    if (debug):
        print('ding7')
    if ((furniture == 'bookshelf') or (furniture == 'bookcase')):
        newbookcase = (height/averageheight)*bookcase
        print('Your bookcase should be %.1f inches tall' % newbookcase)
def heightverifier(height):
    if (height.isdigit()):
        height = int(height)
        if (debug):
            print('ding2')
            print(height)
        if (height >= 69):
            print('ding3')
            tallerthan69heightconverter(height)
            
        elif ((height < 69) and (height > 0)):
            if (debug):
                print('ding4')
            shorterthan69heightconverter(height)

        elif (height < 0):
            print('ding5')
            print('The measurement you have entered is impossible')
        else: 
            print('Something has gone terribly wrong')    
        
def main():
    height = ''
    flagmain2 = True
    flagmain1 = True
    choice = ''
    choice2 = ''
    print('This program will find the most comfortable height for a peice of furniture')
    print('This will be based on the standard hieght for furniture for a 5 ft. 9 in. person')
    print('That height will then be translated to either your height or the height of the person you are building it for')
    print('Please enter the height of the person who will be using the furniture in inches with no unit markers')
    while (flagmain1 == True):
        
        height = input('Height: ')
        
        while (flagmain2 == True):
            heightverifier(height)
            choice = str(input('Would you like to find the height of another peice of furniture?: '))
            if ((choice[0] == 'n') or (choice[0] == 'N')):
                print('Thank you for using this program!')
                flagmain1 = False
                flagmain2 = False
            elif ((choice[0] == 'y') or (choice[0] == 'Y')):
                flagmain2 = True 
                choice2 = str(input('Would you like to change the height you entered? : '))
                if ((choice2[0] == 'y') or (choice2[0] == 'Y')):
                    flagmain1 = True
                elif ((choice2[0] == 'n') or (choice2[0] == 'N')):
                    flagmain1 = False
                
main()
            