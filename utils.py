# =============================================================================
# utils.py
# Shared UI utility functions used across all modules.
# Centralising these avoids copy-pasting print statements everywhere.
# =============================================================================


def separator():
    """Print a horizontal divider line."""
    print("-" * 80)


def banner():
    """Display the ASCII-art welcome banner on startup."""
    print("*" * 106)
    print("***                                                                                                      ***")
    print(r"***                  \              / _____ |      /--\    -    |\    /|  _____                          ***")
    print(r"***                   \            / |      |     /--    -   -  | \  / | |                               ***")
    print(r"***                    \    /\    /  |_____ |    |--    -     - |  \/  | |_____                          ***")
    print(r"***                     \  /  \  /   |      |     \--    -   -  |      | |                               ***")
    print(r"***                      \/    \/    |_____ |____  \--/    -    |      | |_____                          ***")
    print("***                                                                                                      ***")
    print("***                                       -------     -                                                  ***")
    print("***                                          |      -   -                                                ***")
    print("***                                          |     -     -                                               ***")
    print("***                                          |      -   -                                                ***")
    print("***                                          |        -                                                  ***")
    print("***                                                                                                      ***")
    print(r"***                   _____                                      _____   _____                           ***")
    print(r"***                  |       |\    /|  |---  |      /--\  \   / |       |                                ***")
    print(r"***                  |_____  | \  / |  |   } |     |    |  \ /  |_____  |_____                           ***")
    print(r"***                  |       |  \/  |  |---  |     |    |   |   |       |                                ***")
    print(r"***                  |_____  |      |  |     |____  \--/    |   |_____  |_____                           ***")
    print("***                                                                                                      ***")
    print("***                                                                                                      ***")
    print(r"***                              |---   /--\   |---  -----    /\    |                                    ***")
    print(r"***                              |   } |    |  |   }   |     /  \   |                                    ***")
    print(r"***                              |---  |    |  |---    |    /----\  |                                    ***")
    print(r"***                              |      \--/   |   \   |   /      \ |____                                ***")
    print("***                                                                                                      ***")
    print("*" * 106)


def invalid_choice():
    """Print a styled INVALID INPUT message."""
    print()
    print(r"| |\  | \    /  /\   |    | |--      | |\  | |\ |  | ---")
    print(r"| | \ |  \  /  /__\  |    | |   )    | | \  | |/ |  |  | ")
    print(r"| |  \|   \/  /    \ |___ | |--      | |  \| |  |__|  | ")
    print()


def get_int_input(prompt):
    """
    Prompt for an integer menu choice.
    Returns the integer, or None if the user types something non-numeric.
    Callers should treat None as an invalid choice.
    """
    try:
        return int(input(prompt))
    except ValueError:
        invalid_choice()
        return None


def get_yn_input(prompt):
    """
    Keep prompting until the user enters Y or N (case-insensitive).
    Returns 'Y' or 'N'.
    """
    while True:
        answer = input(prompt).strip().upper()
        if answer in ("Y", "N"):
            return answer
        print("  Please enter Y or N.")


def get_temperature():
    """
    Keep prompting until a valid float temperature is entered.
    Returns the temperature as a float.
    """
    while True:
        try:
            return float(input("  Enter your body temperature in Fahrenheit: "))
        except ValueError:
            print("  Invalid temperature. Please enter a number (e.g. 98.6).")
