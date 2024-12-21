from simple_term_menu import TerminalMenu
from utils import save_chats, clear_screen, load_chats, handle_menu

def delete_chat(chats):
    clear_screen()
    if not chats:
        print("\nNo chats available to delete.\n")
        return

    options = [f"{i + 1}. {chat['title']}" for i, chat in enumerate(chats)]
    menu = TerminalMenu(options, title="Select chats to delete (Ctrl+Space to multi-select):", multi_select=True)
    selected_indices = menu.show()

    if selected_indices:
        deleted_chats = [chats.pop(index) for index in sorted(selected_indices, reverse=True)]
        save_chats(chats)
        print("\nDeleted chats:")
        for chat in deleted_chats:
            print(f"- {chat['title']}")
    else:
        print("\nNo chats were deleted.\n")


def delete_all_chats(chats):
    clear_screen()
    if not chats:
        print("\nNo chats available to delete.\n")
        return

    confirmation = input("Are you sure you want to delete all chats? (yes/no): ")
    if confirmation.lower() == "yes":
        chats.clear()
        save_chats(chats)
        print("\nAll chats have been deleted.\n")
    else:
        print("\nNo chats were deleted.\n")


def view_chats(chats):
    clear_screen()
    if not chats:
        print("\nNo chats available.\n")
        input("\nPress Enter to return to the main menu...")
        # clear screen
        clear_screen()
        return

    options = [f"{i + 1}. {chat['title']}" for i, chat in enumerate(chats)]
    menu = TerminalMenu(
        options,
        title="Select a chat to view (Escape to go back, Ctrl+D to exit):"
    )

    while True:
        selected_index = handle_menu(menu, go_back_message="Returning to main menu...")
        if selected_index is None:  # Escape pressed
            return

        selected_chat = chats[selected_index]
        clear_screen()

        print(f"--- Chat: {selected_chat['title']} ---\n")
        for message in selected_chat["history"]:
            role = message["role"].capitalize()
            print(f"{role}: {message['content']}\n")

        input("\nPress Enter to return to the chat selection menu...")
        clear_screen()

