print("SM EMPLOYEES INFORMATION")
print("====================================")

employee_record = {} #empty

while True:
    print("SELECT FORM THE FOLLOWING OPTION")
    print("A - adding employee record ")
    print("B - search employee ")
    print("C - edit employee record ")
    print("D - print all record ")
    print("E - expord data ")
    print("F - exit system")
    
    choice = input("Input your choice ---> ").lower().strip()
    
    if choice == 'a':
        print("ADD EMPLOYEE RECORD")
        employee_position = input("input employee position ")
        first_name = input("input first name ")
        last_name = input("input last name ")
        age = input("input age ")
        house_address = input("input house address" )
        email = input("Input email ")
        #transfering input to a dictionary
        employee_record[employee_position] = [first_name, last_name, age, house_address, email ]
        print("DATA SAVE SUCCESSFULLY")
        
        if choice == 'b':
            print("SEARCH STUDENT")
            employee_position = input("input emloyee position: ")
            if employee_position in employee_record:
                print(employee_record[employee_position])
                else:
                    print("Record not found")
                continue
        
        elif choice == 'c':
            print("EDIT STUDENT RECORD")
            employee_position = input("input employee position: ")
            first_name = input("input first name: ")
            last_name = input("input last name: ")
            age = input("input age: ")
            house_address = input("input house address: ")
            email = input("input email: ")
            employee_record[employee_position] = [first_name, last_name, age, house address, email ]
            print("Record Updated")
            continue
            
            

    
