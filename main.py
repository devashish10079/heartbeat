# main.py
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from responses import get_response, get_quote, get_vent_response

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Function to log user queries
def log_query(user_id, query):
    with open("queries.log", "a") as f:
        f.write(f"User {user_id}: {query}\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hi! I'm your 24/7 relationship coach. How can I help you today?"
    )

async def advice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_response(update.message.text))

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_quote())

async def vent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(get_vent_response())

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_query(update.message.from_user.id, update.message.text)
    response = get_response(update.message.text)
    await update.message.reply_text(response)

import sys

def main() -> None:
    # Get the token from the command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <token>")
        sys.exit(1)
    token = sys.argv[1]

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("advice", advice))
    application.add_handler(CommandHandler("quote", quote))
    application.add_handler(CommandHandler("vent", vent))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
