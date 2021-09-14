import sqlite3
"""
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    sqlite_create_table_query = "CREATE TABLE vstProducts (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                photo BLOB,
                                drawing BLOB
                                );"

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
"""
def convertToBinaryData(filename):
    "Converting digital data to binary format"
    
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(item_id, item_name, photo, drawing):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """INSERT into vstProducts (id, name, photo, drawing) VALUES (?,?,?,?)"""

        item_photo = convertToBinaryData(photo)
        item_drawing = convertToBinaryData(drawing)
        data_tuple = (item_id, item_name, item_photo, item_drawing)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
            
insertBLOB(1,"VST_Wall_Basic", "img\DJI_0429.JPG", "img\sell.png")

