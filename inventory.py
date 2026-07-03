def view_inventory(inventory):
    if not inventory:
        print("=====Inventory=====")
        print()
        print("Inventory is empty")
    else:
        print("=====Inventory=====")
        print()
    for medicine in inventory:            
        print()
        print("Name: ", medicine["name"])
        print("Quantity: ", medicine["quantity"])
        print()

def add_medicine(inventory):
    name = input("Medicine name: ")
    quantity = int(input("Medicine quantity: "))
    medicine = {
        "name" : name,
        "quantity" : quantity
    }
    inventory.append(medicine)

def remove_medicine(inventory):
    if not inventory:
        print("Nothing to remove")
        return
    remove = input("Name of medicine you want removed: ")
    for medicine in inventory:
        if medicine["name"] == remove:
            inventory.remove(medicine)
            print("Medicine Removed")
            break
        else:
            print("Medicine not in inventory")

def search_inventory(inventory):
    if not inventory:
        print("Nothing to search")
        return
    search = input("Medicine name: ").strip().lower()
    if not inventory:
        print("List is empty")
        return
    for medicine in inventory:
        if search == medicine["name"].lower():
            print("Medicine found!")
            print("Name: ", medicine["name"])
            print("Quantity: ", medicine["quantity"])
            break
    else:
        print("Medicine not found")

def update_quantity(inventory):
    if not inventory:
        print("Nothing to update")
        return
    medicine_name = input("What medications quantity would you like to update? ").strip().lower()
    for medicine in inventory:
        if medicine_name == medicine["name"].lower():
            update = int(input("What will be the new quantity?"))
            medicine["quantity"] = update
            print("Quantity updated!")
            break
            
    else:
        print("Medicine not found")