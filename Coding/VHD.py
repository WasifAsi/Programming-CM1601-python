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
