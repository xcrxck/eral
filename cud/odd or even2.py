number = input('Enter a number: ')

multiplication = float(number) * 2

result = multiplication % 4

if result == 0:
    print('Your number is even.')
else:
    print('Your number is odd.')
