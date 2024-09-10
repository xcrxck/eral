import time

# Sign up
userReg = input('Register your username: ')

passReg = input('Register your password: ')

# Login
status = 1
while status == 1:
 
 userLog = input('Enter your username: ')
 
 if userLog == userReg:
     print('Your name is registered.')
     
     passLog = input('Enter your password: ')
     
     if passLog == passReg:
         print('Welcome to the system.')
         
         break
     else:
         attemptNum = 9
         # Gives the user 9 attempts to enter their password again.
         while True: 
             passRelog = input(f'Enter your password again (You have {attemptNum} more attempts): ')
             
             attemptNum -= 1
             
             if passRelog == passReg:
                 print('Welcome to the system.')
            
                 # Change status to false so the main loop breaks.
                 status = 2
                 
                 # Breaks the second loop.
                 break
             
             #  5 second timeout every 3 attempts.
             if attemptNum == 3 or attemptNum == 6:
                 print('You have been rate limited for 5 seconds.')
                 
                 time.sleep(5)
                 
             # Breaks the sequence if 9 attempts have been incorrectly entered.
             if attemptNum == 0:
                 passAdmin = input('Sytstem has been locked. Enter the admin password to continue: ')
                 
                 # Allows the admin to give the user an extra 2 attempts.
                 if passAdmin == 'aLIrez@gg':
                     attemptNum += 2
                     
                 else: 
                     print('System shutdown')   
                     # Breaks the main loop.
                     status = 2
                     # Breaks the second loop.
                     break
 # Allows the user to enter their username as much as they want at 2 second intervals.
 else:
     print('Your name is not registered. Press try again')
     
     time.sleep(2)