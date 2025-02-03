from flask import Flask, request, jsonify, render_template
import sqlite3
import re

app = Flask(__name__)

# Database connection function
def connect_db():
    return sqlite3.connect('company.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query').strip().lower()

    # Match queries for "Show me all employees in the [department] department."
    match = re.match(r"show me all employees in the (.+) department", user_input)
    if match:
        dept_name = match.group(1).strip()
        employees = find_employees_by_department(dept_name)
        if employees:
            response = "\n".join([f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}, Hire Date: {emp[4]}" for emp in employees])
        else:
            response = f"No employees found in the {dept_name} department."
        return jsonify({'response': response})

    # Match queries for "Who is the manager of the [department] department?"
    match = re.match(r"who is the manager of the (.+) department", user_input)
    if match:
        dept_name = match.group(1).strip()
        manager = find_manager_by_department(dept_name)
        if manager:
            response = f"The manager of the {dept_name} department is {manager[0]}."
        else:
            response = f"No manager found for the {dept_name} department."
        return jsonify({'response': response})

    # Match queries for "List all employees hired after [date]."
    match = re.match(r"list all employees hired after (.+)", user_input)
    if match:
        date = match.group(1).strip()
        employees = find_employees_hired_after(date)
        if employees:
            response = "\n".join([f"ID: {emp[0]}, Name: {emp[1]}, Department: {emp[2]}, Salary: {emp[3]}, Hire Date: {emp[4]}" for emp in employees])
        else:
            response = f"No employees found hired after {date}."
        return jsonify({'response': response})

    # Match queries for "What is the total salary expense for the [department] department?"
    match = re.match(r"what is the total salary expense for the (.+) department", user_input)
    if match:
        dept_name = match.group(1).strip()
        total_salary = calculate_total_salary_by_department(dept_name)
        if total_salary is not None:
            response = f"The total salary expense for the {dept_name} department is ${total_salary:.2f}."
        else:
            response = f"No salary data found for the {dept_name} department."
        return jsonify({'response': response})

    # Additional queries can be added here, such as:
    if "employee count" in user_input:
        dept_name = extract_department(user_input)
        if dept_name:
            count = count_employees_in_department(dept_name)
            response = f"The {dept_name} department has {count} employees."
        else:
            response = "Please specify a department."
        return jsonify({'response': response})

    elif "average salary" in user_input:
        dept_name = extract_department(user_input)
        if dept_name:
            avg_salary = average_salary_in_department(dept_name)
            response = f"The average salary in the {dept_name} department is ${avg_salary:.2f}."
        else:
            response = "Please specify a department."
        return jsonify({'response': response})

    else:
        return jsonify({'response': 'Sorry, I did not understand your query.'})

# Helper functions for interacting with the database

def find_employees_by_department(dept_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE Department LIKE ?", (f'%{dept_name}%',))
    employees = cursor.fetchall()
    conn.close()
    return employees

def find_manager_by_department(dept_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Manager FROM departments WHERE Name LIKE ?", (f'%{dept_name}%',))
    manager = cursor.fetchone()
    conn.close()
    return manager

def find_employees_hired_after(date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE Hire_Date > ?", (date,))
    employees = cursor.fetchall()
    conn.close()
    return employees

def calculate_total_salary_by_department(dept_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Salary) FROM employees WHERE Department LIKE ?", (f'%{dept_name}%',))
    total_salary = cursor.fetchone()[0]
    conn.close()
    return total_salary

# Additional helper functions for extra queries

def extract_department(user_input):
    # Look for department names in the user query (can be customized with a list of known departments)
    departments = ["sales", "marketing", "engineering", "hr", "it", "finance"]
    for dept in departments:
        if dept in user_input:
            return dept
    return None

def count_employees_in_department(dept_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM employees WHERE Department LIKE ?", (f'%{dept_name}%',))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def average_salary_in_department(dept_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(Salary) FROM employees WHERE Department LIKE ?", (f'%{dept_name}%',))
    avg_salary = cursor.fetchone()[0]
    conn.close()
    return avg_salary

if __name__ == '__main__':
    app.run(debug=True)

