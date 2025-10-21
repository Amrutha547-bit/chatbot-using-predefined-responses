# %%
#import the regular expression module to handle pattern matching

import re

responses = {
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm a chatbot, so I don't have feelings, but thanks for asking!",
    "bye": "Goodbye! Have a great day!",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "name": "I'm ChatGPT, your friendly chatbot.",
    "joke": "Why don't scientists trust atoms? Because they make up everything!"
}

print("Chatbot is running. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    response = responses.get(user_input, "I'm not sure how to respond to that. Can you try something else?")
    print("Bot:", response)
    if user_input == "bye":
        break

    # Get chatbot's responsenbased on user input
    response = responses.get(user_input, "I'm not sure how to respond to that. Can you try something else?")

    #print chatbot's response
    print(f"chatbot: {response}")




