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
