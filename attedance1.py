import datetime

def read_student_names(file_path):
    with open(file_path, 'r') as file:
        student_names = file.readlines()
        student_names = [name.strip() for name in student_names]
    return student_names

def attendance(file_path):
    student_names = read_student_names(file_path)
    aa = True
    lev = [] 
    ab1 = []
    while aa:
        print("\t\t\t\tATENDANCE TRACKER\n")
        print("1. LEAVE")
        print("2. ON-DUTY")
        print("3. PRINT THE ATTENDANCE")
        print("4. EXIT")
        i = int(input("Enter your choice: "))
        a = True
        if i == 1:
            ab1 = []  # Move this line inside the if block
            while a:
                ab = int(input("Enter student number (or 0 to stop): "))
                if ab == 0:
                    a = False
                else:
                    ab1.append(student_names[ab - 1])
            print("Leave recorded:", ab1)

        elif i == 2:
            while a:
                ab = int(input("Enter student number (or 0 to stop): "))
                if ab == 0:
                    a = False
                else:
                    lev.append(student_names[ab - 1])  
            print("On-duty recorded:", lev)
        elif i == 3:
            # Generate attendance report
            date = datetime.datetime.now().strftime("%d.%m.%Y")
            l = len(ab1)  # Number of on-duty students
            p = len(student_names) - l  # Number of present students
            total_students = len(student_names)
            attendance_percentage = (p / total_students) * 100

            a1 = 'Good Morning Sir, Today Attendance\n'
            a2 = f'''\nClass: II- B.Tech (CSBS)\n

Total Strength: {total_students}'''
            a3 = f'''\n
- No. of Present: {p}
- No. of Absent: {l}

'''
            # Print the attendance report
            print(a1)
            print("Date:", date)
            print(a2)
            print(a3)
            print("Absentees:\n")
            for x in range(len(ab1)):
                print("\t\t",x+1,". ",ab1[x])
            print("\nOn-duty Students:")
            for x in range(len(lev)):
                print("\t\t",x+1,". ",lev[x])

            print(f"\n\nPercentage: {attendance_percentage:.2f}%")

            print("\n Thank you Sir.")
            aa = False
        else:
            print("Invalid choice. Please try again.")

file_path = "C:\\Users\\Sathishkumar\\Downloads\\CSBS.txt"
attendance(file_path)
