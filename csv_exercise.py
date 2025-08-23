import csv

def create_sample_data():
    employee_data = [
        ["Name", "Department", "Salary", "Years_Experience", "Performance_Score"],
        ["Alice Johnson", "Engineering", "75000", "5", "4.2"],
        ["Bob Smith", "Marketing", "65000", "3", "3.8"],
        ["Carol Williams", "Engineering", "45000", "1", "3.5"],
        ["David Brown", "Sales", "50000", "2", "4.5"],
        ["Eva Davis", "HR", "55000", "4", "4.0"],
        ["Frank Miller", "Engineering", "85000", "8", "4.8"],
        ["Grace Wilson", "Marketing", "40000", "1", "3.2"],
        ["Henry Garcia", "Sales", "70000", "6", "4.3"]
    ]

    with open('employees.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(employee_data)
    
    print("✅ Sample data created: employees.csv")

def task_1_read_csv():
    """TASK 1: Read CSV and display all data"""
    print("TASK 1: Read CSV File")

    with open('employees.csv', 'r') as file:
        csv_reader = csv.reader(file)
        row_count = 0
        for row in csv_reader:
            print(row)
            row_count += 1

        print(f"Total employees: {row_count - 1}")

def task_2_read_as_dictionaries():
    """TASK 2: Read CSV as dictionaries (easier to work with)"""
    print("\n")
    print("TASK 2: Read as Dictionaries")
    print("=" * 50)
    
    # YOUR CODE HERE:
    # 1. Open the CSV file
    # 2. Use csv.DictReader() to read it
    # 3. Print each row (now it's a dictionary!)
    # 4. Print just the names of all employees

    with open('employees.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
            print(row['Name'])

def task_3_basic_calculations():
    """TASK 3: Calculate average salary"""
    print("\n")
    print("TASK 3: Calculate Average Salary")
    
    # YOUR CODE HERE:
    # 1. Read the CSV file
    # 2. Add up all salaries (remember to convert string to int!)
    # 3. Count number of employees
    # 4. Calculate and display average salary

    with open('employees.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        salaries = []
        employees_count = 0
        for row in csv_reader:
            try:
                salaries.append(int(row['Salary']))
                employees_count += 1
            except (ValueError, KeyError):
                continue

        total = sum(salaries)
        average = total / employees_count if salaries else 0
        print(f"Total employees salary: {total}")
        print(f"Total employees: {employees_count}")
        print(f"Average employees salary; {average}")

def task_4_find_highest_performer():
    """TASK 4: Find employee with highest performance score"""
    print("\n")
    print("TASK 4: Find Top Performer")
    
    # YOUR CODE HERE:
    # 1. Read the CSV file
    # 2. Keep track of the highest score and employee name
    # 3. Convert performance score to float for comparison
    # 4. Display the top performer's name and score
    
    with open('employees.csv', 'r') as file:
        employee = ""
        best_score = 0.0

        try:
            with open("employees.csv", 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    try:
                        score = float(row.get("Performance_Score", 0.0))

                        if score > best_score:
                            best_score = score
                            employee = row.copy()
                    except ValueError:
                        continue
                print(f"{employee["Name"]} is the best performing employee with {employee["Performance_Score"]} performance score.")
        except FileNotFoundError:
            print("File not found")

def task_5_filter_by_department(department):
    """TASK 5: Show all Engineering employees"""
    print("\n")
    print("TASK 5: Filter by Department")
    
    # YOUR CODE HERE:
    # 1. Read the CSV file
    # 2. Print only employees where Department == "Engineering"
    # 3. Count how many Engineering employees there are
    
    with open('employees.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        count = 0
        print("Employees in {department} are:")
        for row in csv_reader:
            if row['Department'] == department:
                print(f"{row['Name']}")
                count += 1
                
        print(f"Total employees in {department} department: {count}")

def task_6_salary_analysis():
    """TASK 6: Analyze salaries by department"""
    print("\n")
    print("TASK 6: Salary Analysis by Department")
    
    # YOUR CODE HERE:
    # 1. Read the CSV file
    # 2. Group employees by department
    # 3. Calculate average salary for each department
    # 4. Display results

    departments = {}

    try:
        with open("employees.csv", 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    dept = row["Department"]
                    salary = row["Salary"]
                    if dept in departments:
                        departments[dept][0] += float(salary)
                        departments[dept][1] += 1
                    else:
                        departments[dept] = [float(salary), 1]
                except ValueError:
                    continue
    except FileNotFoundError:
        print("File not found")

    print(departments)

# MAIN PROGRAM
if __name__ == "__main__":
    print("🎯 CSV ANALYSIS EXERCISE - BASIC PYTHON ONLY")
    
    task_1_read_csv()
    task_2_read_as_dictionaries()
    task_3_basic_calculations()
    task_4_find_highest_performer()
    task_5_filter_by_department("Engineering")
    task_6_salary_analysis()
