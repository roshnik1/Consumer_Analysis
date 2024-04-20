import pandas as pd
import psycopg2
from psycopg2 import sql
from database import get_db_connection

# Excel file path
EXCEL_FILE = "C:/Users/hanee/OneDrive/Desktop/Spring 2024/Cloud Computing/Final Project/400_households.xlsx"

# Table name in PostgreSQL database
TABLE_NAME = "Households"

def insert_data(conn, df):
    """Insert data from DataFrame into PostgreSQL database."""
    try:
        cur = conn.cursor()

        # Build SQL query for inserting data into table
        columns = df.columns.tolist()
        columns_str = ", ".join(columns)
        values_str = ", ".join(["%s" for _ in range(len(columns))])
        insert_query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(TABLE_NAME),
            sql.SQL(columns_str),
            sql.SQL(values_str)
        )

        # Insert data into table
        data = [tuple(row) for row in df.to_numpy()]
        cur.executemany(insert_query, data)
        conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print("Error: Unable to insert data into the table.")
        print(e)
    finally:
        if cur:
            cur.close()

def main():
    # Create database connection
    conn = get_db_connection()
    if conn is None:
        return

    try:
        # Read Excel file into DataFrame
        df = pd.read_excel(EXCEL_FILE)

        # Insert data into PostgreSQL database
        insert_data(conn, df)
    finally:
        # Close database connection
        conn.close()

if __name__ == "__main__":
    main()