rows=int(input("Enter number of rows: "))
cols=int(input("Enter number of columns: "))
center=input("Do you want items to be centered? (true/false): ")
headings=[]
print("\nEnter the data for each cell respectively!")
file = open("table.md", "w")
print("Let's Generate a Table in Markdown Syntax:\n")

for i in range(1, cols+1):
    value=input(f"Enter Heading for column{i} : ")
    if i==cols:
        entry= f"| {value} |\n"
        headings.append(value)
    else:
        entry= f"| {value} "
        headings.append(value)
    file.write(entry)
print("Headings Received!")

for i in range(0, cols):
    if i==cols-1:
        if center=="true" and len(headings[i])>2:
            entry= f"| :{'-'*(len(headings[i])-2)}: |\n"
        else:
            entry= f"| {'-'*len(headings[i])} |\n"
    else:
        if center=="true" and len(headings[i])>2:
            entry= f"| :{'-'*(len(headings[i])-2)}: "
        else:
            entry= f"| {'-'*len(headings[i])} "
    file.write(entry)
print("Done!")

for i in range(2, rows+1):
    print(f"\nEnter data for Row{i} : ")
    for j in range(1, cols+1):
        value=input(f"Row{i} Column{j} - {headings[j-2]}: ")
        if j==cols:
            entry= f"| {value} |\n"
            file.write(entry)
        else:
            entry= f"| {value} "
            file.write(entry)
print("\nDone Succesfully! :)")
print("Now check table.md or run 'cat table.md' in terminal to copy the syntax.\n")
file.close()
