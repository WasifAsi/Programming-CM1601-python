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