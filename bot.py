 # STEM_Core_bot

# Class for defining the ChatBot
class ChatBot:
    def __init__(self):
        self.memory = {}
        self.history = []

    def reply(self, message):

        if message.lower() == "hello":
            return "Hi!"
        
        elif "my name is" in message.lower():
            words = message.split()
            name = words[3]
            self.memory["name"] = name
            return f"Nice to meet you {name}"
        
        elif message.lower() =="what is my name":

            if "name" in self.memory:
                return f"Your name is {self.memory['name']}"
            else:
                return "I don't understand."

            
# Object
bot = ChatBot()

while True:
    message = input("User: ")
    answer = bot.reply(message)
    print("STEM:", answer)

