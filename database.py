# =============================================================================
# database.py
# Handles all MySQL connection and query execution.
# Every other module imports from here — no raw mysql calls elsewhere.
# =============================================================================

import mysql.connector
from config import DB_CONFIG


def get_connection():
    """
    Open and return a MySQL connection using credentials from config.py.
    Returns None if the connection fails so the caller can handle it.
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"\n  [DB ERROR] Could not connect to database: {err}")
        return None


def execute_query(conn, sql, params=None, fetch=False):
    """
    Execute a parameterized SQL query safely.

    Args:
        conn   : active MySQL connection
        sql    : SQL string with %s placeholders
        params : tuple of values to bind (prevents SQL injection)
        fetch  : True  → SELECT  → returns list of row tuples
                 False → INSERT/UPDATE → commits and returns []

    Returns None on error so callers can check for failure.
    Always closes the cursor in the finally block.
    """
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return []
    except mysql.connector.Error as err:
        print(f"\n  [DB ERROR] Query failed: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
