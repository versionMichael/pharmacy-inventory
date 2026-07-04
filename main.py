import menu
import inventory
import database


running = True

while running:

    menu.display_menu()
    try:
        choice = int(input("Choice: "))
    except:
        print("invalid input, try again.")
        continue
    print()
    if choice == 1:
        inventory.view_inventory()
    elif choice ==2:
        inventory.add_medicine()
    elif choice == 3:
        inventory.remove_medicine()
    elif choice == 4:
        inventory.search_inventory()
    elif choice == 5:
        inventory.update_quantity()
    elif choice == 6:
        print("Goodbye!")
        running = False    
    else:
        print("Invalid choice, try again.")
    print()


