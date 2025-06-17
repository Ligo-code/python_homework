import sqlite3

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database connected successfully.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        );
        """)

        print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    result = cursor.fetchone()
    if result:
        publisher_id = result[0]
        try:
            cursor.execute(
                "INSERT INTO magazines (name, publisher_id) VALUES (?, ?)",
                (name, publisher_id)
            )
        except sqlite3.IntegrityError:
            print(f"Magazine '{name}' already exists.")
    else:
        print(f"Publisher '{publisher_name}' not found.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    result = cursor.fetchone()
    if result:
        print(f"Subscriber '{name}' at '{address}' already exists.")
    else:
        cursor.execute(
            "INSERT INTO subscribers (name, address) VALUES (?, ?)",
            (name, address)
        )

def add_subscription(cursor, subscriber_name, magazine_name, expiration_date):
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ?", (subscriber_name,))
    subscriber = cursor.fetchone()

    cursor.execute("SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
    magazine = cursor.fetchone()

    if subscriber and magazine:
        subscriber_id = subscriber[0]
        magazine_id = magazine[0]

        cursor.execute(
            "SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?",
            (subscriber_id, magazine_id)
        )
        if cursor.fetchone():
            print(f"{subscriber_name} is already subscribed to {magazine_name}.")
            return

        cursor.execute("""
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
        """, (subscriber_id, magazine_id, expiration_date))
    else:
        print(f"Subscriber or magazine not found: {subscriber_name}, {magazine_name}")


# Main block to insert data
with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    add_publisher(cursor, "Tech World")
    add_publisher(cursor, "Health Plus")
    add_publisher(cursor, "Nature Daily")

    add_magazine(cursor, "AI Monthly", "Tech World")
    add_magazine(cursor, "Wellness Weekly", "Health Plus")
    add_magazine(cursor, "Planet Earth", "Nature Daily")

    add_subscriber(cursor, "Alice Smith", "123 Main St")
    add_subscriber(cursor, "Bob Johnson", "456 Elm St")
    add_subscriber(cursor, "Charlie Rose", "789 Oak St")

    add_subscription(cursor, "Alice Smith", "AI Monthly", "2025-12-31")
    add_subscription(cursor, "Bob Johnson", "Wellness Weekly", "2025-11-30")
    add_subscription(cursor, "Charlie Rose", "Planet Earth", "2026-01-15")

    conn.commit()
    print("Data inserted successfully.")

with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("\n All subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\n All magazines sorted by name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name")
    for row in cursor.fetchall():
        print(row)

    print("\n Magazines by publisher 'Tech World':")
    cursor.execute("""
        SELECT m.magazine_id, m.name
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = 'Tech World'
    """)
    for row in cursor.fetchall():
        print(row)

