import datetime

# List of student names
student_names = [
    "ARTHI S",
    "ADITHIYA D",
    "AKKSHETHA M",
    "ARAVINDRAJ G",
    "ARUNACHALESHWARAN A",
    "ANUSRI S",
    "BARATHI K",
    "BATHRINATH K",
    "DEEPAN R",
    "DHANUSH K R",
    "DHARSHAN V S",
    "DIVAKAR T",
    "GAYATHRI R",
    "GAYATHRI DEVI S",
    "GIRIDASS S",
    "GOPIKA S",
    "GOWMITHA R",
    "HARI KRISHNAN V",
    "HARSHINI K",
    "HEMAPRIYAA S",
    "JAYAVARSHAN SS",
    "KABILAN S",
    "KAMALI S",
    "KRISHNAPRASATH B",
    "LOGESWARAN P V",
    "MADHU VARSHA P",
    "MALAVICKA V",
    "MANIKANDAN R",
    "MOHAMMED RASIQUE S A",
    "NAVEEN KUMAR M",
    "NIRNAJAN S",
    "NITHYA SHREE S",
    "PAVITHRA N",
    "POJASHREE V",
    "PRAGATHI C",
    "PREETHIKA S V",
    "PRIYADHARSHAN D S",
    "RAMANAN A S",
    "RAVEENA K",
    "RISHWANTH ADISHWAR K",
    "SABRANA K",
    "SACHIN V",
    "SAMIHA M",
    "SANJANA S P",
    "SASHVINA F",
    "SASIDHARAN B",
    "SHOBIKA S",
    "SHYAM SUNDAR K",
    "SRIRAM P",
    "SUMITHA S",
    "SURENDAR P",
    "SWAPNA D P",
    "UMA NANDHINI M",
    "VAISHNAVI V",
    "VASUDEVAN M",
    "NAVIN KUMAR M",
    "PRADEEP M",
    "PRADIBA A S",
    "SANTHOSH KUMAR S"
]

def attendance():
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
            ab1 = []
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

            a1 = '\n\n\nGood Morning Sir, Today Attendance\n'
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
        elif i == 4:
            aa = False
        else:
            print("Invalid choice. Please try again.")

attendance()