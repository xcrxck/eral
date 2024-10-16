import os
import keyboard
import random


DIR_NAME = "generated_files"


if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)


def create_files():
    while True:
        main_input = str.lower(input('Enter the number of files you want to create (or type "p" for pause menu): '))
        if main_input != 'p' and main_input != 'pause':
            try:
                file_components = ['a','b','c','d','e','f','g','h','j','k','l','m']
                for i in range(1, int(main_input) + 1):
                    file_path = os.path.join(DIR_NAME, f'file_{i}.txt')
                    with open(file_path, 'a') as junk_file:
                        for j in range(1, 1000000):
                            junk_file.write(random.choice([str.lower, str.upper])(random.choice(file_components)))
                print(f"{main_input} files created successfully.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            pause_menu()
            break


def delete_files():
    if len(os.listdir(DIR_NAME)) != 0:
        for file in os.listdir(DIR_NAME):
            file_path = os.path.join(DIR_NAME, file)
            os.remove(file_path)
        print("All files deleted successfully.")
    else:
        print("No files to delete.")
  

def pause_menu():
    print('Press "d" to delete all files or press "esc" to quit else press "backspace" to continue')
    keyboard.on_press_key('d', lambda event: delete_files())
    keyboard.on_press_key('esc', lambda event: quit())
    keyboard.on_press_key('backspace', lambda event: create_files())
    keyboard.wait('esc', 'backspace', 'd')


create_files()