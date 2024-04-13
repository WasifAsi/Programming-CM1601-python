#Importing Files 
from AHD import add_horse
from UHD import update_horse
from DHD import delete_horse
from VHD import view_horses
from SHD import save_to_file
from SDD import select_horses_for_race
from WHD import Winning_Horse
from VWH import Visualize_Winning

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