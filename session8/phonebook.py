number_of_entries=int(input("Enter number of entries: "))
print("Enter the Names and Numbers respectively!")
file = open("numbers.txt", "w")

for i in range(0, number_of_entries):
    name=input("Name: ")
    number=input("Number: ")
    entry= f"{name}: {number}\n"
    file.write(entry)
    if i==(number_of_entries -1):
        print("Done!")
    else:
        print("Okay next one!")

file.close()
