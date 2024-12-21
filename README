# ChatGPT CLI

This project is a command-line interface (CLI) application that integrates OpenAI's API for creating and managing chat conversations. It offers a user-friendly menu system for interacting with a chatbot, resuming previous chats, and managing chat history.

## Features

- **Start New Chats**: Initiate a new conversation with the chatbot.
- **Resume Chats**: View and continue previous conversations.
- **View Chat History**: Browse saved chats and view full conversation details.
- **Delete Chats**: Remove individual or multiple chat records.
- **Delete All Chats**: Clear all saved conversations.
- **Combine Chats**: Merge multiple chat histories into a single conversation.
- **Set Chat Model**: Select from a variety of models to customize chatbot behavior.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Configure your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```env
     TOKEN=your_openai_api_key_here
     ```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

- **Set Model**: Change the model used for chat completion (e.g., `gpt-4`, `gpt-3.5-turbo`).
- **Start New Chat**: Start a fresh conversation with the chatbot.
- **Resume Chat**: Select and continue a saved conversation. Previous messages are displayed for context.
- **View All Chats**: View a list of all saved chats and their full content.
- **Delete a Chat**: Remove selected chats from history.
- **Delete All Chats**: Clear all saved chats.
- **Combine Chats**: Merge multiple chat histories into one.
- **Exit**: Quit the application. Use `Escape` to go back or `Ctrl+D` to exit directly.

## File Structure

- **`cli_main.py`**: Main entry point for the application.
- **`chat.py`**: Contains functions for managing chat interactions.
- **`utils.py`**: Utility functions for clearing the screen, loading/saving data, and handling menus.
- **`chat_management.py`**: Functions for managing chat deletion and viewing history.
- **`models.py`**: Model selection and configuration.
- **`settings.json`**: Stores user preferences such as the selected model.
- **`chats.json`**: Stores chat histories.
