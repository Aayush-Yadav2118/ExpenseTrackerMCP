import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "aayush18",
    "database": "expense_tracker"
}


def get_connection():
    """
    Returns a connection to the MySQL database.
    """
    return mysql.connector.connect(**DB_CONFIG)


def initialize_database():
    """
    Creates the database and expenses table if they don't already exist.
    """

    try:
        # Connect to MySQL server (without selecting a database)
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )

        cursor = conn.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS expense_tracker")

        cursor.close()
        conn.close()

        # Connect to expense_tracker database
        conn = get_connection()
        cursor = conn.cursor()

        # Create expenses table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INT AUTO_INCREMENT PRIMARY KEY,
            amount DECIMAL(10,2) NOT NULL,
            category VARCHAR(100) NOT NULL,
            description TEXT,
            expense_date DATE NOT NULL,
            payment_method VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()

        print("Database initialized successfully.")

    except Error as e:
        print("MySQL Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()

        if 'conn' in locals() and conn.is_connected():
            conn.close()