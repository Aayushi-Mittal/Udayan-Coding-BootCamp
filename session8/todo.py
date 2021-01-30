todo_list=[]
done=[]
file = open("todo.md", "w")

print("******** TO-DO LIST! *********")
print("Press 1: To create a todo")
print("Press 2: To delete a todo")
print("Press 3: To display todo list")
print("Press 4: To Mark as done")
print("Press 5: Quit")
ch=input("Enter your choice: ")

while True:
    if ch=="1":
        print("\nEnter q to exit")
        while True:
            todo=input("Enter a todo: ")
            if todo=="q":
                break
            todo_list.append(todo)
            done.append("n")
    elif ch=="2":
        for i in range(0, len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")
        delete=int(input("Enter the position of todo you want to delete: "))
        todo_list.remove(todo_list[delete-1])
        done.remove(done[delete-1])
    elif ch=="3":
        print("****** DISPLAYING TO-DO LIST ******")
        for i in range(0, len(todo_list)):
            if done[i]=="y":
                print(f"{i+1}. {todo_list[i]} ✔")
            else:
                print(f"{i+1}. {todo_list[i]}")
    elif ch=="4":
        print("****** DISPLAYING TO-DO LIST ******")
        print("Press 'y' to mark as done otherwise press 'n'.")
        for i in range(0, len(todo_list)):
            print(f"{i+1}. {todo_list[i]}")
            done[i]=input(f"Mark todo-{i+1} as done? ")
    elif ch=="5":
        break
    else:
        print("Invalid input! Press: 1,2,3,4 or 5")
    ch=input("\nEnter your choice: ")
            
for i in range(0, len(todo_list)):
    if done[i]=="y":
        entry= f"{i+1}. ~~{todo_list[i]}~~\n"
    else:
        entry= f"{i+1}. {todo_list[i]}\n"
    file.write(entry)
print("Contents printed successfully!\n")

file.close()
