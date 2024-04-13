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