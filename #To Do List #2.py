#To Do List #2
#Calissa Stevens


#Initialize


ToDo = ["milk", "cream", "butter", "sugar", "eggs", "apples"]


#Functions
def Quit():
    print("Thank you for using this digital To-Do list :)")


def FullList():
    print("Welcome to you digital to do list!")
    def RunAgain():
        print("Please choose what you would like to do next.")
        print("Type in a number between 1 and 5")
        print("1. Add a task \n2. View current to do list \n3. Mark a task as completed \n4. Remove a task from the list \n5. Exit the program \n6.Remove all tasks from list \n7. Sort the list alphabetically \n8.Count the number of items on the list")
        option = int(input("Please type the number here: "))




        if(option == 1):
            item = input("Please add your task: ")
            ToDo.append(item)
            print(ToDo)
            RunAgain()
        
        if(option == 2):
            print(ToDo)
            RunAgain()
            
        if(option == 3):
            print(ToDo)
            ans = input("select an item from the list to mark as done: ")
            i = ToDo.index(ans)
            ToDo[i] = ans + " X"
            print(ToDo)
            RunAgain()


        if(option == 4):
            RemoveItem = input("what item would you like to remove: ")
            ToDo.remove(RemoveItem)
            print(ToDo)
            RunAgain()


            
        if(option == 5):
            Quit()

        if(option == 6):
           ToDo.clear()
           print(ToDo)

        if(option == 7):
            ToDo.sort()
            print(ToDo)

        if(option == 8):
            count = ToDo.count(6)
            print(count)

    RunAgain()




#Main

FullList()

