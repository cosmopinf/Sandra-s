import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tugmalar
main_menu = [["ℹ️ About", "💬 Help"], ["📞 Contact"]]

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Hello! I'm your simple Telegram bot.\nChoose an option:",
        reply_markup=reply_markup
    )

# Xabarlarni qayta ishlash
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "about" in text:
        await update.message.reply_text("I'm a demo bot created for learning purposes.")
    elif "help" in text:
        await update.message.reply_text("Just send me any message and I’ll echo it back!")
    elif "contact" in text:
        await update.message.reply_text("You can contact the developer at example@email.com.")
    else:
        await update.message.reply_text(f"You said: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
