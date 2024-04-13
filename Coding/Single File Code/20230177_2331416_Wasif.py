import random


def add_horse(total_horse_details):
    
    # Creating Local Variable 
    Group_A_count = 0
    Group_B_count = 0
    Group_C_count = 0
    Group_D_count = 0

    # Counting how Many Horses in the Group
    for horse in (total_horse_details):

        if (horse['group']=="A"):
            Group_A_count+=1

        if (horse['group']=="B"):
            Group_B_count+=1
        
        if (horse['group']=="C"):
            Group_C_count+=1

        if (horse['group']=="D"):
                Group_D_count+=1
    

    #Seting a limit for totel horses 
    if len(total_horse_details)<20:

        # Getting Horse id , validating and Duplication handling 
        while True:
            horse_id = input("\nEnter Horse ID: ")
            if horse_id.isdigit():
                for horse in total_horse_details:
                    if horse['horse_id']== horse_id:
                        print("\nId is already there\n")
                        break
                else:
                    break
            else:
                print("\nInvalid input. Horse ID must be an integer.")
    
        
        # Validating Horse Name as Alphabetic
        while True:
            horse_name = input("Enter Horse Name: ")
            if  horse_name.isalpha():
                break
            else:
                print("\nInvalid input. Horse Name must contain only alphabetic characters.\n")


        # Validating Jockey Name as Alphabetic
        while True:
            jockey_name = input("Enter Jockey Name: ")
            if  jockey_name.isalpha():
                break
            else:
                print("\nInvalid input. Jockey Name must contain only alphabetic characters.\n")


        # Validating Age as Integer
        while True:
            age = input("Enter Age: ")
            if age.isdigit():
                break
            else:
                print("\nInvalid input. Age must be an integer.\n")


        # Validating Breed Name as Alphabetic
        while True:
            breed = input("Enter Breed: ")
            if  breed.isalpha():
                break
            else:
                print("\nInvalid input. Breed must contain only alphabetic characters.\n")


        # Asking for race Record
        while True:
            Wins = input("Enter How Many Wins: ")
            Total_Races = input("Enter How Many Matches: ")
            if  Wins.isdigit() and Total_Races.isdigit():
                if (int(Wins)<=int(Total_Races)):
                    break
                else:
                    print ("\nWins Can't be higher than Totel Races")
                    continue
            else:
                print("\nInvalid input. Wins and Races must be an integer\n")
        
        race_record =f"{Wins} Wins in {Total_Races} races"


        # Checking availabily for groups and adding horse for each group 
        # If the Group is full You can Add to Other Groups
        while True:

            group = str(input("Enter Group (A, B, C, D): ")).upper()

            horse = {'horse_id': horse_id, 'horse_name': horse_name, 'jockey_name': jockey_name,
                    'age': age, 'breed': breed, 'race_record': race_record, 'group': group}
            

            if (group == "A"):
                if Group_A_count < 5 :
                    total_horse_details.append(horse)
                    print("\nHorse details Added Successfully ")
                    break
                else:
                    print("\nA is full\n")
                
            elif (group == "B"):
                if Group_B_count < 5:
                    total_horse_details.append(horse)
                    print("\nHorse details Added Successfully ")
                    break
                else:
                    print("\nB is full\n")

            elif (group == "C"):
                if Group_C_count < 5:
                    total_horse_details.append(horse)
                    print("\nHorse details Added Successfully")
                    break
                else:
                    print("\nC is full\n")
            
            elif (group == "D"):
                if Group_D_count <  5:
                    total_horse_details.append(horse)
                    print("\nHorse details Added Successfully ")
                    break
                else:
                    print("\nD is full\n")
            
            else:
                print("\nWroung Group Input")
    
    # If Limit is Reached You can add More Horses
    else:
        print("\nAlready There were Totaly 20 Horses. You can't add more. ")



