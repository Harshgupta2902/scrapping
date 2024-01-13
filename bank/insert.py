import os
import pandas as pd
import mysql.connector
from mysql.connector import Error

# MySQL connection parameters
host = 'localhost'
database = 'banks'
user = 'root'
password = ''

# Folder containing the Excel files
download_directory = "/home/user/Downloads/xls"

# Establish the MySQL connection
try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the 'banks' table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS banks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            BANK VARCHAR(255) NULL,
            IFSC VARCHAR(255) NULL,
            BRANCH VARCHAR(255) NULL,
            ADDRESS VARCHAR(255) NULL,
            CITY1 VARCHAR(255) NULL,
            CITY2 VARCHAR(255) NULL,
            STATE VARCHAR(255) NULL,
            STD_CODE INT NULL,
            PHONE VARCHAR(255) NULL
        )
        """
        cursor.execute(create_table_query)

        # Iterate over each file in the folder
        for file_name in os.listdir(download_directory):
            if file_name.endswith(".xlsx"):
                file_path = os.path.join(download_directory, file_name)

                try:
                    # Read Excel file into a DataFrame
                    df = pd.read_excel(file_path)

                    # Insert data into the MySQL table
                    for _, row in df.iterrows():
                        insert_query = """
                        INSERT INTO banks (BANK, IFSC, BRANCH, ADDRESS, CITY1, CITY2, STATE, STD_CODE, PHONE)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        data = tuple(row)
                        cursor.execute(insert_query, data)

                    print(f"Data from file {file_name} inserted into 'banks' table.")

                except Exception as insert_error:
                    print(f"Error processing file {file_name}: {insert_error}")

        # Commit changes
        connection.commit()
        print("All data inserted into 'banks' table successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
