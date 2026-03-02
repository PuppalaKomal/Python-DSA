attendence={}
def show_menu():
    print("Attendence tracking system")
    print("1. Add attendence")
    print("2. View attendence")
    print("Exit")
def add_attendence():
    name=input("Enter name: ")
    status=input("Enter status: ")
    attendence[name]=status
    print("Attendence is  added")
def view_attendence():
    print("Name\tStatus")
    for name,status in attendence.items():
        print(name,"\t",status)
def main():            
    while True:
        show_menu()
        choice=input("Enter your choice: ")
        if choice=="1":
            add_attendence()
        elif choice=="2":
            view_attendence()
        elif choice=="3":
            break
        else:
            print("Invalid choice")
main()
