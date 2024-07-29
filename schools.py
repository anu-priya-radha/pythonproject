while True :
    print("""
        Please select your options below :
            1) Student Details
            2) Teacher Details
            3) Exit
    """)
    choice = int(input("Enter your Choices : "))

    if choice == 1:
            print("")
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            mark = int(input("Enter student mark: "))
            if(age>20):
                  print(f"{name} not a student")
            else:
                  print(f"{name} is a student")
            if(mark>=80):
                  print(f"{name} Got a grade A")
            elif(mark<=80 and mark>=60):
                   print(f"{name} Got a grade B")
            elif(mark>=50 and mark<=60):
                   print(f"{name} Got a grade C")
            else:
                  print("Fail")
            break

                
    if choice == 2:
            print("")
            name = input("Enter Teacher name: ")
            age = int(input("Enter the Teacher age:"))
            subject = str(input("Enter the subject:"))
            if(age<20):
                  print(f"{name} not a Teacher")
            else:
                  print(f"{name} is a Teacher")
            if(subject=="Maths"):
                  print(f"{name} is a Maths Teacher")
            elif(subject=="Science"):
                  print(f"{name} is a Science Teacher")
            elif(subject=="Englis"):
                  print(f"{name} is a English Teacher")
            else:
                  print("Not Subject Found")
    elif (choice == 3) :
        print("Program Successfully Executed")
        break
    else :
        print("Invalid Choice")


          
        