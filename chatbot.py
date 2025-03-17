def simple_chatbot():
    # Dictionary of responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a simple program, but I'm working well!",
        "name": "I'm SimpleBot, a very basic rule-based AI.",
        "age": "I was just created recently!",
        "bye": "Goodbye! Have a nice day!",
        "help": "I can respond to: hello, how are you, name, age, bye, help, what's up",
	"what's up": "Nothing"
    }
    
    print("Simple AI Chatbot")
    print("Type 'bye' to exit")
    print("Type 'help' to see what I understand")
    
    while True:
        user_input = input("\nYou: ").lower()
        
        if user_input == "bye":
            print("Bot:", responses["bye"])
            break
            
        # Check if any keywords match
        response_sent = False
        for keyword in responses:
            if keyword in user_input:
                print("Bot:", responses[keyword])
                response_sent = True
                break
                
        # Default response if no keywords match
        if not response_sent:
            print("Bot: I don't understand that yet. Type 'help' to see what I can respond to.")

if __name__ == "__main__":
    simple_chatbot()