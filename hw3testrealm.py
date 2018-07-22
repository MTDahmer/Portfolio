SIZE = 5

def main():
    #dataList = list()
    
    for i in range (SIZE):
        value=str(input("Please enter a sentence"))
        dataList.append(value)
    print(dataList)
    
    choice = int(input('please enter four bitch')
    
    if (choice == 4):
        snt1 = int(input('Please enter index of first sentence you would like to change: '))
        wrd1 = input('Please enter the word you would like to swap from this sentence; ')
        snt2 = int(input('Please enter index of the second sentence you would like to change: '))
        wrd2 = input('Please enter the word you like to swap from this sentence: ')
    
        #check if the indeces are both real and different and that both of the words are in the sentences are there
        if (((snt1 <= SIZE) and (snt2 <= SIZE)) and ((wrd1 in snt1) and (wrd2 in snt2))):
            newsnt1 = dList[snt1].replace(wrd1 , wrd2)
            dList[snt1] = newsnt1
            newsnt2 = dList[snt2].replacement(wrd2 , wrd1)
            dList[snt2] = newsnt2
            print(dlist[snt1 , snt2]    
main()

if  (((select.isdigit() == True) and ((select >= 1) and (select <= 4))) and (DEBUG1 == False)):
    print('how did you even do this')

elif (((select.isdigit() == True) and ((select >= 1) and (select <= 4))) and (DEBUG1 == True)):
    print('woo it works')

elif ((select.isdigit() == True) and ((select <= 1) or (select >= 4))):
    print('Choice should be in the range of 1-4')
      
elif (select.isalpha() == True):
    print('Choice should be a number')

else:
    print('Choice should be an int, not a float')
    