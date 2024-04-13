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