def update_horse(total_horse_details):
    
    # Creating Local Variable 
    Group_A_count=0
    Group_B_count=0
    Group_C_count=0
    Group_D_count=0

    # Counting How many horses in each group
    for horse in (total_horse_details):

        if (horse['group']=="A"):
            Group_A_count+=1

        if (horse['group']=="B"):
            Group_B_count+=1
        
        if (horse['group']=="C"):
            Group_C_count+=1

        if (horse['group']=="D"):
            Group_D_count+=1


    # Asking and Validating The Horse Id
    while True:
        Update_horse_id = input("\nEnter Horse ID to update: ")
        if  Update_horse_id.isdigit():
                break
        else:
            print("\nInvalid input. Age must be an integer.\n")

    
    for horse in (total_horse_details):

        # Checking is there any horse With That Horse Id
        if horse['horse_id'] == Update_horse_id:

            print("Horse Deatils : ",horse)                      # User can View the Horse Deatails

            # Checking Which Group is Entered Horse Before Updating
            # This Part will Allow  User to Change the Group  
            if (horse['group']=="A") :
                Group_A_count-=1
            elif (horse['group']=="B"):
                Group_B_count-=1
            elif (horse['group']=="C"):
                Group_C_count-=1

            elif (horse['group']=="D"):
                Group_D_count-=1    
            
            
            # Validating Horse Name to be an Alphabetic
            while True:
                horse_name = input("\nEnter updated Horse Name: ")
                if  horse_name.isalpha():
                    break
                else:
                    print("\nInvalid input. Horse Name must contain only alphabetic characters.\n")

            # Validating Jockey Name to be an Alphabetic
            while True:
                jockey_name = input("Enter updated Jockey Name: ")
                if  jockey_name.isalpha():
                    break
                else:
                    print("\nInvalid input. Jockey Name must contain only alphabetic characters.\n")

            #  Validating Age as Integer
            while True:
                age = (input("Enter updated Age: "))
                if age.isdigit():
                    break
                else:
                    print("\nInvalid input. Age must be an integer.\n")

            # Validating Breed Name as Alphabetic
            while True:
                breed = (input("Enter updated Breed: "))
                if  breed.isalpha():
                    break
                else:
                    print("\nInvalid input. Breed must contain only alphabetic characters.\n")

            # Asking for race Record
            while True:
                Wins = input("Enter How Many Wins: ")
                Total_Races = input("Enter How Many Races: ")
                if  Wins.isdigit() and Total_Races.isdigit():
                    if (int(Wins)<=int(Total_Races)):
                        break
                    else:
                        print ("\nWins Can't be higher than Totel Races")
                        continue
                else:
                    print("\nInvalid input. Wins and Races must be an integer.\n")
        
            race_record =f"{Wins} Wins in {Total_Races} races"


            # Asking For Group
            # user can put in same Group or Any Other Available Groups 
            while True:
                group = str(input("Enter updated Group (A, B, C, D): ")).upper()

                if (group == "A"):
                    if Group_A_count < 5 :                             
                        Group_A_count = Group_A_count + 1
                        break
                    else:
                        print("\nA is full\n")

                elif (group == "B"):
                    if Group_B_count < 5 :
                        Group_B_count = Group_B_count + 1
                        break
                    else:
                        print("\nB is full\n ")

                elif (group == "C"):
                    if Group_C_count < 5 :
                        Group_C_count = Group_C_count + 1
                        break
                    else:
                        print("\nC is full\n ")

                elif (group == "D"):
                    if Group_D_count < 5 :
                        Group_D_count = Group_D_count + 1
                        break
                    else:
                        print("\nD is full\n ")

                else:
                    print("\nWroung Group Input\n")

            # Inserting Updated  Data
            horse['horse_name'] = horse_name
            horse['jockey_name'] = jockey_name
            horse['age'] = age
            horse['breed'] = breed
            horse['race_record'] = race_record
            horse['group'] = group
            print("\nHorse details updated successfully!")
            
            return
            
    #IF the Horse id is  wrong 
    print("Horse not found!")



def delete_horse(total_horse_details):

    # Asking and Validating The Horse Id
    while True:
        horse_id = input("\nEnter Horse ID to delete: ")
        if  horse_id.isdigit():
            break
        else:
            print("\nInvalid input. Age must be an integer.\n")


    for horse in (total_horse_details ):
        
         # Checking is there any horse With That Horse Id
        if horse['horse_id'] == horse_id:

            # Removing The Horse Deatils
            total_horse_details.remove(horse)
            print("\nHorse details deleted successfully.")
            return

    print("\nHorse not found!\n")



def view_horses(total_horse_details):
  
    for i in range(1, len(total_horse_details)):
        current_dict = total_horse_details[i]
        current_horse_id = int(current_dict["horse_id"])
        j = i - 1

        # Move elements of the sorted part that are greater than the current_horse_id
        # to one position ahead of their current position
        while j >= 0 and current_horse_id < int(total_horse_details[j]["horse_id"]):
            total_horse_details[j + 1] = total_horse_details[j]
            j -= 1

        # Insert the current_dict into the correct position in the sorted part
        total_horse_details[j + 1] = current_dict

    # Print the sorted list
    for horse in total_horse_details:
        print (horse)



