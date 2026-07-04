import database

def view_inventory():
    inventory = database.get_all_medicines()
    if not inventory:
        print("=====Inventory=====")
        print()
        print("Inventory is empty")
    else:
        print("=====Inventory=====")
        print()
        print(f"{'ID':<4}{'Name':<20}{'Qty':<8}NDC")
        print("-----------------------------------------------")
    for medicine in inventory:            
        print(f"{medicine['id']:<4}{medicine["name"]:<20}{medicine["quantity"]:<8}{medicine["ndc"]}")
        # print("Name:", medicine["name"])
        # print("Quantity:", medicine["quantity"])
        # print("NDC:", medicine["ndc"])
    print("-----------------------------------------------")

def add_medicine():
    name = get_non_empty_input("Medicine name: ")
    quantity = get_valid_quantity("Medicine quantity: ")
    ndc = get_non_empty_input("NDC: ")
    if database.ndc_exists(ndc):
        print("A medicine with that NDC already exists.")
    else:
        database.add_medicine(name,quantity,ndc)

def remove_medicine():
    name = input("Name of medicine you want removed: ")
    success = database.remove_medicine(name)
    if success:
        print("Medicine removed")
    else:
        print("Medicine not found")
    
def search_inventory():
    search = input("Medicine name: ").strip()
    name = database.search_medicine(search)
    if name is None:
        print("Medicine not found")
    else:
        print(f"Name: {name['name']}")
        print(f"Quantity: {name['quantity']}")
        print(f"NDC: {name['ndc']}")

def update_quantity():
    medicine_name = input("Medicine name: ").strip()
    new_quantity = get_valid_quantity("New quantity: ")
    success = database.update_quantity(medicine_name, new_quantity)
    if success:
        print("Medicine quantity updated")
    else:
        print("Medicine not found")

def get_valid_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity <0:
                print("quantity cannot be negative")
            else:
                return quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")


def get_non_empty_input(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("Input can not be empty.")
        else:
            return text