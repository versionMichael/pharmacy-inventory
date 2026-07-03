def save_inventory(inventory):
    file = open("test.txt", "w")
    #file.write("hello pharmacy")
    for medicine in inventory:
        data = medicine["name"] + ", " + str(medicine["quantity"]) +"\n"
        file.write(data)    
    file.close()

def load_inventory():

    inventory = []

    with open("test.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        if line.strip() == "":
            continue
        medicine = {}
        parts = line.split(",")
        medicine["name"] = parts[0]
        medicine["quantity"] = int(parts[1].strip())
        inventory.append(medicine)
        

    return inventory
