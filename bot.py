import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

# Perintah /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! 👋 Saya bot auto reply.\nKirim pesan apa saja, saya akan balas!"
    )

# Auto reply semua pesan
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pesan = update.message.text
    await update.message.reply_text(f"Kamu bilang: {pesan} 😊")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot berjalan...")
app.run_polling()
