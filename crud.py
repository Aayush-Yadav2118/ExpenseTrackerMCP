from database import get_connection

def add_expense(amount, category, description, expense_date, payment_method):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO expenses
        (amount, category, description, expense_date, payment_method)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            amount,
            category,
            description,
            expense_date,
            payment_method
        )

        cursor.execute(query, values)
        conn.commit()

        expense_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return f"Expense added successfully. Expense ID: {expense_id}"
    except Exception as e:
        return str(e)
    
    finally:
        cursor.close()
        conn.close()


def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM expenses ORDER BY expense_date DESC")

    expenses = cursor.fetchall()

    cursor.close()
    conn.close()

    return expenses


def get_expenses_by_category(category):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM expenses WHERE category=%s",
        (category,)
    )

    expenses = cursor.fetchall()

    cursor.close()
    conn.close()

    return expenses


def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=%s",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        message = "Expense not found."
    else:
        message = "Expense deleted successfully."

    cursor.close()
    conn.close()

    return message


def update_expense(expense_id, amount, category, description, expense_date, payment_method):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE expenses
    SET amount=%s, category=%s, description=%s, expense_date=%s, payment_method=%s
    WHERE id=%s
    """

    values = (
        amount,
        category,
        description,
        expense_date,
        payment_method,
        expense_id
    )

    cursor.execute(query, values)
    conn.commit()

    if cursor.rowcount == 0:
        message = "Expense not found."
    else:
        message = "Expense updated successfully."

    cursor.close()
    conn.close()

    return message

def get_total_expense():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total if total else 0

def get_category_summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT category, SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
    """)

    summary = cursor.fetchall()

    cursor.close()
    conn.close()

    return summary