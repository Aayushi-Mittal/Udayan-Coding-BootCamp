todo_list=[]
file = open("todo.txt", "w")
1
print("******** TO-DO LIST! *********")
print("Press 1: To create a todo")
print("Press 2: To delete a todo")
print("Press 3: To display todo list")
print("Press 4: Quit")
ch=input("Enter your choice: ")

while ch!="4":
    if ch=="1":
        todo=input("Enter a todo: ")
        todo_list.append(todo)
    elif ch=="2":
        delete=int(input("Enter the position of todo you want to delete: "))
        todo_list.remove(todo_list[delete-1])
    elif ch=="3":
        print("****** DISPLAYING TO-DO LIST ******")
        for i in range(0, len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")
    ch=input("\nEnter your choice: ")
            
for i in range(0, len(todo_list)):
    entry= f"{i+1}. {todo_list[i]}\n"
    file.write(entry)
print("Contents printed successfully!\n")

file.close()