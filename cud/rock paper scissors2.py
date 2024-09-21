import time
import random

print('Welcome to Rock, Paper, Scissors!')

time.sleep(1)

userScore = 0
cpuScore = 0

# Main Game loop
while True: 
 allChoices = ['Rock','Paper','Scissors']
 
 # User input to lowercase allowing for various capitalized or uncapitalized inputs. Also shows scores every round.
 userChoice = str.lower(input(f'(Current scores: Cpu: {cpuScore} User: {userScore}) Play your turn or type "P" for pause menu: '))

 # Similar thing for cpuChoice. CPU chooses a random item from allChoices.
 cpuChoice = str.lower(random.choice(allChoices))
 
 result = ''
 
 # Outcome for a draw.
 if cpuChoice == userChoice:
     result = 'draw'

 # Outcome if user has chosen paper.
 elif userChoice == 'paper':
     if cpuChoice == 'rock':
         result = 'win'
         
     else:
         result = 'lose'
         
 # Outcome if user has chosen scissors.        
 elif userChoice == 'scissors':
     if cpuChoice == 'paper':
         result = 'win'
         
     else:
         result = 'lose'
         
 # Outcome if user has chosen rock.       
 elif userChoice == 'rock':
     if cpuChoice == 'scissors':
         result = 'win'
         
     else:
         result = 'lose'
    
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
     print('Wrong input! Please choose between "Rock, Paper, Scissors".')
     
 # Shows what the CPU chose.    
 if result != '':
     print(f'CPU chose {cpuChoice}.')
     
     # Slight delay in all outcomes to allow the user to read the text.
     time.sleep(1.5)

 # Results and score changes.    
 if result == 'draw':
     print(f'Both you and the CPU chose {userChoice}. It is a draw!')
     
 elif result == 'win':
     userScore += 1

     print('You win!')
     
 elif result == 'lose':
     cpuScore += 1
     
     print('CPU win!')