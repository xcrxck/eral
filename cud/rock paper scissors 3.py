import time
import random
# ANSI escape sequences for colors and styles.
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
darkGrey = '\033[90m'
bold = '\u001b[1m'
italic = "\u001b[3m"
# Reset color and style back to default
reset = '\033[0m'

print('Welcome to Rock, Paper, Scissors!')

time.sleep(1)

# Function for setting game speed
def game_speed():  
 global delayTime
 
 delayTime = 0
 
 while True: 
     setDelay = str.lower(input(f'Type your game speed ({red}Slow{reset}/{green}Normal{reset}/{blue}Fast{reset}): '))

     if setDelay == 'slow':
         delayTime = 3

     elif setDelay == 'normal':
         delayTime = 1.5
    
     elif setDelay == 'fast':
         delayTime = 0.5
         
     else:
         print('Wrong Input! Please try again')

     if delayTime != 0:
         break
game_speed()
         
# Score counters
userScore = 0
cpuScore = 0

# Main Game loop
status = True
while status == True: 
 allChoices = ['Rock','Paper','Scissors']
 
 # User input to lowercase allowing for various capitalized or uncapitalized inputs also shows scores every round
 userChoice = str.lower(input(f'{yellow}Play your {italic}turn or type "P" for pause menu:{reset} '))

 # Similar thing for cpuChoice. CPU chooses a random item from allChoices
 cpuChoice = str.lower(random.choice(allChoices))
 
 result = ''
 
 # Outcome for a draw
 if cpuChoice == userChoice:
     
     result = 'draw'

 # Outcome if user has chosen paper
 elif userChoice == 'paper':
     
     if cpuChoice == 'rock':
         result = 'win'
         
     else:
         result = 'lose'
         
 # Outcome if user has chosen scissors       
 elif userChoice == 'scissors':
     
     if cpuChoice == 'paper':
         result = 'win'
         
     else:
         result = 'lose'
         
 # Outcome if user has chosen rock      
 elif userChoice == 'rock':
     
     if cpuChoice == 'scissors':
         result = 'win'
         
     else:
         result = 'lose'
    
 # Pause menu
 elif userChoice == 'p' or userChoice == 'pause':
     print('Game paused')
     
     # Loop for pause menu
     while True:
         pause = str.lower(input(f'Type {red}{bold}"Q"{reset} to exit the game/{yellow}{bold}"R"{reset} to reset scores/{green}{bold}"GS"{reset} to change the game speed, otherwise press {blue}{bold}enter key{reset} to unpause: '))
     
         if pause == 'q' or pause == 'quit':
             status = False
             break
     
         elif pause == 'r' or pause == 'reset':
             cpuScore = 0
             userScore = 0
             
             print('Changes applied!')
             
             time.sleep(1)
         
         elif pause == 'gs' or pause == 'gamespeed' or pause == 's' or pause == 'change speed':
             game_speed()
             
             print('Changes applied!')
             
             time.sleep(1)
             
         elif pause == '':
             break
         
         else:
             print('Wrong input! Please try again')
         
 else: 
     print(f'Wrong input! Please choose between "{darkGrey}Rock{reset}, Paper,{red} Scissors{reset}".')
     
 # Shows what the CPU chose    
 if result != '':
     print(f'CPU chose {cpuChoice}.')
     
     # Delay to allow the user to read the text
     time.sleep(delayTime)

 # Results and score changes
 if result == 'draw':
     print(f'Both you and the CPU chose {darkGrey}{userChoice}{reset}. It is a draw!')
     
 elif result == 'win':
     userScore += 1

     print(f'{blue}You {bold}win!{reset}')
     
 elif result == 'lose':
     cpuScore += 1
     
     print(f'{red}CPU {bold}win!{reset}')
     
 # Shows score (has the same conditions as line 127 but difference is when they happen)    
 if result != '':
     time.sleep(delayTime/2)
     
     print(f'Current scores: {red}Cpu: {cpuScore} {blue}User: {userScore}{reset}')