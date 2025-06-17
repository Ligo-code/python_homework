import pandas as pd

# Task 1: Create DataFrame from dictionary
data = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)
print("Task 1 - Original DataFrame:")
print(task1_data_frame)

# Create a copy and add a Salary column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print("\nTask 1 - DataFrame with Salary:")
print(task1_with_salary)

# Create another copy and increment Age
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

print("\nTask 1 - DataFrame with incremented Age:")
print(task1_older)

# Save DataFrame to CSV
task1_older.to_csv("employees.csv", index=False)

# Load data from CSV 
task2_employees = pd.read_csv("employees.csv")
print("\nTask 2 - Data loaded from CSV:")
print(task2_employees)

# Load data from JSON
json_employees = pd.read_json("assignment3/additional_employees.json")
print("\nTask 2 - Data loaded from JSON:")
print(json_employees)

# Combine both DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined DataFrame:")
print(more_employees)

# Task 3 - Use head() to get first three rows
first_three = more_employees.head(3)
print("\nTask 3 - First three rows:")
print(first_three)

# Use tail() to get last two rows
last_two = more_employees.tail(2)
print("\nTask 3 - Last two rows:")
print(last_two)

# Get shape of DataFrame
employee_shape = more_employees.shape
print("\nTask 3 - Shape of DataFrame:")
print(employee_shape)

# Use info() to display summary
print("\nTask 3 - DataFrame Info:")
more_employees.info()

# Task 4 - Read dirty data
dirty_data = pd.read_csv("assignment3/dirty_data.csv")
print("\nTask 4 - Dirty Data:")
print(dirty_data)

clean_data = dirty_data.copy()

clean_data.drop_duplicates(inplace=True)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("\nTask 4 - Clean Data:")
print(clean_data)
