def get_response(user_input):
    
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I'm a simple chatbot."
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def chatbot():
   
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if user_input.lower().strip() == "bye":
            break


chatbot()