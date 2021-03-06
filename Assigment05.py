# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ALanger,7.29.21,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants

objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

f = open(objFile, "r")
for row in f:
    if row != "":
        lstRow = row.split(":")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
        lstTable.append(dicRow)
f.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Here is what is currently in the table:\n")
        if len(lstTable) != 0:
            for row in lstTable:
                print(row["Task"] + ": priority " + row["Priority"])
        else:
            print("There is currently nothing in the table.")
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        task = input("Please enter a new task: ")
        priority = input("Please enter a priority for this task: ")
        dicRow = {"Task": task, "Priority": priority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        choice = input("Please enter the task you would like to remove: ")
        for i in range(len(lstTable)):
            if lstTable[i]["Task"] == choice.lower():
                del lstTable[i]
                print(choice + " has been deleted from the table.")
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        print("Saving tasks to the file...")
        f = open(objFile, "w")
        for row in lstTable:
            f.write(row["Task"] + ":" + row["Priority"])
        print("All saved!")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        input("Press enter to exit the program")
        break  # and Exit the program
