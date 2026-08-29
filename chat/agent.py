def get_response(user_message):
    user_message = user_message.lower()

    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you?"

    elif "your name" in user_message:
        return "I am Tulsi, your AI assistant."

    elif "how are you" in user_message:
        return "I am doing great! How can I help you?"

    return "Sorry, I don't understand that yet."