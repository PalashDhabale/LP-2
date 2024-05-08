from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chatbot
chatbot = ChatBot('HotelMenuBot')

# Train the chatbot with some sample conversations
trainer = ListTrainer(chatbot)
trainer.train([
    "What do you have for breakfast?",
    "For breakfast, we have pancakes, eggs, bacon, cereal, and fruit.",
    "What are the options for lunch?",
    "Our lunch menu includes sandwiches, salads, soups, pasta, and burgers.",
    "Can you tell me about dinner?",
    "Sure, our dinner menu offers steak, seafood, chicken dishes, vegetarian options, and desserts.",
    "What about drinks?",
    "We have a variety of beverages including soft drinks, juices, cocktails, wine, and beer.",
    "Do you offer any specials?",
    "Yes, we have daily specials which vary. You can ask the server for today's special.",
    "Thank you!",
    "You're welcome! If you have any more questions, feel free to ask."
])

# Get responses from the chatbot
response = chatbot.get_response("What do you have for breakfast?")
print(response)
response = chatbot.get_response("Can you tell me about dinner?")
print(response)
response = chatbot.get_response("Do you offer any specials?")
print(response)
