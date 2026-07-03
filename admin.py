# =============================================================================
# admin.py
# All admin-facing menus and operations.
# Admin can view employees, check health records, and manage notifications.
# =============================================================================

from database import execute_query
from file_manager import display_notifications, add_notification
from config import EMPLOYEES
from utils import separator, invalid_choice, get_int_input


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def get_health_table(emp_id):
    """Return the health table name for a given employee ID."""
    entry = EMPLOYEES.get(emp_id)
    return entry[1] if entry else None


# ---------------------------------------------------------------------------
# Employee records
# ---------------------------------------------------------------------------

def display_all_employees(conn):
    """Fetch and display all employee records from the admin table."""
    rows = execute_query(conn, "SELECT * FROM admin", fetch=True)

    if not rows:
        print("  No employee records found.")
        return

    separator()
    for row in rows:
        print(f"  Employee ID     : {row[0]}")
        print(f"  Employee Name   : {row[1]}")
        print(f"  Employee Post   : {row[2]}")
        print(f"  Employee Salary : {row[3]}")
        separator()


def view_employee_health(conn):
    """Prompt for an employee ID and display all their health records."""
    emp_id = input("\n  Enter Employee ID (Emp1 / Emp2 / Emp3 / Emp4): ").strip()
    table  = get_health_table(emp_id)

    if not table:
        print("  Invalid Employee ID.")
        return

    rows = execute_query(conn, f"SELECT * FROM {table}", fetch=True)

    if not rows:
        print(f"  No health records found for {emp_id}.")
        return

    separator()
    for row in rows:
        print(f"  Employee ID : {emp_id}")
        print(f"  Date        : {row[0]}")
        print(f"  Status      : {row[1]}")
        separator()


# ---------------------------------------------------------------------------
# Sub-menus
# ---------------------------------------------------------------------------

def notifications_menu():
    """Sub-menu: admin can read or add notifications."""
    while True:
        print("\n" + "=" * 80)
        print("  NOTIFICATIONS CENTER")
        print("=" * 80)
        print("  1. Read notifications")
        print("  2. Add notification")
        print("  3. Back")
        print("=" * 80)

        choice = get_int_input("\n  Enter choice: ")
        if choice == 1:
            display_notifications()
        elif choice == 2:
            add_notification()
        elif choice == 3:
            break
        else:
            invalid_choice()


def employee_records_menu(conn):
    """Sub-menu: admin can view all employees or check a health record."""
    while True:
        print("\n" + "=" * 80)
        print("  EMPLOYEE RECORDS")
        print("=" * 80)
        print("  1. Display all employees")
        print("  2. View employee health status")
        print("  3. Back")
        print("=" * 80)

        choice = get_int_input("\n  Enter choice: ")
        if choice == 1:
            display_all_employees(conn)
        elif choice == 2:
            view_employee_health(conn)
        elif choice == 3:
            break
        else:
            invalid_choice()


# ---------------------------------------------------------------------------
# Admin main menu
# ---------------------------------------------------------------------------

def admin_menu(conn):
    """
    Main menu loop shown to the logged-in admin.
    Runs until the admin chooses Exit.
    """
    while True:
        print("\n" + "=" * 80)
        print("  ADMIN DASHBOARD  |  Employee Management Portal")
        print("=" * 80)
        print("  1. Notifications Center")
        print("  2. Employee Records")
        print("  3. Exit")
        print("=" * 80)

        choice = get_int_input("\n  Enter choice: ")
        if choice == 1:
            notifications_menu()
        elif choice == 2:
            employee_records_menu(conn)
        elif choice == 3:
            print("\n  Goodbye, Admin!")
            break
        else:
            invalid_choice()
