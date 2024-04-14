import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import sql

# Load environment variables from .env file
load_dotenv()

# Database connection configuration
DATABASE_HOST = "consumer-server.postgres.database.azure.com"
DATABASE_NAME = "consumer-database"
DATABASE_USER = "zlbzszmwuj"
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

# # Excel file path
# EXCEL_FILE = "C:/Users/hanee/OneDrive/Desktop/Spring 2024/Cloud Computing/Final Project/400_households.xlsx"

# # Table name in PostgreSQL database
# TABLE_NAME = "Households"

def create_connection():
    """Create a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DATABASE_HOST,
            database=DATABASE_NAME,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD
        )
        return conn
    except psycopg2.Error as e:
        print("Error: Unable to connect to the database.")
        print(e)
        return None

# def insert_data(conn, df):
#     """Insert data from DataFrame into PostgreSQL database."""
#     try:
#         cur = conn.cursor()

#         # Build SQL query for inserting data into table
#         columns = df.columns.tolist()
#         columns_str = ", ".join(columns)
#         values_str = ", ".join(["%s" for _ in range(len(columns))])
#         insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
#             sql.Identifier(TABLE_NAME),
#             sql.SQL(columns_str),
#             sql.SQL(values_str)
#         )

#         # Insert data into table
#         data = [tuple(row) for row in df.to_numpy()]
#         cur.executemany(insert_query, data)
#         conn.commit()

#         print("Data inserted successfully.")
#     except psycopg2.Error as e:
#         if conn:
#             conn.rollback()
#         print("Error: Unable to insert data into the table.")
#         print(e)
#     finally:
#         if cur:
#             cur.close()

def main():
    # Create database connection
    conn = create_connection()
    if conn is None:
        return

#     try:
#         # Read Excel file into DataFrame
#         df = pd.read_excel(EXCEL_FILE)

#         # Insert data into PostgreSQL database
#         insert_data(conn, df)
#     finally:
#         # Close database connection
#         conn.close()

if __name__ == "__main__":
    main()
