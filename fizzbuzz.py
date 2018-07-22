import math
var1 = 3
var2 = 10

def main():
   i = 1
   while i<100:
      if i%(var1*var2) == 0:
         print('FizzBuzz')
         i += 1      
      if i%var1 == 0:
         print('Fizz')
         i += 1
      if i%var2 == 0:
         print("Buzz")
         i += 1
      else:
         print(i)
         i += 1

main()