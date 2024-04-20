from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from database import get_db_connection
import psycopg2

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route for handling the login form submission
@app.route('/login', methods=['POST'])
def login_post():
    # Retrieve username, password, and email from the form
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Process login data here (e.g., validate credentials)

    # Redirect to the search page
    return render_template('search.html')

# Route for the search page
@app.route('/search')
def search():
    return render_template('search.html')

# Route for handling the search form submission
@app.route('/search', methods=['POST'])
def search_post():
    # Retrieve Hshd_num from the form
    hshd_num = request.form['hshd_num']

    # Get a database connection
    conn = get_db_connection()
    if conn:
        try:
            # Retrieve data based on Hshd_num
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM your_table WHERE Hshd_num = {hshd_num} ORDER BY Hshd_num, Basket_num, Date, Product_num, Department, Commodity")
            search_results = cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            search_results = []
        finally:
            # Close connection
            cursor.close()
            conn.close()
    else:
        print("Failed to establish a database connection.")
        search_results = []

    # Render search results template with retrieved data
    return render_template('search.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True)