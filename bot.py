import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! 👋 Kirim pesan apa saja!")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Kamu bilang: {update.message.text} 😊")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    app.run_polling()
