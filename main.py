import menu
import inventory
import file_handler


running = True
inventory_data = file_handler.load_inventory()
while running:

    menu.display_menu()
    try:
        choice = int(input("Choice: "))
    except:
        print("invalid input, try again.")
        continue
    print()
    if choice == 1:
        inventory.view_inventory(inventory_data)
    elif choice ==2:
        inventory.add_medicine(inventory_data)
    elif choice == 3:
        inventory.remove_medicine(inventory_data)
    elif choice == 4:
        inventory.search_inventory(inventory_data)
    elif choice == 5:
        inventory.update_quantity(inventory_data)
    elif choice == 6:
        print("Goodbye!")
        running = False    
    else:
        print("Invalid choice, try again.")
    print()

file_handler.save_inventory(inventory_data)

