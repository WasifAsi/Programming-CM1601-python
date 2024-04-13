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