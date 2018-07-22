# File: homework4.py
# Author: Mitchell Dahmer
# Date: 10/3/17
# Section: 503
# Email: mtdahmer@tamu.edu
# Description: A program that uses true/false loops and custom math functions to calculate the area of a circle
# and the surface area and volume of spheres based on a radius provided by a user



import math



DEBUG1 = True



def areaofcircle(rds1): #function computes the area of a circle
    
    area = math.pi*(rds1*rds1)
    return area



def surfacesphere(rds2): #function computes the surface area of a sphere
    
    surf = math.pi*4*(rds2*rds2)
    return surf



def volumesphere(rds3): #function computes the volume of a sphere
    
    vol = math.pi*(4/3)*(rds3*rds3*rds3)
    return vol



def callmenu(): #function calls the menu of options
    
    print('Enter 1 to calculate the area of a circle')
    print('Enter 2 to calculate the surface area of a sphere')
    print('Enter 3 to calculate the volume of a sphere')
    print('Enter 4 to quit')
 
 
    
def main():
    
    flag = True #flags for lopps within the choices
    flag1 = True
    flag2 = True
    flag3 = True
    select = -1
    
    
    
    while (flag == True): #begins the loop for the selection and functions
        
        
        
        callmenu()     #calls the menu function
        
        
        try:
            
            select = int(input('Enter your choice: ')) #gets the users choice for menu
            
            if (select == 1):
                
                while (flag1 == True): #begins loop if user selects 1
                    
                    try: #makes sure the user is using a number
                        
                        rds1 = float(input('Enter the radius: '))
                        
                        if (rds1 >= 0): # makes sure the users radius is positive
                            area = areaofcircle(rds1) #calls area function
                            print('The area is: %.5f' % area) #prints answer
                            flag1 = False #stops area loop
                        
                        else:
                            print('The radius must be a positive number')
                            
                    except ValueError:
                        print('Radius must be a number')
                        
                        
                    
            elif (select == 2):
                
                while (flag2 == True): #begins loop if user selects 2
                    
                    try: #makes sure the user is using a number
                        
                        rds2 = float(input('Enter the radius: '))
                        
                        if (rds2 >= 0): # makes sure the users radius is positive
                            surf = surfacesphere(rds2)
                            print('The surface area is: %.5f' % surf) #prints answer
                            flag2 = False #stops surface loop
                            
                        else:
                            print('The radius must be a positive number')
                            
                    except ValueError:
                        print('Radius must be a number') 
                        
                        
                    
            elif (select == 3):
                
                while (flag3 == True): #begins loop if user selects 3
                    
                    try: #makes sure the user is using a number
                        
                        rds3 = float(input('Enter the radius: '))
                        
                        if (rds3 >= 0): # makes sure the users radius is positive
                            vol = volumesphere(rds3)
                            print('The volume is: %.5f' % vol) #prints answer
                            flag3 = False #stops volume loop
                            
                        else:
                            print('The radius must be a positive number')
                   
                    except ValueError:
                        print('Radius must be a number')            
                    
                    
                    
            if (select == 4):
                print('Thank you for using this program!')
                flag = False #stops main loop
            
            else:
                print('Choice should be in range 1-4')
                
                
        except ValueError:
            print('Choice must be an int, not a float') #accounts for float being entered for choice
        except NameError:
            print('Choice must be a number') #accounts for string being entered for choice

main()
