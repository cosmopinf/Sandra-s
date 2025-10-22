import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# .env fayldan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tugmalar
main_menu = [
    ["ℹ️ About", "💬 Help"],
    ["📞 Contact"]
]

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Salom! Men oddiy Telegram botman.\nQuyidagi menyudan tanlang:",
        reply_markup=reply_markup
    )

# Xabarlarni qayta ishlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "about" in text:
        await update.message.reply_text(
            "ℹ️ **Bot haqida:**\n\n"
            "Bu bot Python yordamida yaratilgan oddiy namuna bo‘lib, foydalanuvchi bilan interaktiv muloqot qilishni o‘rgatadi.\n\n"
            "Dasturlash tili: Python 🐍\nKutubxona: python-telegram-bot"
        )
    elif "help" in text:
        await update.message.reply_text(
            "💬 **Yordam:**\n\n"
            "Siz quyidagi buyruqlardan foydalanishingiz mumkin:\n"
            "/start – Botni ishga tushirish\n"
            "ℹ️ About – Bot haqida\n"
            "📞 Contact – Bizga ulanish\n\n"
            "Yoki istalgan so‘rov yuboring, men sizga javob qaytaraman 😊"
        )
    elif "contact" in text:
        await update.message.reply_text(
            "📞 **Bizga ulaning:**\n\n"
            "Email: example@email.com\n"
            "Telegram: @YourUsername\n"
            "Web: https://yourwebsite.com"
        )
    else:
        await update.message.reply_text(f"📩 Siz yozdingiz: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlerlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
