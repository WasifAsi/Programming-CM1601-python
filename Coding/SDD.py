import random

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
