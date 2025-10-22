import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# .env fayldan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tugmalar
main_menu = [
    ["ℹ️ Biz haqimizda", "💬 Savol va murojatlar uchun"],
    ["📞  Biz bilan aloqa "]
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
            "ℹ️ **Biz haqimizda:**\n\n"
            "Bu bot Python yordamida yaratilgan oddiy namuna bo‘lib, foydalanuvchi bilan interaktiv muloqot qilishni o‘rgatadi.\n\n"
            "Dasturlash tili: Python 🐍\nKutubxona: python-telegram-bot"
        )
    elif "help" in text:
        await update.message.reply_text(
            "💬 **Savol va murojatlar uchun:**\n\n"
            "Siz quyidagi buyruqlardan foydalanishingiz mumkin:\n"
            "/start – Botni ishga tushirish\n"
            "ℹ️ Biz haqimizda – Bot haqida\n"
            "📞 Biz bilan aloqa – Bizga ulanish\n\n"
            "Yoki istalgan so‘rov yuboring, men sizga javob qaytaraman 😊"
        )
    elif "contact" in text:
        await update.message.reply_text(
            "📞 **Bizga ulaning:**\n\n"
            "Email: saodatalimova9@gmail.com\n"
            "Telegram: @cosmopinf\n"
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
