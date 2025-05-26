import sqlite3

# --- Connect to the database ---
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# --- Task 1: Total price for the first 5 orders ---
query1 = """
SELECT 
    o.order_id, 
    SUM(p.price * li.quantity) AS total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""
cursor.execute(query1)
results1 = cursor.fetchall()

print("Task 1: Total Price for First 5 Orders")
for row in results1:
    print(f"Order ID: {row[0]}, Total Price: {row[1]}")

# --- Task 2: Average order price per customer using subquery ---
query2 = """
SELECT 
    c.customer_name AS customer_name,
    AVG(sub.total_price) AS average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b,
        SUM(p.price * li.quantity) AS total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) AS sub ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

print("\nTask 2: Average Order Price Per Customer")
for row in results2:
    name = row[0]
    avg_price = round(row[1], 2) if row[1] is not None else 0
    print(f"Customer: {name}, Average Order Price: {avg_price}")

# --- Task 3: Insert a new order for 'Perez and Sons' ---
try:
    cursor = conn.cursor()

    # Get customer_id for 'Perez and Sons'
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]

    # Get employee_id for 'Miranda Harris'
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]

    # Get the 5 least expensive products
    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    print("\nTask 3: Creating a new order for 'Perez and Sons'...")

    # Begin transaction
    conn.execute("BEGIN")

    # Insert order and return new order_id
    cursor.execute(
        "INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, DATE('now')) RETURNING order_id",
        (customer_id, employee_id)
    )
    order_id = cursor.fetchone()[0]

    # Insert 5 line_items for that order
    for pid in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, pid, 10)
        )

    # Commit the transaction
    conn.commit()

    # Display the created line_items
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
    """, (order_id,))
    line_items = cursor.fetchall()

    print("Line Items for the New Order:")
    for item in line_items:
        print(f"LineItem ID: {item[0]}, Quantity: {item[1]}, Product: {item[2]}")

except Exception as e:
    conn.rollback()
    print("Transaction failed:", e)

# --- Task 4: Employees with more than 5 orders ---
query4 = """
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id
HAVING COUNT(o.order_id) > 5;
"""

cursor.execute(query4)
results4 = cursor.fetchall()

print("\nTask 4: Employees with More Than 5 Orders")
for row in results4:
    emp_id = row[0]
    first = row[1]
    last = row[2]
    count = row[3]
    print(f"Employee ID: {emp_id}, Name: {first} {last}, Order Count: {count}")


# --- Close the connection ---
conn.close()
