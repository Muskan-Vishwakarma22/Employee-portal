# =============================================================================
# main.py
# Entry point for the Employee Management Portal.
# Run this file to start the application:  python main.py
#
# This file only does three things:
#   1. Show the banner
#   2. Open the DB connection
#   3. Route to admin or employee menu based on login
# =============================================================================

import sys

from database import get_connection
from auth import login
from admin import admin_menu
from employee import employee_menu
from utils import banner, invalid_choice


def main():
    """Start the portal: banner → login → route to correct menu."""
    banner()

    # Open one DB connection for the entire session
    conn = get_connection()
    if conn is None:
        print("\n  Cannot start portal without a database connection. Exiting.")
        sys.exit(1)

    try:
        role, emp_id = login()

        if role == "admin":
            admin_menu(conn)
        elif role == "employee":
            employee_menu(conn, emp_id)
        else:
            invalid_choice()
            print("  Invalid credentials. Program will terminate.")

    finally:
        # Always close the DB connection cleanly on exit
        if conn and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    main()
