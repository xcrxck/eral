# First way (much worse)
user = input('Your username: ')
if user == 'Alireza1223' :
    print('Your username is registered')
    
else :
    print('SYSTEM LOCKDOWN')
    
password = input('Your password: ')
if password == '1234567' :
    print ('Your password is correct')
    print ('Welcome to the system, USER#2123')
    
else :
     print('SECURITY BREACH')

print('----------------------')

# Second way (much better)
user1 = input('Your username: ')
if user1 == 'Erfan':
    print('Username is correct')
    
    pass1 = input('Your password: ')
    if pass1 == '1234':
        print('Welcome to your app')
    else :
        print('Password is false')  
else : 
    print('Username is false')