def save_to_file(total_horse_details):

    #Local Variables
    Group_A_id = []
    Group_B_id = []
    Group_C_id = []
    Group_D_id = []

    Group_A = []
    Group_B = []
    Group_C = []
    Group_D = []

    # Appending Horse Deatails and Horse IDs to Lists 
    for horse in (total_horse_details):

        if (horse['group']=="A"):
            Group_A.append(horse)
            value=horse['horse_id']
            Group_A_id.append(value)

        elif (horse['group']=="B"):
            Group_B.append(horse)
            value=horse['horse_id']
            Group_B_id.append(value)

        elif (horse['group']=="C"):
            Group_C.append(horse)
            value=horse['horse_id']
            Group_C_id.append(value)

        elif (horse['group']=="D"):
            Group_D.append(horse)
            value=horse['horse_id']
            Group_D_id.append(value)
    
    # Saving horse deatils according to the group in one  Text file
    with open("horse_details.txt", "w") as file:
        
        file.write("Group A" + "\n") 
        for horse in (Group_A):
            file.write(str(horse) + "\n")
        
        file.write("\n"+"Group B" + "\n")
        for horse in (Group_B):
            file.write(str(horse) + "\n")
        
        file.write("\n"+"Group C" + "\n")
        for horse in (Group_C):
            file.write(str(horse) + "\n")
        
        file.write("\n"+"Group D" + "\n")
        for horse in (Group_D):
            file.write(str(horse) + "\n")


    # saving Horse IDs according to the group In Each Single file
    with open("Group_A_id.txt","w") as file:
        for horse_id in Group_A_id:
            file.write(str(horse_id) + "\n")
    
    with open("Group_B_id.txt","w") as file:
        for horse_id in Group_B_id:
            file.write(str(horse_id) + "\n")
    
    with open("Group_C_id.txt","w") as file:
        for horse_id in Group_C_id:
            file.write(str(horse_id) + "\n")

    with open("Group_D_id.txt","w") as file:
        for horse_id in Group_D_id:
            file.write(str(horse_id) + "\n")

    print ("\nSuccesfully  Saved")




def select_horses_for_race(total_horse_details,selected_horses):
    try:
        # Local Variable
        Group_A = []
        Group_B = []
        Group_C = []
        Group_D = []

        # Reading IDs from Saved File And appending Those into Local Groups
        with  open("Group_A_id.txt","r") as file_1:
            lines_1= file_1.readlines()
            for line in lines_1:
                removeing_enter=line.replace("\n","")
                Group_A.append(removeing_enter)

        with open("Group_B_id.txt","r") as file_2:
            lines_2= file_2.readlines()
            for line in lines_2:
                removeing_enter=line.replace("\n","")
                Group_B.append(removeing_enter)

        with open("Group_C_id.txt","r") as file_3:
            lines_3= file_3.readlines()
            for line in lines_3:
                removeing_enter=line.replace("\n","")
                Group_C.append(removeing_enter)

        with open("Group_D_id.txt","r") as file_4:
            lines_4= file_4.readlines()
            for line in lines_4:
                removeing_enter=line.replace("\n","")
                Group_D.append(removeing_enter)

        # Selecting One horse from each Group
        select_Group_A=random.choice(Group_A)
        select_Group_B=random.choice(Group_B)
        select_Group_C=random.choice(Group_C)
        select_Group_D=random.choice(Group_D)

        
        # Getting Deatails of  the Selected Horses and appending those deatails Selected Horses list and Printing Thoses Deatils
        # Selected Horses is A global Variable  
        
        for horse in total_horse_details:
            try:
            
                if horse['horse_id']==select_Group_A:
                    print(f"Horse id {horse['horse_id']} is selected from Group A and Horse's Name is {horse['horse_name']}")
                    selected_horses.append(horse)

                elif horse['horse_id']==select_Group_B:
                    print(f"Horse id {horse['horse_id']} is selected from Group B and Horse's Name is {horse['horse_name']}")
                    selected_horses.append(horse)
                
                elif horse['horse_id']==select_Group_C:
                    print(f"Horse id {horse['horse_id']} is selected from Group C and Horse's Name is {horse['horse_name']}")
                    selected_horses.append(horse)

                elif horse['horse_id']==select_Group_D:
                    print(f"Horse id {horse['horse_id']} is selected from Group D and Horse's Name is {horse['horse_name']}")
                    selected_horses.append(horse)
        
            except Exception:
                print("There was no horse in such Horse ID")

    except FileNotFoundError:
        print("\nFile Not Founded. Go to Menu and Save the file First")

    except Exception:
        print("\nAdd Minimum one Horse deatils for Each Group")




