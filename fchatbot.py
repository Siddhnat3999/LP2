from datetime import date, datetime
import webbrowser

# Define some responses
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "help": "Sure, I can help you with that. What do you need assistance with?",
    "goodbye": "Goodbye! Feel free to come back anytime.",
    "default": "I'm sorry, I didn't understand that. Could you please rephrase?",
    "what is date today?":str(date.today()),
    "what is time":str(datetime.now().strftime("%H:%M:%S")),
    "open youtube":["https://youtube.com"]
}

# Main function to handle user input and generate responses
def chat():
    print("Welcome to the Customer Interaction Bot. How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        response = responses.get(user_input, responses["default"])
        print("Bot:", response)
        if user_input == "goodbye":
            break
        
# Run the chatbot
chat()