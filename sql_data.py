#import mysql.connector


'''def connect_to_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Agnik12345",
        database="text_utils"
    )
    return connection'''


def write_data(data):
    pass
    '''connection = connect_to_database()
    cursor = connection.cursor()

    # Extract dictionary keys and values
    keys = ", ".join(data.keys())
    values = tuple(data.values())

    # Create placeholders for values in the SQL query
    placeholders = ", ".join(["%s"] * len(data))

    # Define the SQL query to insert data
    query = f"INSERT INTO user_message values ({placeholders});"

    # Execute the query
    cursor.execute(query, values)

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()'''

def read_data():
   pass
   ''' connection = connect_to_database()
    cursor = connection.cursor()

    # Define the SQL query to retrieve data
    query = "SELECT * FROM user_message"

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    return rows'''


if __name__=="__main__":
    data_to_write = {
        "name": "John",
        "password": "12345"
    }

    write_data(data_to_write)
    print("Data written to the database successfully!")

    # Read data from the database
    data_read = read_data()
    print("Data read from the database:")
    for row in data_read:
        print(row)
