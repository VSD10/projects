print('TO-DO LIST')
b=[]
while True:
    print("1.TO VIEW YOUR TASK\n2.TO ADD YOUR TASK\n3.TO DELETE YOUR TASK")
    a=int(input("Your choice::"))
    if a==1:
        if len(b)==0:
            print("NO TASK")
        else:
            print("\n\t\t\t\t\tYOUR TASKS")
            for x in range(len(b)):
                print('\n\t\t\t',x+1,".",b[x])
    elif a==2:
        a2=input("ENTER YOUR TASK:")
        b.append(a2)
        print("\t\t\tYOUR TASK ADDED SUCCESFULLY!!!")
    elif a==3:
            print("\n\t\t\t\t\tYOUR TASKS")
            for x in range(len(b)):
                print('\n\t\t\t',x+1,".",b[x])

            print("ENTER THE TASK TO DELETE::")
            d=int(input("enter here:"))
            b.remove(b[d-1])
            print('TASK REMOVED SUCCESSFULLY!!!')
    print("\n\nwould you like to continue?\n1.Yes\t2.No")
    r=int(input("enter here::"))
    if r==1:
        continue
    else:
        break




