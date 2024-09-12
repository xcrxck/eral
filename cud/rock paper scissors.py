import time
import random
# ANSI escape codes for colors.
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
lightGrey = '\033[37m'
darkGrey = '\033[90m'
# ANSI escape codes for styles.
bold = '\u001b[1m'
italic = "\u001b[3m"
# Reset color and style back to default
reset = '\033[0m'

print('Welcome to Rock, Paper, Scissors!')

time.sleep(1)

status = 1

timeout = 0

# Allows the game to be replayed while status is true.
while status == 1:
 allChoices = ['Rock','Paper','Scissors']
 
 # User input to lowercase allowing for various capitalized or uncapitalized inputs.
 userChoice = str.lower(input(f'{yellow}Play your {italic}turn{reset}: '))
 
 # Similar thing for cpuChoice. Pops a random index from main list that will be returned once the code reruns. (could have also used random.choice without pop.)
 cpuChoice = str.lower(allChoices.pop(random.randrange(len(allChoices))))
 
 # Outcome for a draw.
 if cpuChoice == userChoice:
     print(f"{lightGrey}Both you and the CPU chose {darkGrey}{userChoice}{lightGrey}. It's a draw!{reset}")
     
     # Slight delay in all outcomes to allow the user to read the text.
     time.sleep(1)
     
     timeout += 1
     
 # Outcome if user has chosen paper.
 elif userChoice == 'paper':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1)
     
     if cpuChoice == 'rock':
         print(f'{blue}You {bold}win!{reset}')
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
     
     timeout += 1
         
 # Outcome if user has chosen scissors.        
 elif userChoice == 'scissors':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1)
     
     if cpuChoice == 'paper':
         print(f'{blue}You {bold}win!{reset}')
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
         
     timeout += 1
         
 # Outcome if user has chosen rock.       
 elif userChoice == 'rock':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1)
     
     if cpuChoice == 'scissors':
         print(f'{blue}You {bold}win!{reset}')
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
         
     timeout += 1
         
 else: 
     print(f'Wrong input! Please choose between "{darkGrey}Rock{reset}, Paper,{red} Scissors{reset}".')
    
 # Asks the user if they want to keep playing or not every five rounds(once the timeout has been reached).    
 if timeout == 5:
     replay = str.lower(input(f'Do you want to play again ({blue}y{reset}/{red}n{reset})? '))
 
     if replay == 'n' or replay == 'no':
         print(f'{black}Quitting game.{reset}')
         
         status = 2
     else:
         timeout = 0