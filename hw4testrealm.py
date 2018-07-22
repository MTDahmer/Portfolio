import math

DEBUG1 = True

def areaofcircle(rds1):
    area = math.pi*(rds1*rds1)
    return area

def surfacesphere(rds2):
    surf = math.pi*4*(rds2*rds2)
    return surf

def volumesphere(rds3):
    vol = math.pi*(4/3)*(rds3*rds3*rds3)
    return vol

def callmenu():
    print('Enter 1 to calculate the area of a circle')
    print('Enter 2 to calculate the surface area of a sphere')
    print('Enter 3 to calculate the volume of a sphere')
    print('Enter 4 to quit')
    
def main():
    
    flag = True
    flag1 = True
    flag2 = True
    flag3 = True
    select = 0
    while (flag == True):
        callmenu
        select = int(input('fuck')
        if (select.isdigit() == True):
            if (select == 1):
                while (flag1 == True):
                    try:
                        rds1 = float(input('Enter the radius: '))
                        if (rds1 >= 0):
                            area = areaofcircle(rds1)
                            print('The area is: %.5f' % area) 
                            flag1 = False
                        else:
                            print('The radius must be a positive number')
                    except ValueError:
                        print('Radius must be a number')
                    
            elif (select == 2):
                while (flag2 == True):
                    try:
                        rds2 = float(input('Enter the radius: '))
                        if (rds2 >= 0):
                            surf = surfacesphere(rds2)
                            print('The surface area is: %.5f' % surf) 
                            flag2 = False
                        else:
                            print('The radius must be a positive number')
                    except ValueError:
                        print('Radius must be a number')              
                    
            elif (select == 3):
                while (flag3 == True):
                    try:
                        rds3 = float(input('Enter the radius: '))
                        if (rds3 >= 0):
                            vol = volumesphere(rds3)
                            print('The volume is: %.5f' % vol)
                            flag3 = False
                        else:
                            print('The radius must be a positive number')
                    except ValueError:
                        print('Radius must be a number')            
                    
            if (select == 4):
                print('Thank you for using this program!')
                flag = False 
            else:
                print('Choice should be in range 1-4')
        elif (select.isalpha()):
            print(' Choice should be a number')
        else:
            print('Choice should be an int, not a float')

main()
