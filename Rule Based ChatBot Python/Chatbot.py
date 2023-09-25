# Build A Role Based ChatBot Operation
import re
mr
# Define a function to respond to user inputs
def chatbot(user_input):
    # Define a set of patterns and their corresponding responses
    patterns_responses = [
        (r"(hello|hi|hey)", "Hello! How can I help you?"),
        (r"how are you", "I'm just a computer program, but I'm here to help. How can I assist you?"),
        (r"what's your name|your name", "I'm a chatbot."),
        (r"what can you do", "I can provide information, answer questions, and assist with various tasks."),
        (r"bye", "Goodbye! Have a great day."),
    ]

    # Iterate through patterns and find a match in the user input
    for pattern, response in patterns_responses:
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no match is found, provide a default response
    return "I'm sorry, I don't understand that. Can you please rephrase your question?"

# Main loop for chatting
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot(user_input)
    print("Chatbot:", response)