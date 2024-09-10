# ANSI codes for colors.
black = '\033[30m'
red = '\033[31m'
blue = '\033[34m'
yellow = '\033[33m'
brightRed = '\033[91m'
# ANSI codes for styles.
bold = '\u001b[1m'
italic = "\u001b[3m"
# Reset color and style back to default
reset = '\033[0m'

# Modules  -------------------
import random

import time
#--------------------

studentNum = int(input(f'{blue}Enter the number of students{reset}: '))

list = []

for i in range(1 , studentNum+1):
    
    studentName = input(f'{yellow}Name of student{red} {i}{reset}: ')
    
    list.append(studentName)
    
print(f'One of the students will be randomly{brightRed}{bold} executed{reset}.')

#5 seconds time out.

time.sleep(5)

execute = list.pop(random.randrange(len(list)))

print(f'{black}{italic}{execute}{reset} has been executed.')