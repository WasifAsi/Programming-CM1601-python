import random

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
