import time
import random
# ANSI escape sequences for colors and styles.
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
darkGrey = '\033[90m'
bold = '\u001b[1m'
italic = "\u001b[3m"
# Reset color and style back to default
reset = '\033[0m'

print('Welcome to Rock, Paper, Scissors!')

time.sleep(1)

userScore = 0
cpuScore = 0
    
# Main Game loop
while True: 
 allChoices = ['Rock','Paper','Scissors']
 
 # User input to lowercase allowing for various capitalized or uncapitalized inputs. Also shows scores every round.
 userChoice = str.lower(input(f'(Current scores: {red}Cpu: {cpuScore} {blue}User: {userScore}{reset}) {yellow}Play your {italic}turn or type "P" for pause menu:{reset} '))

 # Similar thing for cpuChoice. CPU chooses a random item from allChoices.
 cpuChoice = str.lower(random.choice(allChoices))
 
 # Outcome for a draw.
 if cpuChoice == userChoice:
     print(f"Both you and the CPU chose {darkGrey}{userChoice}{reset}. It's a draw!")
     
     # Slight delay in all outcomes to allow the user to read the text.
     time.sleep(1.5)
     
 # Outcome if user has chosen paper.
 elif userChoice == 'paper':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1.5)
     
     if cpuChoice == 'rock':
         print(f'{blue}You {bold}win!{reset}')
         # Gives user one score.
         userScore += 1
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
         # Gives CPU one score.
         cpuScore += 1 

         
 # Outcome if user has chosen scissors.        
 elif userChoice == 'scissors':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1.5)
     
     if cpuChoice == 'paper':
         print(f'{blue}You {bold}win!{reset}')
        
         userScore += 1
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
        
         cpuScore += 1 
         
 # Outcome if user has chosen rock.       
 elif userChoice == 'rock':
     print(f'CPU chose {cpuChoice}.')
     
     time.sleep(1.5)
     
     if cpuChoice == 'scissors':
         print(f'{blue}You {bold}win!{reset}')
         
         userScore += 1
         
     else:
         print(f'{red}CPU {bold}win!{reset}')
         
         cpuScore += 1 
    
 # Pause menu
 elif userChoice == 'p' or userChoice == 'pause':
     print('Game paused')
     
     pause = str.lower(input('Type "Q" to exit the game or type "R" to reset scores, otherwise press enter key to unpause: '))
     
     if pause == "q" or pause == "quit":
         break
     
     elif pause == "r" or pause == "reset":
         cpuScore = 0
         userScore = 0

 else: 
     print(f'Wrong input! Please choose between "{darkGrey}Rock{reset}, Paper,{red} Scissors{reset}".')