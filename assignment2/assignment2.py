
import os


# Task 1: Diary
import traceback

try:
    
    with open("diary.txt", "a") as diary:# opens the file in append mode. If the file does not exist, it will be created
        
        line = input("What happened today? ")# asks the user for input initially
        
        while line.lower() != "done for now":
            diary.write(line + "\n")# next line
            line = input("What else? ")# loops until the user types "done for now"
        
        diary.write("done for now\n")

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(
            f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
        )
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")


# Task 2: Read a CSV File
import csv
import traceback

def read_employees():
    try:
        employees_dict = {}  # Dictionary to store fields and rows
        rows = []  # List to store employee rows

        # Open the CSV file using a context manager
        with open("csv/employees.csv", "r", newline='') as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    employees_dict["fields"] = row  # First row as headers
                else:
                    rows.append(row)  # All other rows as employee data

        employees_dict["rows"] = rows
        return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

# Global variable to store employees dict
employees = read_employees()
print(employees)


# Task 3: Find the Column Index
def column_index(column_name):
    return employees["fields"].index(column_name)

# Get index of "employee_id" column
employee_id_column = column_index("employee_id")
print(f"Index of employee_id: {employee_id_column}")

# Task 4: Find the Employee First Name
def first_name(row_number):
    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]

print("First name in row 0:", first_name(0))

# Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches

print("Employee with ID 5 (function version):", employee_find(5))

# Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

print("Employee with ID 5 (lambda version):", employee_find_2(5))

# Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

sorted_rows = sort_by_last_name()
print("Sorted by last name:")
for row in sorted_rows:
    print(row)

# Task 8: Create a dict for an Employee
def employee_dict(row):
    employee_data = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":  # Skip employee_id
            employee_data[field] = row[i]
    return employee_data

example_dict = employee_dict(employees["rows"][2])
print("Employee dict (row 2):", example_dict)

# Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    all_emps = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        all_emps[emp_id] = employee_dict(row)
    return all_emps

# Call and store in global variable
all_employees = all_employees_dict()

print("All employees (2 samples):")
print("ID 1:", all_employees["1"])
print("ID 5:", all_employees["5"])

# Task 10: Use the os Module
import os

def get_this_value():
    return os.getenv("THISVALUE")

print("THISVALUE environment variable:", get_this_value())

# Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_value):
    custom_module.set_secret(new_value)

set_that_secret("simsim")
print("Updated secret from custom_module:", custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def read_file(path):
        try:
            with open(path, "r", newline='') as file:
                reader = csv.reader(file)
                minutes_data = {}
                rows = []

                for i, row in enumerate(reader):
                    if i == 0:
                        minutes_data["fields"] = row
                    else:
                        rows.append(tuple(row))  # Store each row as a tuple

                minutes_data["rows"] = rows
                return minutes_data

        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(
                    f"File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}"
                )
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
            exit()

    minutes1 = read_file("csv/minutes1.csv")
    minutes2 = read_file("csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


# Task 13: Create minutes_set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined_set = set1.union(set2)
    return combined_set

# Global variable to hold the set
minutes_set = create_minutes_set()
print("Combined minutes set:")
print(minutes_set)


# Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    raw_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), raw_list))
    return converted

# Global variable to hold the datetime list
minutes_list = create_minutes_list()
print("Minutes list with datetime objects:")
for item in minutes_list:
    print(item)


# Task 15: Write Out Sorted List
def write_sorted_list():
    # Sort by datetime (second element of each tuple)
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    # Convert datetime back to string
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))

    # Write to minutes.csv
    try:
        with open("minutes.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])  # Write headers
            writer.writerows(converted)        
        return converted
    except Exception as e:
        print(f"Failed to write file: {e}")
        return []

# Call the function and store result
final_minutes = write_sorted_list()
print("Final sorted minutes list:")
for row in final_minutes:
    print(row)
