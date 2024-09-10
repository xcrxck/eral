while 32 == 32:
    
 num = int(input('Enter an integer: '))
 
 numStr = str(num)
 
 result = num % 2

 if len(numStr) == 4:
     if result == 0:
        print('Your number is four digits and even.')
        
     else:
        print('Your number is four digits and odd.')
        
 else: 
     if result == 0:
        print('Your number is not 4 digits but even')
        
     else: 
        print('Your number is not four digits but odd')
 
 input('Press enter to rerun the test. ')