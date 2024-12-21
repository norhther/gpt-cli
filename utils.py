import os
import json

SETTINGS_FILE = "settings.json"
CHATS_FILE = "chats.json"

DEFAULT_SETTINGS = {"model": "gpt-4o-mini"}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as f:
            json.dump(DEFAULT_SETTINGS, f)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f)

def load_chats():
    if os.path.exists(CHATS_FILE):
        with open(CHATS_FILE, "r") as f:
            return json.load(f)
    return []

def save_chats(chats):
    with open(CHATS_FILE, "w") as f:
        json.dump(chats, f)

def handle_menu(menu, go_back_message="Returning to the previous menu...", exit_message="Exiting program..."):
    """
    Handle menu interaction with Escape and Ctrl+D support.
    - Escape: Return to the previous menu.
    - Ctrl+D: Exit the program.
    """
    try:
        choice = menu.show()
        if choice is None:  # Escape key pressed
            print(f"\n{go_back_message}\n")
            return None
        return choice
    except EOFError:  # Ctrl+D pressed
        print(f"\n{exit_message}\n")
        exit(0)
