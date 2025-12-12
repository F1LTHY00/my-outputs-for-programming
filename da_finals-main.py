from da_finals import *
import os 
import time, sys 

os.system('cls')


print('\nWelcome to LEARNING PYTHON')
print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
print('LET US START THE PROGRAM\nBUT FIRST, PLEASE TELL ME YOUR NAME')
n = input('What Is Your Name? ').upper()

answer = input(f'\nHello {n}, Are You Ready To Start Learning? (Y/N) ').lower()

if answer == 'y':
    os.system('cls')
    print('LET US NOW START !')
    time.sleep(1)
    for i in range(11):
        bar = "█" * i + '-' * (10-i)
        sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
        sys.stdout.flush()
        time.sleep(0.2)
    os.system('cls')

while True: 
    if answer == 'y':
        menu()
        choice = input('Please Select A Topic Of Your Choice--> ')
    
        if choice == '1':
            os.system('cls')
            printmenu()
            continue
        elif choice == '2':
            os.system('cls')
            variablesmenu()
            continue
        elif choice == '3':
            os.system('cls')
            operatorsmenu()
            continue
        elif choice == '4':
            os.system('cls')
            conditionalmenu()
            continue
        elif choice == '5':
            os.system('cls')
            loopmenu()
            continue
        elif choice == '6':
            os.system('cls')
            functionmenu()
            continue
        elif choice == '0': 
            time.sleep(0.5)
            print('\nThank You For Using This Program!')
            time.sleep(0.5)
            print('YOU DID GREAT!')
            time.sleep(0.5)
            print('Exiting Program....')
            time.sleep(0.5)
            break
        else:
            print('Invalid Option, Please Try Again')
            continue
    
    elif answer == 'n':
        print(f'Thank You For Opening The Program, {n}')
        break
        
    
    else: 
        print('Invalid Input, Please Try Again')