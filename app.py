import os
import mysql.connector

# ================== DATABASE CONNECTION ==================

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",
        database="muskanproject"
    )

con = get_connection()

# ================== GLOBAL USERS ==================

EMPLOYEES = {
    "Emp1": "meow123",
    "Emp2": "nn123",
    "Emp3": "jivi11",
    "Emp4": "kanha22"
}

ADMIN_PASSWORD = "adm34"

# ================== FILE FUNCTIONS ==================

def display_notifications():
    try:
        with open("notif.txt", "r") as f:
            print("\n--- NOTIFICATIONS ---")
            print(f.read())
    except FileNotFoundError:
        print("Notification file not found.")

def display_holidays():
    try:
        with open("list.txt", "r") as f:
            print("\n--- HOLIDAY LIST ---")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Holiday file not found.")

# ================== WELLNESS ==================

def wellness(emp_id):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        temp = float(input("Enter temperature (F): "))
        contact = input("Contact with sick person? (Y/N): ").upper()
        symptoms = input("Symptoms? (Y/N): ").upper()

        score = 0
        if temp >= 100.1:
            score += 1
        if contact == "Y":
            score += 1
        if symptoms == "Y":
            score += 1

        status = "Unwell" if score >= 2 else "Well"
        print(f"Health Status: {status}")

        sql = f"INSERT INTO {emp_id.lower()} VALUES (%s,%s)"
        data = (date, status)

        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()

        print("Health record updated successfully.")

    except Exception as e:
        print("Error:", e)

# ================== ADMIN MENU ==================

def admin_menu():
    while True:
        print("\n===== ADMIN MENU =====")
        print("1. View Notifications")
        print("2. Add Notification")
        print("3. View Employees")
        print("4. View Employee Health")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            display_notifications()

        elif choice == 2:
            msg = input("Enter notification: ")
            with open("notif.txt", "a") as f:
                f.write("\n" + msg)
            print("Notification added.")

        elif choice == 3:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM admin")
            for row in cursor.fetchall():
                print(row)

        elif choice == 4:
            emp = input("Enter Employee ID (Emp1-Emp4): ")
            if emp in EMPLOYEES:
                cursor = con.cursor()
                cursor.execute(f"SELECT * FROM {emp.lower()}")
                for row in cursor.fetchall():
                    print(row)
            else:
                print("Invalid employee.")

        elif choice == 5:
            print("Exiting Admin Panel.")
            break

        else:
            print("Invalid choice.")

# ================== EMPLOYEE MENU ==================

def employee_menu(emp_id):
    while True:
        print("\n===== EMPLOYEE MENU =====")
        print("1. View My Data")
        print("2. Wellness")
        print("3. Holidays")
        print("4. Notifications")
        print("5. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM admin WHERE EmpId=%s", (emp_id,))
            for row in cursor.fetchall():
                print(row)

        elif choice == 2:
            wellness(emp_id)

        elif choice == 3:
            display_holidays()

        elif choice == 4:
            display_notifications()

        elif choice == 5:
            print("Exiting Employee Panel.")
            break

        else:
            print("Invalid choice.")

# ================== LOGIN SYSTEM ==================

def login():
    emp_id = input("Enter ID: ")
    password = input("Enter Password: ")

    if emp_id.lower() == "admin" and password == ADMIN_PASSWORD:
        admin_menu()

    elif emp_id in EMPLOYEES and EMPLOYEES[emp_id] == password:
        employee_menu(emp_id)

    else:
        print("Invalid credentials.")

# ================== MAIN APP ==================

def main():
    print("===== EMPLOYEE PORTAL APPLICATION =====")
    login()

if __name__ == "__main__":
    main()

# For Render Deployment (keeps app alive)
PORT = int(os.environ.get("PORT", 10000))
