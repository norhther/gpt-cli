from utils import save_settings, clear_screen
from simple_term_menu import TerminalMenu

def model_menu(settings):
    """Display a menu to select a model and save the selection."""
    clear_screen()
    options = ["gpt-4o", "chatgpt-4o-latest", "gpt-4o-mini", "o1", "o1-preview", "o1-mini", "gpt-3.5-turbo"]
    menu = TerminalMenu(options, title="Select a model:")
    choice = menu.show()

    if choice is not None:
        settings["model"] = options[choice]
        save_settings(settings)
        print(f"\nModel set to: {settings['model']}\n")
    else:
        print("\nNo selection made. Returning to the main menu.\n")
    input("\nPress Enter to continue...")
