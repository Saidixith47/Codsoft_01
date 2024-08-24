import re

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define responses based on patterns
    if re.search(r'\bhello\b|\bhi\b', user_input):
        return "Hello! How can I assist you today?"

    elif re.search(r'\bwhat\s+is\s+your\s+name\b', user_input):
        return "I'm a simple chatbot created to help you. What's your name?"

    elif re.search(r'\bhow\s+are\s+you\b', user_input):
        return "I'm just a program, but I'm doing well! How can I help you?"

    elif re.search(r'\bwhat\s+can\s+you\s+do\b', user_input):
        return "I can answer basic questions and have simple conversations with you."

    elif re.search(r'\bbye\b|\bgoodbye\b', user_input):
        return "Goodbye! Have a great day!"

    elif re.search(r'\bthank\s+you\b|\bthanks\b', user_input):
        return "You're welcome! If you have any more questions, feel free to ask."

    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
