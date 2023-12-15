import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def req_sql():
    # Establish a connection to the MySQL database
    # Change the credentials here
    conn = mysql.connector.connect(
        host="database.quanc.com",
        user="user1138",
        password="P455WORD",
        database="mydatabase"
    )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Define your SQL query to select data
    query = "SELECT * FROM Challenge;"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Return all the rows here
    return rows