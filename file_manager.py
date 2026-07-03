# =============================================================================
# file_manager.py
# All file read/write operations for notif.txt and list.txt.
# Centralising file I/O means missing-file errors are handled in one place.
# =============================================================================

import os
from config import NOTIF_FILE, HOLIDAY_FILE
from utils import separator


# ---------------------------------------------------------------------------
# Low-level helpers
# ---------------------------------------------------------------------------

def read_file(filepath):
    """
    Read and print the contents of a text file.
    Handles missing files and OS-level read errors gracefully.
    """
    if not os.path.exists(filepath):
        print(f"\n  [FILE ERROR] '{filepath}' not found.")
        return

    try:
        with open(filepath, "r") as f:
            content = f.read().strip()

        if not content:
            print("\n  No content available.")
        else:
            separator()
            print(content)
            separator()

    except OSError as err:
        print(f"\n  [FILE ERROR] Could not read '{filepath}': {err}")


def append_to_file(filepath, text):
    """
    Append a single non-empty line to a text file.
    Creates the file if it does not exist.

    Returns True on success, False on failure.
    """
    if not text.strip():
        print("\n  Text cannot be empty.")
        return False

    try:
        with open(filepath, "a") as f:
            f.write("\n" + text.strip())
        return True

    except OSError as err:
        print(f"\n  [FILE ERROR] Could not write to '{filepath}': {err}")
        return False


# ---------------------------------------------------------------------------
# Notifications
# ---------------------------------------------------------------------------

def display_notifications():
    """Print all notifications from notif.txt."""
    print("\n  ── NOTIFICATIONS ──")
    read_file(NOTIF_FILE)


def add_notification():
    """Prompt admin for a new notification and append it to notif.txt."""
    note = input("\n  Enter the notification to add: ").strip()
    if append_to_file(NOTIF_FILE, note):
        print("  Notification added successfully!")


# ---------------------------------------------------------------------------
# Holiday list
# ---------------------------------------------------------------------------

def display_holidays():
    """Print the holiday list from list.txt."""
    print("\n  ── HOLIDAY LIST ──")
    read_file(HOLIDAY_FILE)
