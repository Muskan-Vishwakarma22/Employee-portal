# =============================================================================
# config.py
# Central configuration file.
# All credentials and file paths live here.
# To change DB password or file locations, edit ONLY this file.
# =============================================================================

import os

# --- Database ---
DB_CONFIG = {
    "host":     os.environ.get("DB_HOST",     "localhost"),
    "user":     os.environ.get("DB_USER",     "root"),
    "password": os.environ.get("DB_PASSWORD", "admin123"),
    "database": os.environ.get("DB_NAME",     "muskanproject"),
}

# --- Admin credentials ---
ADMIN_ID       = "admin"
ADMIN_PASSWORD = "adm34"

# --- Employee credentials: { emp_id: (password, health_table) } ---
EMPLOYEES = {
    "Emp1": ("meow123", "emp1"),
    "Emp2": ("nn123",   "emp2"),
    "Emp3": ("jivi11",  "emp3"),
    "Emp4": ("kanha22", "emp4"),
}

# --- Data file paths ---
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
NOTIF_FILE   = os.path.join(BASE_DIR, "data", "notif.txt")
HOLIDAY_FILE = os.path.join(BASE_DIR, "data", "list.txt")
