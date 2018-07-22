  #ask the user for how many strings they are going to enter


SIZE = int(input("How many sentences would you like the enter? "))

def main():
                                          
                                          
 #take the sentences from the user, set loop for users size and set the sentences to all lowercase
    
    
    dList = list()
    
    for i in range(SIZE):
        value = str(input('Please enter a sentense: '))
        value = value.lower()
        dList.append(value)
    
    print(dList)

  #set loop for options with the same number of times as the list
    
    
    for i in range (SIZE):
        print ('Enter 1 to see a sentence')
        print ('Enter 2 to see the whole list')
        print ('Enter 3 to change a sentence')
        print ('Enter 4 to switch words')
        choice = int(input('Enter choice here: ' ))
        
        
#if/else/elif tree for the options listed going from 1-5 and including possibility of error

  #option 1: ask user for index
  
    if (choice == 1) :
        one += 1
        ind = int(input('Please enter the index of the sentence you wish to see: '))
       
#if valid index, find sentence for index and print  

        if ((ind <= SIZE)) :
            print (dList[ind])
        
#if not valid index, print error
        
        else:
            print ('Invalid index') 

  #option 2: display entire list of sentences
    elif (choice == 2):
        two += 1
        print(dList)
    
  #option 3: ask user for index of sentence they would like to change
    elif (choice == 3):
        three += 1
        snt = int(input('Please enter the index of the sentence you would like to change: '))
    #if valid index, ask for input of new sentence and change that index to the that
         
        if ((snt <= SIZE)):
            repl = str(input('Please enter your new sentence: '))
            dList[snt]=repl
            print ('New sentence is: %s' % dList[snt])
    #if not valid index, display an error
        
        else:
            print('Invalid index')
  
  
  #option 4: ask for indeces and words to swap from user for what they would like to change
    elif (choice == 4):
        four +=
        snt1 = int(input('Please enter index of first sentence you would like to change: '))
        wrd1 = input('Please enter the word you would like to swap from this sentence; ')
        snt2 = int(input('Please enter index of the second sentence you would like to change: '))
        wrd2 = input('Please enter the word you like to swap from this sentence: ')
         
    #check if the indeces are both real and different and that both of the words are in the sentences are there
        if (((snt1 <= SIZE) and (snt2 <= SIZE)) and ((wrd1 in dList[snt1]) and (wrd2 in dList[snt2]))):
            
            newsnt1 = dList[snt1].replace(wrd1, wrd2)
            dList[snt1] = newsnt1
            newsnt2 = dList[snt2].replace(wrd2, wrd1)
            dList[snt2] = newsnt2
            print(dList[snt1])
            print(dList[snt2])
    
    #if anything not valid, display error message
        elif (snt1 > SIZE):
            print('First index invalid')
        elif (snt2 > SIZE):
            print('Second Index invalid')
        elif (wrd1 not in dList[snt1]):
            print('Word not in first sentence')
        elif (wrd2 not in dList[snt2]):
            print('Word not in second sentence')
  
  #if not 1-4 display error message
    else:
        Print('Option not available')
         
        print("You sleected choice 1 %.0f time(s)" % one)
        print("Uou selected choice 2 %.0f time(s)" % two)
        print("You selected choice 3%.0f time(s)" % three)
        print("You selected choice 4%.0f time(s)" % four)
      

main()