import os 
import time
import sys

def menu():
        os.system('cls')
        print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.
                    \n\t\t"HERE IS THE MAIN MENU"                        

            1. Print Statements
            2. Variable
            3. Operators
            4. Conditional Statements
            5. Loops
            6. Functions
            0. Exit                       
                                   
.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.                  
                                            ''')





#This is for printing statements
def printmenu():
    while True: 
        print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
        print('1. Basic Printing')
        print('2. Definition')
        print('3. Create your own code')
        print('0. Back To Main Menu')
        print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
        option = input('Enter The Option You Want To Proceed With--> ')
        
        
        if option == '1':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('INPUT: \nprint("Hello, World") \nprint("Sir Mesiera  is the best teacher")')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('OUTPUT: \nHello World \nSir Mesiera  is the best teacher')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            
        
        elif option == '2':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''The main purpose of printing in programming is to show 
information to the user or for troubleshooting. It's 
enables programmers to view the results of their code, which 
can include variables, text, or other kinds of data. This is 
vital for comprehending the operation of a program
and to troubleshoot problems.''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
        
        elif option == '3':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue

        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break
        
        else: 
            print('Invalid Option, Please Try Again')



#for variables
def variablesmenu():
    while True:
        print('1. Using of Len \n(Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('4. Create your own code')
        print('0. Back To Main Menu')

        option = input('Enter The Option You Want To Proceed With--> ')
        
        
        if option == '1':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            import activity4
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
     
        elif option == '2':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('\n EXPLANATION FOR STATEMENTS')
            print('name = input ("type your name here --> "')
            print('print ("Your name has ", len(name), "characters")')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
    
        
        elif option == '3':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''Variables are symbolic names that reference objects. 
They are created by assigning a value to a name using the equals sign (=).
len() tells you "how many items are inside" a given object.
''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
        
        elif option == '4':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue
        
        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#FOR OPERATORS
def operatorsmenu():
    while True:
        print('1. Operators (Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('4. Create your own code')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
       
        if option == '1':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            import activity6
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
       
       
        elif option == '2':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''n1 = eval(input("Enter the first number : "))
n2 = eval(input("Enter the second number : "))
s = n1 + n2
a = n1 - n2
m = n1 * n2
b = n1 / n2
print("\nThe sum of",n1,"and",n2,"is",s)
print("The difference of",n1,"and",n2,"is",a)
print("The product of",n1,"and",n2,"is",m)
print("The qoutient of",n1,"and",n2,"is",b)
print(n1, "exponent by",n2,"is",n1**n2)
print("The remainder of",n1,"and",n2,"is",n1 % n2)
print("The floor division of",n1,"and",n2,"is",n1//n2)''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
    
       
        elif option == '3':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''Operators are special symbols that perform operations on variables and values. \nThey are essential for performing arithmetic, logical, comparison, and other operations. ''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
        
        elif option == '4':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue
        
        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break
        
        else: 
            print('Invalid Option Please Try Again')



#FOR CONDITIONAL STATEMENTS
def conditionalmenu():
    while True:
        print('1. Conditional Statement (Try An Example)')
        print('2. Explanation')
        print('3. Definition')
        print('4. Create your own code')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
      
        if option == '1':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            import Activity10
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            continue
       
       
        elif option == '2':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''print ("Enter your Username -->")
Username = input()

print ("Enter your Password -->")
Password = input ()

if (Username == 'F1LTHY00') and (Password == 'pbcalbum00'):
		print ("Login Successful")


if (Username != 'F1LTHY00') and (Password != 'pbcalbum00'):
		print ("Login Failed")''')
        
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
    
        
        elif option == '3':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''Conditional statements are used to make decisions in your program — 
they allow you to execute certain blocks of code only if specific conditions are met. 
This use if, elif, and else for creating conditions for each variables and statements. ''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
        
        elif option == '4':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue
      
        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break
        
        else: 
            print('Invalid Option Please Try Again')


#FOR LOOPS
def loopmenu():
    while True:
        print('1. For Loops')
        print('2. While Loops')
        print('3. Nested For Loops')
        print('4. Nested While Loop')
        print('5. Explanation')
        print('6. Definition')
        print('7. Create your own code')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')
        
    
        if option == '1':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            
            for i in range(10):
                print(i)

            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
       
    
        if option == '2':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            i = 1
            while i <= 3:
                print(i)
                i += 2
            else:
                print("Loop ended")            
            
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
        
       
        if option == '3':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            for i in range(21, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue

        if option == '4':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            rows = 5
            i = 1
            while i <= rows:
                j = 1
                while j <= i:
                    print("*", end=" ")
                    j += 1
                    print()   
                    i += 1
                    print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
                    print(' ')
                    print(' ')
                    break


 
        elif option == '5':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('FOR LOOP')
            
            print('''            for i in range(10):
                print(i) ''')
            
            print('WHILE LOOP')
            
            print('''            i = 1
            while i <= 3:
                print(i)
                i += 2
            else:
                print("Loop ended")      ''')

            print('NESTED FOR LOOP')
            
            print('''            for i in range(21, 1, -1):
                for x in range(1, i, 1):
                    print("*", end=" ")
                print()   ''')
            
            print('NESTED WHILE LOOP')
            print(''' rows = 5
            i = 1
            while i <= rows:
                j = 1
                while j <= i:
                    print("*", end=" ")
                    j += 1
                    print()   
                    i += 1''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
    
        
        elif option == '6':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''Loops in Python are constructs used to execute a block of code repeatedly, 
either for a fixed number of iterations or until a specific condition is met. 
They are essential for automating repetitive tasks and improving code efficiency.''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue
        
        elif option == '7':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue

        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break
        
        else: 
            print('Invalid Option Please Try Again')
#FOR FUNCTIONS
def functionmenu():
    while True:
        print('1. Functions')
        print('2. Explanation')
        print('3. Definition')
        print('4. Create your own code')
        print('0. Back To Main Menu')
     
        option = input('Enter The Option You Want To Proceed With--> ')    

       
        if option == '1':
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            import activity11
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
        elif option == '2':
            print(''' temp = eval(input("What is the temp right now: "))

if temp >= 1 and temp <= 15:
    print ("Temp is considered as extremely cold")
elif temp >= 16 and temp <= 30:
    print ("Cold temperatures")
elif temp >= 31 and temp <= 38:
    print ("Lukewarm temperatures")
elif temp >= 39 and temp <= 42:
    print ("Warm temperatures")
elif temp >= 43 and temp <= 50:
    print ("Hot temperatures")
elif temp >= 51 and temp <= 60:
    print ("Extremely hot temperatures")
elif temp >= 61:
    print ("Burning temperatures")

else: 
    print ("Invalid temperatures")''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
       
        
        elif option == '3':
            os.system('cls')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print('''A function is a block of reusable code that performs a specific task and only runs when it is called.
 ''')
            print('''.-.. . --- -. .- .-. -.. -... . ... - - . .- -.-. .... . .-.''')
            print(' ')
            print(' ')
            continue

        elif option == '4':
            os.system('cls')
            lines = []
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)

            user_input = "\n".join(lines)
            exec(user_input) 
            time.sleep(1)
            continue
        
        
        elif option == '0':
            print('Returning.....')
            for i in range(11):
                bar = "█" * i + '-' * (10-i)
                sys.stdout.write(f'\rLoading: [{bar}] {i*10}%')
                sys.stdout.flush()
                time.sleep(0.2)
            break