import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# .env fayldan tokenni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tugmalar
main_menu = [
    ["ℹ️ Biz haqimizda", "💬 Savol va murojaatlar uchun"],
    ["📞 Biz bilan aloqa", "🤝 Hamkorlik uchun"]
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

    if "biz haqimizda" in text:
        await update.message.reply_text(
            "ℹ️ **Biz haqimizda:**\n\n"
            "Bu bot foydalanuvchilar bilan interaktiv muloqot qilishni namoyish etish uchun yaratilgan.\n"
            "Dasturlash tili: Python 🐍\nKutubxona: python-telegram-bot\n\n"
            "Biz innovatsion ta’lim va texnologik loyihalarni rivojlantirishga e’tibor qaratamiz."
        )

    elif "savol" in text or "murojaat" in text:
        await update.message.reply_text(
            "💬 **Savol va murojaatlar uchun:**\n\n"
            "Siz bot orqali o‘z fikringiz, taklifingiz yoki savollaringizni yozishingiz mumkin.\n"
            "Biz imkon qadar tezroq javob beramiz. 😊"
        )

    elif "aloqa" in text:
        await update.message.reply_text(
            "📞 **Biz bilan aloqa:**\n\n"
            "✉️ Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: @cosmopinf"
        )

    elif "hamkorlik" in text:
        await update.message.reply_text(
            "🤝 **Hamkorlik uchun:**\n\n"
            "Agar siz hamkorlik qilishni xohlasangiz yoki qo‘shma loyihalar haqida gaplashmoqchi bo‘lsangiz,\n"
            "biz bilan quyidagi manzillar orqali bog‘laning:\n\n"
            "📧 Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: @cosmopinf"
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
