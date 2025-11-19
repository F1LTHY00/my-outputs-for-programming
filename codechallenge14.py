import os
import json

os.system('cls')
print("student information system")
print("==========================")

student_record = {}

while True:
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORD")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - EXIT SYSTEM")

    choice = input("SELECT FORM THE OPTIONS ABOVE....   ").lower()

    if choice == 'a':
        os.system('cls')
        print("\nADDING STUDENT RECORD")

        ID_no = input('PLEASE INPUT STUDENT ID NUMBER:  ')
        first = input('PLEASE INPUT STUDENT FIRST NAME:  ').upper()
        last = input('PLEASE INPUT STUDENT LAST NAME:  ').upper()
        age = input('PLEASE INPUT STUDENT AGE:  ')
        sec = input('PLEASE INPUT STUDENT SECTION:  ').upper()
        cou = input('PLEASE INPUT STUDENT COURSE:  ').upper()
        
        student_record[ID_no] = [first, last, age, sec, cou]

        print("SAVED SUCCESSFULLY")

        continue
    elif choice == 'b':
        os.system('cls')
        print('STUDENT PRINTING RECORD')
        
        for s, b in student_record.items ():
            print(f'STUDENT ID - {s}, INFORMATION {b}')
        continue 
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        
        search_ID = input ("PLEASE TYPE THE STUDENT ID YOU WANT TO SEARCH....   ").lower()

        for info in student_record.keys():
                if search_ID in student_record.keys():
                    print ("STUDENT FOUND")
                    print("==============================")
                    print(f"\nRECORD FOUND FOR ID NUMBER {search_ID}")
                    
                    for s in student_record[search_ID]:
                        print(f" ----- {s}")
                    print ("=========================")
                else:
                    print("STUDENT DOES NOT EXIST")
                break
        continue 
    elif choice == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")
        
        search_ID = input ("PLEASE TYPE THE STUDENT ID YOU WANT TO SEARCH....   ").lower()

        for info in student_record.keys():
                if search_ID in student_record.keys():
                    print ("STUDENT FOUND")
                    print("==============================")
                    print(f"\nRECORD FOUND FOR ID NUMBER {search_ID}")
                    
                    for s in student_record[search_ID]:
                        print(f" ----- {s}")
                    print ("=========================")

                    student_record.pop(search_ID)
                    print("STUDENT RECORD DELETED")
                else:
                    print("STUDENT DOES NOT EXIST")
                break
        continue 
    elif choice == 'e':
         os.system('cls')
         print("EDIT STUDENT RECORD")
        
         search_ID = input ("PLEASE TYPE THE STUDENT ID YOU WANT TO SEARCH....   ").lower()

         for info in student_record.keys():
                if search_ID in student_record.keys():
                    print ("STUDENT FOUND")
                    print("==============================")
                    print(f"\nRECORD FOUND FOR ID NUMBER {search_ID}")
                    
                    for s in student_record[search_ID]:
                        print(f" ----- {s}")
                    print ("=========================")

                    
                    first = input('PLEASE INPUT STUDENT FIRST NAME:  ').upper()
                    last = input('PLEASE INPUT STUDENT LAST NAME:  ').upper()
                    age = eval(input('PLEASE INPUT STUDENT AGE:  '))
                    sec = input('PLEASE INPUT STUDENT SECTION:  ').upper()
                    cou = input('PLEASE INPUT STUDENT COURSE:  ').upper()

                    student_record[search_ID][0] = first
                    student_record[search_ID][1] = last
                    student_record[search_ID][2] = age
                    student_record[search_ID][3] = sec
                    student_record[search_ID][4] = cou
                    print("=============================")
                    
                    print("DATA UPDATED")
        
                else:
                    print("STUDENT DOES NOT EXIST")
                break
            
         continue 
    elif choice == 'f':

        os.system('cls')
        print("EXPORT STUDENT DATA")
        print("========================")

        with open('RECORDS.json', 'w') as new_file:
             json.dump(student_record, new_file, indent = 4)

             print("DATA EXPORTED TO RECORDS.json")


        continue 
    elif choice == 'g':
        print("SYSTEM EXIT")
        break  
    else:
        print('INVALID CHOICE. PLEASE SELECT AGAIN.')