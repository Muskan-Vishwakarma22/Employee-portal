# =============================================================================
# auth.py
# Handles all login and credential validation.
# Keeping auth separate means you can swap the login mechanism later
# (e.g. hashed passwords, DB-stored credentials) without touching menus.
# =============================================================================

from config import ADMIN_ID, ADMIN_PASSWORD, EMPLOYEES
from utils import separator


def login():
    """
    Display the login prompt and validate credentials.

    Returns:
        (role, emp_id) where role is 'admin' or 'employee'.
        Returns (None, None) if credentials are wrong.
    """
    print("\n" + "=" * 80)
    print("                            LOG IN")
    print("=" * 80)

    emp_id   = input("  Enter Employee ID : ").strip()
    password = input("  Enter Password    : ").strip()

    # Check admin credentials
    if emp_id.lower() == ADMIN_ID and password == ADMIN_PASSWORD:
        return "admin", emp_id

    # Check employee credentials
    creds = EMPLOYEES.get(emp_id)
    if creds and creds[0] == password:
        return "employee", emp_id

    return None, None
