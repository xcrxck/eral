# Function for creating new ids
import time

import os

print('Welcome to the grand ID library!')
time.sleep(1)

def dict_entry(firstName, lastName, date, occupation, father, place):
    global new_id
    new_id = {
        'First name' : firstName,
        'Last name' : lastName,
        'Date of birth' : date,
        'Occupation' : occupation,
        "Fathers' name" : father,
        'Place of birth' : place
    }
    return new_id

data = {
   'id_Albert Einstein' :
        dict_entry('Albert', 'Einstein', '1257/12/23', 'Physicist', 'Hermann', 'Ulm, Germany'),
    
   'id_Socrates' : 
        dict_entry('Socrates', 'Greekisson', '1/1/1', 'Philosopher', 'Sophroniscus', 'Athens, Greece'),
    
   'id_Mohammad Ebrahimi' : 
        dict_entry('Mohammad', 'Ebrahimi', '1384/09/16', 'Programmer', 'Mohammad Sr.', 'Atlanta, US state of Georgia'),

    'id_Niels Bohr' : 
        dict_entry('Niels', 'Bohr', '1264/07/15', 'Physicist', 'Christian', 'Copenhagen, Denmark'),
    
    'id_ the Rock':
        dict_entry('Dwayne', 'Johnson', '1351/02/12', 'Actor and Wrestler', 'Rocky', 'Hayward, US state of California'),
    
    'id_ Barack Obama':
        dict_entry('Barack', 'Obama', '1340/05/13', 'Politician, 44th US president', 'Barack Sr.', 'Honolulu, US state of Hawaii'),
    
    'id_ Ali Khamenei':
        dict_entry('Ali', 'Khamenei', '1318/01/29', 'Politician, Shia marja, 2nd Supreme Leader of Iran' , 'Javad', 'Mashhad, Khorasan, Iran')
}
filterEntry = int(input('Type which filter you want to use \n(1 = First names\n2 = Last names\n3 = Dates of birth\n4 = Occupations\n5 = Father names\n6 = Places of birth): '))

searchFilter = ''

filterKeys = ['first names', 'last names', 'dates of birth', 'occupations', 'father names', 'places of birth']

for filter in range(0,6): # Loop for filters
    
    if filterEntry-1 == filter:
        
        filterIndex = filterKeys[filterEntry-1]
        
        searchFilter = str.lower(input(f'Search among {filterIndex}: '))

os.system('cls')
     
for id in list(data.values()): # Loop for id detection 
    
    detect = str.lower(list(id.values())[filterEntry-1])
    
    if searchFilter in detect:
        print('-------------')
        
        dotNumber = 1
        end = 0
        
        while True: # Fake loading time
            print('Searching for the closest match'+ '.'*dotNumber,'  ', end='\r')
            
            time.sleep(0.5)
            
            dotNumber += 1
            
            end += 1
            
            if dotNumber == 3+1:
                dotNumber = 1
               
            if end == 6: # Has to be dividable by 3 (3, 6, 9, ...) so it ends with 3 dots
                break

        idKeysIndex = 0 
         
        for idValue in id.values(): # Loop for showing the id(s)
            print(f'{list(new_id)[idKeysIndex]} : {idValue}                       ') # Extra space to overwrite the previous print
            
            idKeysIndex += 1 