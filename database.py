import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    try:
        cnx = psycopg2.connect(
            user="zfimgpswjt",
            password=os.getenv("DATABASE_PASSWORD"),
            host="consumer-analysis-server.postgres.database.azure.com",
            port=5432,
            database="postgres"
        )
        return cnx
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None