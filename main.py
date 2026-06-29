import json

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from bot import ChatBot
from config import TOKEN
from datetime import datetime



chatbot = ChatBot()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now()
    current_time_string = current_time.isoformat()
    hour = current_time.hour

    welcome = ""

    if 5 <= hour < 12:
        greeting = "Good morning"

    elif 12 <= hour < 17:
        greeting = "Good afternoon"

    else:
        greeting = "Good evening"
        

    if "last_seen" in chatbot.memory:
        last_seen = datetime.fromisoformat(chatbot.memory["last_seen"])
        
        time_difference = current_time - last_seen
        seconds = time_difference.total_seconds()
            
            
        if seconds < 4 * 60 * 60:
            welcome = "Welcome back."
            
        elif seconds < 24 * 60 * 60:
            welcome = "Good to see you again."
            
        else:
            welcome = "It's good to have you back."
    
        
    message = (
        "STEM initiated.\n\n"
        "All systems online.\n\n"
        f"{greeting}, sir."
    )

    if welcome:
        message += f"\n\n{welcome}"
        
    message += "\n\nHow may I assist you today?"    
    await update.message.reply_text(message)
    
    chatbot.memory["last_seen"] = current_time_string

    with open("memory.json", "w") as file:
        json.dump(chatbot.memory, file, indent=4)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.message.text

    answer = chatbot.reply(message)

    await update.message.reply_text(answer)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    print("STEM is online...")
    app.run_polling()


if __name__ == "__main__":
    main()

