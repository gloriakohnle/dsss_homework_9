from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Use a pipeline as a high-level helper
from transformers import pipeline
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama_v1.1")

TOKEN: Final = '7209622006:AAEul4_miufC6ypPv3KcAPm0HMjRHPwkJGM'
BOT_USERNAME: Final = '@DataScienceGloriaBot'

# Commands
async def start(update: Update, context) -> None:
    await update.message.reply_text('Hello! Thanks for chatting with me! I am your cool AI assistant.')

async def process(update: Update, context) -> None:
    text: str = update.message.text

    print(f'User ({update.message.chat.id}): "{text}"')

    response = pipe(text, max_length = 100, num_return_sequences=1)

    generated_text = response[0]['generated_text']

    print(f'Bot: {generated_text}')

    await update.message.reply_text(generated_text)

def main():
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start)) # /start command
    app.add_handler(MessageHandler(filters.TET & ~filters.COMMAND, process)) 
    
    # Polls the bot
    print('Polling...')
    app.run_polling(poll_intervall=3) # checks every 3 seconds for messages

if __name__ == '__main__':
    main()