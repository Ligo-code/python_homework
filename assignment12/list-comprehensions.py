import pandas as pd

df = pd.read_csv("../csv/employees.csv")

# 1. full names
full_names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print("All names:", full_names)

# 2. names containing 'e' (case-insensitive)
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nNames with 'e':", names_with_e)