def Winning_Horse(selected_horses):

    try:
    # Setting Random Number that increse by 10 For Each Selected Horse as time
    
        for Horse in selected_horses:
            Horse['time'] = random.randrange(10, 90,10)

        for i in range(1, len(selected_horses)):
            current_dict = selected_horses[i]
            current_horse_id = int(current_dict["time"])
            j = i - 1

            # Move elements of the sorted part that are greater than the current_horse_id
            # to one position ahead of their current position
            while j >= 0 and current_horse_id < int(selected_horses[j]["time"]):
                selected_horses[j + 1] = selected_horses[j]
                j -= 1

            # Insert the current_dict into the correct position in the sorted part
            selected_horses[j + 1] = current_dict

        
        # Printing Horse Deatils And Timing

        First_Horse=selected_horses[0]
        print (f"\nFirst Place winner Horse's ID is {First_Horse['horse_id']} \nHorse's Name is {First_Horse['horse_name']} and Race time is {First_Horse['time']}s")
        
        Second_Horse=selected_horses[1]
        print (f"\nSecond Place winner Horse's ID is {Second_Horse['horse_id']} \nHorse's Name is {Second_Horse['horse_name']} and Race time is {Second_Horse['time']}s")

        Third_Horse=selected_horses[2]
        print (f"\nThird Place winner Horse's ID is {Third_Horse['horse_id']} \nHorse's Name is {Third_Horse['horse_name']} and Race time is {Third_Horse['time']}s")

    except Exception:
        print("\nBefore entering game menu , Finsh the Main Menu ")
        print("Input everything Order by order.")

    

def Visualize_Winning(selected_horses):

    try:
        # Getting First Three Horses Deatails 
        First_Horse=selected_horses[0]
        Second_Horse=selected_horses[1]
        Third_Horse=selected_horses[2]
        
        # Checking For How may Stars
        First_time='*' * int(First_Horse['time']/10)
        Second_time='*' *int(Second_Horse['time']/10)
        Third_time='*' * int(Third_Horse['time']/10)

        # Printing Horse id , How many stars and Taken Time  
        print(f"\nHorse ID {First_Horse['horse_id']} : {First_time}    {First_Horse['time']}s (1st Place)")
        print(f"Horse ID {Second_Horse['horse_id']} : {Second_time}    {Second_Horse['time']}s (2nd Place)")
        print(f"Horse ID {Third_Horse['horse_id']} : {Third_time}    {Third_Horse['time']}s (3rd Place)")

    except Exception:
        print("Input everything Order by order.")




# Global Variable Creation
total_horse_details=[]
selected_horses=[]

# Main console Menu   
while True:
    print("\n===== Horse Race Event Menu =====")
    print("1. Type AHD for adding horse details.")
    print("2. Type UHD for updating horse details.")
    print("3. Type DHD for deleting horse details.")
    print("4. Type VHD for viewing the registered horses\' details table.")
    print("5. Type SHD for saving the horse details to the text file.")
    print("6. Type START for Start the Game \n")
    print("7. Type ESC to exit the program.")

    choice = input("\nEnter your choice: ").upper()

    if choice == "AHD":
        add_horse(total_horse_details)
    elif choice == "UHD":
        update_horse(total_horse_details)
    elif choice == "DHD":
        delete_horse(total_horse_details)
    elif choice == "VHD":
        view_horses(total_horse_details)
    elif choice == "SHD":
        save_to_file(total_horse_details)
    elif choice == "START":
        
        # Clearing The List
        selected_horses.clear()

        # Starting the Game Menu
        # When The Game Started  You Have to Stop the Game Menu To do Previous Choices 
        while True:
            print(" \n\t---Game is Started ---")
            print("1. Type SDD for selecting four horses randomly for the major round.")
            print("2. Type WHD for displaying the Winning horses\' details.")
            print("3. Type VWH for Visualizing the time of the winning horses.")
            print("4. Type STOP  the Game And Entering the Menu . ")

            choice = input("\nEnter your choice: ").upper()
            
            if choice == "SDD":
                select_horses_for_race(total_horse_details,selected_horses)
            elif choice == "WHD":
                Winning_Horse(selected_horses)
            elif choice == "VWH":
                Visualize_Winning(selected_horses)
            elif choice == "STOP":                                  # Getting Out Of the Game Menu
                print("\nGetting Out The Menu")
                break
            else:
                print("\nInvalid choice. Please enter a valid option.")

    elif choice == "ESC":                                           # Getting Out Of the Program
        print("Exiting the program. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please enter a valid option.")
