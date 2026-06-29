 # STEM_Core_bot

import json
# Class for defining the ChatBot
class ChatBot:
    def __init__(self):
        self.history = []

          # Execption for handling error within the self.memory 
        try:
            with open("memory.json","r") as file:
                self.memory = json.load(file)        
        except FileNotFoundError:
            self.memory = {}
        except json.JSONDecodeError:
            self.memory = {}

      # Method to handle output(reply) of stem based on user input
    def reply(self, message):
        self.history.append(message)

        if message.lower() == "hello":
            return "Hi!"
        
        # For picking the key and its value to put in the memory in dict form
        # eg; user: my name is Roqeeb, it picks the key(name) and its value(Roqeeb)
        # where self.memory = {"name": "Roqeeb"} 
        elif " is " in message.lower() and message.lower().startswith("my "):
            words = message.split()
            is_index = words.index("is")
            key = " ".join(words[1:is_index])
            value = " ".join(words[is_index+1:])
            self.memory[key] = value

             
            with open("memory.json","w") as file:
                json.dump(self.memory,file)
                # The file is automaticlly closed from here
                
            return "I'll remember that, sir."
        
        # To ask to return already given input in the given format.
        elif message.lower().startswith("what is my"):
            words = message.split()
            key = " ".join(words[3:])

            if key in self.memory:
                return f"Your {key} is {self.memory[key]}"
            else:
                return "I don't know that yet, sir."
        
        # To ask to return most recent input.
        elif message.lower() == "what did i just say":
            if len(self.history) >= 2:
                return f"You said '{self.history[-2]}', sir."
            else:
                return f"You haven't said anything before that, sir."
            
        else:
            return "I don't understand that yet, sir."

            
# Object
bot = ChatBot()

while True:
    message = input("User: ")
    answer = bot.reply(message)
    print("STEM:", answer)

b