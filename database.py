import sqlite3

connection = sqlite3.connect("pharmacy.db", check_same_thread=False)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def get_all_medicines():
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    return rows

def add_medicine(name,quantity, ndc):
    cursor.execute(
        "INSERT INTO MEDICINES (name, quantity, ndc) VALUES (?,?,?)",
        (name,quantity,ndc)
        )
    connection.commit()

def remove_medicine(name):
    cursor.execute("DELETE FROM MEDICINES WHERE LOWER(name) = LOWER(?)", (name,))
    check = cursor.rowcount
    connection.commit()
    return check > 0
    

def update_quantity(name,quantity):
    cursor.execute("UPDATE MEDICINES SET QUANTITY = ? WHERE LOWER(name) = LOWER(?)", (quantity,name))
    check = cursor.rowcount
    connection.commit()
    return check > 0

def search_medicine(name):
    cursor.execute("SELECT * FROM MEDICINES WHERE LOWER(name) = LOWER(?)", (name,))
    searched = cursor.fetchone() 
    return searched

def ndc_exists(ndc):
    cursor.execute("SELECT * FROM MEDICINES WHERE ndc = ?", (ndc,))
    medicine = cursor.fetchone()
    return medicine