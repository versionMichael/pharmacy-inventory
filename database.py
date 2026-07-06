import psycopg
from psycopg.rows import dict_row

connection = psycopg.connect(
    host="localhost",
    dbname="pharmacy_inventory",
    user="postgres",
    password="3921",
    port=5432
)
cursor = connection.cursor(row_factory=dict_row)

cursor.execute("SELECT * FROM medicines")
rows = cursor.fetchall()

def get_all_medicines():
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    return rows

def add_medicine(name, quantity, ndc):
    cursor.execute(
        "INSERT INTO medicines (name, quantity, ndc) VALUES (%s, %s, %s)",
        (name, quantity, ndc)
    )
    connection.commit()

def remove_medicine(name):
    cursor.execute(
        "DELETE FROM medicines WHERE LOWER(name) = LOWER(%s)",
        (name,)
    )
    check = cursor.rowcount
    connection.commit()
    return check > 0

def update_quantity(name, quantity):
    cursor.execute(
        "UPDATE medicines SET quantity = %s WHERE LOWER(name) = LOWER(%s)",
        (quantity, name)
    )
    check = cursor.rowcount
    connection.commit()
    return check > 0

def search_medicine(name):
    cursor.execute("SELECT * FROM MEDICINES WHERE LOWER(name) = LOWER(%s)", (name,))
    searched = cursor.fetchone() 
    return searched

def ndc_exists(ndc):
    cursor.execute("SELECT * FROM MEDICINES WHERE ndc = %s", (ndc,))
    medicine = cursor.fetchone()
    return medicine



print(get_all_medicines())