age=int(input("Enter your age:"))

if 10<age<20:
    print("Permission Granted")
if age>20:
    id=input("Do you have verified id, Yes or No:")
    if id=="Yes":
        print("Permission Granted")
    else:
        print("Permission Denied")
    
