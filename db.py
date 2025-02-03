import sqlite3

def create_database():
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Create departments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            manager TEXT NOT NULL
        )
    ''')

    # Create employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL,
            hire_date TEXT NOT NULL
        )
    ''')

    # Insert data into departments table
    cursor.executemany('''
        INSERT INTO departments (id, name, manager)
        VALUES (?, ?, ?)
    ''', [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie'),
        (4, 'HR', 'David'),
        (5, 'Finance', 'Eva'),
        (6, 'IT', 'Frank'),
        (7, 'Customer Support', 'Grace')
    ])

    # Insert data into employees table
    cursor.executemany('''
        INSERT INTO employees (id, name, department, salary, hire_date)
        VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
        (4, 'David', 'HR', 45000, '2021-07-01'),
        (5, 'Eva', 'Finance', 75000, '2020-08-15'),
        (6, 'Frank', 'IT', 80000, '2019-11-30'),
        (7, 'Grace', 'Customer Support', 40000, '2022-01-10'),
        (8, 'Helen', 'Sales', 52000, '2021-03-05'),
        (9, 'Ian', 'Engineering', 72000, '2019-04-25'),
        (10, 'Jack', 'Marketing', 65000, '2023-05-18'),
        (11, 'Katie', 'HR', 47000, '2022-10-01'),
        (12, 'Liam', 'Finance', 77000, '2021-06-30'),
        (13, 'Monica', 'IT', 85000, '2018-08-22'),
        (14, 'Nina', 'Customer Support', 39000, '2023-02-17'),
        (15, 'Oscar', 'Sales', 54000, '2020-11-10'),
        (16, 'Peter', 'Engineering', 71000, '2022-01-12'),
        (17, 'Quincy', 'Marketing', 62000, '2020-12-07'),
        (18, 'Rachel', 'HR', 48000, '2023-04-14'),
        (19, 'Sam', 'Finance', 79000, '2022-03-01'),
        (20, 'Tina', 'IT', 82000, '2021-09-09')
    ])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()