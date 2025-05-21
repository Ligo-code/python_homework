import sqlite3
import pandas as pd

# Connect to the lesson.db database
with sqlite3.connect("../db/lesson.db") as conn:
    # Step 1: Run JOIN query
    sql = """
        SELECT 
            li.line_item_id,
            li.quantity,
            li.product_id,
            p.product_name,
            p.price
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id;
    """

    df = pd.read_sql_query(sql, conn)

# Step 2: Preview first 5 rows
print(" Initial DataFrame:")
print(df.head())

# Step 3: Calculate total = quantity * price
df["total"] = df["quantity"] * df["price"]
print("\n With 'total' column:")
print(df.head())

# Step 4: Group by product_id
summary = df.groupby("product_id").agg({
    "line_item_id": "count",
    "total": "sum",
    "product_name": "first"
}).reset_index()

# Step 5: Sort by product_name
summary = summary.sort_values(by="product_name")

# Step 6: Save to CSV
summary.to_csv("order_summary.csv", index=False)

print("\n Summary saved to order_summary.csv")
print(summary.head())
