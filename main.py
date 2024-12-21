from utils import clear_screen, load_settings, save_settings, load_chats, handle_menu
from chat import start_new_chat, resume_chat, combine_chats
from models import model_menu
from chat_management import delete_chat, delete_all_chats, view_chats
from simple_term_menu import TerminalMenu
def main_menu():
    settings = load_settings()
    chats = load_chats()

    while True:
        clear_screen()
        options = [
            "Set Model (Current: {})".format(settings["model"]),
            "Start New Chat",
            "Resume Chat",
            "View All Chats",
            "Delete a Chat",
            "Delete All Chats",
            "Combine Chats",
            "Exit",
        ]
        menu = TerminalMenu(
            options,
            title="ChatGPT CLI Menu (Escape to go back, Ctrl+D to exit):"
        )

        choice = handle_menu(menu)
        if choice is None:  # Escape pressed
            continue

        if choice == 0:
            model_menu(settings)
        elif choice == 1:
            start_new_chat(settings, chats)
        elif choice == 2:
            resume_chat(settings, chats)
        elif choice == 3:
            view_chats(chats)
        elif choice == 4:
            delete_chat(chats)
        elif choice == 5:
            delete_all_chats(chats)
        elif choice == 6:
            combine_chats(settings, chats)
        elif choice == 7:
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    try:
        main_menu()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!\n")