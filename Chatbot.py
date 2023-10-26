import random

# List of sample responses
responses = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Nice to meet you!",
    "How can I assist you?",
    "I'm here to help!",
    "How are you today?",
]

def get_random_response():
    """Return a random response from the list of sample responses."""
    return random.choice(responses)

def chat():
    """Main function to handle the chatbot conversation."""
    print("Chatbot: " + get_random_response())

    while True:
        user_input = input("User: ")
        
        # Check if the user wants to end the conversation
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        # Generate and print a random response
        print("Chatbot: " + get_random_response())

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you?")
    chat()
