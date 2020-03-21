import sqlite3

conn = sqlite3.connect("re.db")
c = conn.cursor()


def createDishTable():
    sql = """
        CREATE TABLE IF NOT EXISTS dishes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            price INTEGER (6)
        )
    """
    c.execute(sql)
    conn.commit()
    print("Dish Table Created")

def insertNewDish(name,price):
    sql = """ 
        INSERT INTO dishes(name,price) VALUES (?,?)
    """
    c.execute(sql,(name,price))
    conn.commit();
    print("New Dish Inserted!")

def getAllDishes():
    sql = """ 
        SELECT * FROM dishes
    """ 
    result = c.execute(sql)
    conn.commit()
    return result


