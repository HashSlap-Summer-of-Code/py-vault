#!/usr/bin/env python3


def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hi": "Hello there!",
        "hello": "Hey! How can I help you today?",
        "how are you": "I'm just a bot, but I'm doing great! 😊",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I'm a simple Python chatbot.",
        "help": "Sure, I can help. Try saying hello or asking me how I am!",
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Hmm... I don't understand that yet. Try something else!"

def main():
    print("🤖 Chatbot: Hi! Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        response = get_response(user_input)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    main()
