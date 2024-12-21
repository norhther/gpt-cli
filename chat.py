from utils import save_chats, clear_screen, handle_menu
from openai import OpenAI
import os
import dotenv
from simple_term_menu import TerminalMenu

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("TOKEN"))

def ask_chatgpt(model, system_prompt, user_message, history):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                *history,
                {"role": "user", "content": user_message},
            ],
            max_tokens=4096,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def start_new_chat(settings, chats):
    clear_screen()
    history = []
    system_prompt = "You are an assistant. Answer concisely."
    print("\n--- New Chat ---\nType 'exit' to end the chat.\n")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("\nExiting chat...\n")
            break

        history.append({"role": "user", "content": user_message})
        assistant_response = ask_chatgpt(settings["model"], system_prompt, user_message, history)
        print(f"Assistant: {assistant_response}\n")
        history.append({"role": "assistant", "content": assistant_response})

    if history:
        title = history[0]["content"][:50]
        chats.append({"title": title, "history": history})
        save_chats(chats)
        print(f"\nChat saved as: {title}\n")
def resume_chat(settings, chats):
    clear_screen()
    if not chats:
        print("\nNo chats available to resume.\n")
        input("\nPress Enter to return to the main menu...")
        clear_screen()
        return

    options = [f"{i + 1}. {chat['title']}" for i, chat in enumerate(chats)]
    menu = TerminalMenu(
        options,
        title="Select a chat to resume (Escape to go back, Ctrl+D to exit):"
    )

    choice = handle_menu(menu, go_back_message="Returning to the main menu...")
    if choice is None:  # Escape pressed
        clear_screen()
        return

    chat = chats[choice]
    history = chat["history"]
    system_prompt = "You are an assistant. Answer concisely."

    clear_screen()
    print(f"\n--- Resuming Chat: {chat['title']} ---\nType 'exit' to end the chat.\n")
    print("--- Chat History ---\n")
    for message in history:
        role = message["role"].capitalize()
        print(f"{role}: {message['content']}\n")
    print("--- End of History ---\n")

    while True:
        user_message = input("You: ")
        if user_message.lower() in ["exit", "quit"]:
            print("\nExiting chat...\n")
            break

        history.append({"role": "user", "content": user_message})
        assistant_response = ask_chatgpt(settings["model"], system_prompt, user_message, history)
        print(f"Assistant: {assistant_response}\n")
        history.append({"role": "assistant", "content": assistant_response})

    chat["history"] = history
    save_chats(chats)
    print("\nChat updated.\n")
    input("\nPress Enter to return to the main menu...")
    clear_screen()


def combine_chats(settings, chats):
    clear_screen()
    if len(chats) < 2:
        print("\nNeed at least two chats to combine.\n")
        return

    options = [f"{i + 1}. {chat['title']}" for i, chat in enumerate(chats)]
    menu = TerminalMenu(options, title="Select chats to combine (Ctrl+Space to multi-select):", multi_select=True)
    choices = menu.show()

    if choices:
        combined_history = []
        for choice in choices:
            combined_history.extend(chats[choice]["history"])
        system_prompt = "You are an assistant. Answer concisely."
        print("\n--- Combined Chat ---\nType 'exit' to end the chat.\n")

        while True:
            user_message = input("You: ")
            if user_message.lower() in ["exit", "quit"]:
                print("\nExiting combined chat...\n")
                break

            combined_history.append({"role": "user", "content": user_message})
            assistant_response = ask_chatgpt(settings["model"], system_prompt, user_message, combined_history)
            print(f"Assistant: {assistant_response}\n")
            combined_history.append({"role": "assistant", "content": assistant_response})

        title = "Combined Chat"
        chats.append({"title": title, "history": combined_history})
        save_chats(chats)
        print(f"\nCombined chat saved as: {title}\n")
