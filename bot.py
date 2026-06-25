 # STEM_Core_bot

import json
# Class for defining the ChatBot
class ChatBot:
    def __init__(self):
        self.history = []

        try:
            with open("memory.json","r") as file:
                self.memory = json.load(file)        
        except FileNotFoundError:
            self.memory = {}
        except json.JSONDecodeError:
            self.memory = {}

    def reply(self, message):
        self.history.append(message)

        if message.lower() == "hello":
            return "Hi!"
        
        elif " is " in message.lower() and message.lower().startswith("my "):
            words = message.split()
            is_index = words.index("is")
            key = " ".join(words[1:is_index])
            value = " ".join(words[is_index+1:])
            self.memory[key] = value

            with open("memory.json","w") as file:
                json.dump(self.memory,file)
                return "I'll remember that, sir."
        
        elif message.lower().startswith("what is my"):
            words = message.split()
            key = " ".join(words[3:])

            if key in self.memory:
                return f"Your {key} is {self.memory[key]}"
            else:
                return "I don't know that yet, sir."
        else:
            return "I don't understand that yet, sir."

            
# Object
bot = ChatBot()

while True:
    message = input("User: ")
    answer = bot.reply(message)
    print("STEM:", answer)

