# =============================================================================
# employee.py
# All employee-facing menus and wellness logic.
# Imports only what it needs from other modules — no circular dependencies.
# =============================================================================

from database import execute_query
from file_manager import display_notifications, display_holidays
from config import EMPLOYEES
from utils import separator, invalid_choice, get_int_input, get_yn_input, get_temperature


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def get_health_table(emp_id):
    """
    Return the MySQL table name that stores health records for emp_id.
    e.g. 'Emp1' → 'emp1'
    """
    entry = EMPLOYEES.get(emp_id)
    return entry[1] if entry else None


# ---------------------------------------------------------------------------
# Employee details
# ---------------------------------------------------------------------------

def display_own_details(conn, emp_id):
    """Fetch and display the logged-in employee's record from the admin table."""
    rows = execute_query(
        conn,
        "SELECT * FROM admin WHERE EmpId = %s",
        (emp_id,),
        fetch=True
    )

    if not rows:
        print("  No employee record found.")
        return

    separator()
    for row in rows:
        print(f"  Employee ID     : {row[0]}")
        print(f"  Employee Name   : {row[1]}")
        print(f"  Employee Post   : {row[2]}")
        print(f"  Employee Salary : {row[3]}")
    separator()


# ---------------------------------------------------------------------------
# Wellness Mitra
# ---------------------------------------------------------------------------

def view_wellness_records(conn, emp_id):
    """Display all past wellness check-in records for the employee."""
    table = get_health_table(emp_id)
    if not table:
        print("  [ERROR] Unknown employee ID.")
        return

    rows = execute_query(conn, f"SELECT * FROM {table}", fetch=True)

    if not rows:
        print("  No wellness records found.")
        return

    separator()
    for row in rows:
        print(f"  Employee ID : {emp_id}")
        print(f"  Date        : {row[0]}")
        print(f"  Status      : {row[1]}")
        separator()


def submit_wellness_checkin(conn, emp_id):
    """
    Collect today's wellness data, assess health status,
    and insert the result into the employee's health table.
    """
    print("\n  ── WELLNESS CHECK-IN ──")
    date    = input("  Enter date (YYYY-MM-DD): ").strip()
    temp    = get_temperature()

    print("\n  For the last 5 days:")
    contact = get_yn_input("  Contact with a sick person? (Y/N): ")
    sick    = get_yn_input("  Suffered from cough/cold/fever? (Y/N): ")

    # Score: each risk factor adds 1 point
    score  = sum([temp >= 100.1, contact == "Y", sick == "Y"])
    status = "Unwell" if score >= 2 else "Well"

    if status == "Unwell":
        print("\n  You are not well. Please rest and consult a doctor.")
    else:
        print("\n  Congratulations! You are fine.")

    table = get_health_table(emp_id)
    if not table:
        print("  [ERROR] Unknown employee ID.")
        return

    result = execute_query(conn, f"INSERT INTO {table} VALUES (%s, %s)", (date, status))
    if result is not None:
        print("  Health record updated successfully.")


def wellness_menu(conn, emp_id):
    """Sub-menu for the Wellness Mitra feature."""
    while True:
        print("\n" + "=" * 80)
        print("  WELLNESS MITRA")
        print("=" * 80)
        print("  1. View my wellness records")
        print("  2. Submit today's wellness check-in")
        print("  3. Back")
        print("=" * 80)

        choice = get_int_input("\n  Enter choice: ")
        if choice == 1:
            view_wellness_records(conn, emp_id)
        elif choice == 2:
            submit_wellness_checkin(conn, emp_id)
        elif choice == 3:
            break
        else:
            invalid_choice()


# ---------------------------------------------------------------------------
# Employee main menu
# ---------------------------------------------------------------------------

def employee_menu(conn, emp_id):
    """
    Main menu loop shown to a logged-in employee.
    Runs until the employee chooses Exit.
    """
    while True:
        print("\n" + "=" * 80)
        print(f"  EMPLOYEE PORTAL  |  Welcome, {emp_id}")
        print("=" * 80)
        print("  1. Display My Details")
        print("  2. Wellness Mitra")
        print("  3. Holiday List")
        print("  4. Notifications")
        print("  5. Exit")
        print("=" * 80)

        choice = get_int_input("\n  Enter choice: ")
        if choice == 1:
            display_own_details(conn, emp_id)
        elif choice == 2:
            wellness_menu(conn, emp_id)
        elif choice == 3:
            display_holidays()
        elif choice == 4:
            display_notifications()
        elif choice == 5:
            print("\n  Goodbye! Have a great day.")
            break
        else:
            invalid_choice()
