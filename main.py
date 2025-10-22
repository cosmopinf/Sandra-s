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
        "👋 Salom! Men oddiy Telegram botman.\nQuyidagi menyudan birini tanlang:",
        reply_markup=reply_markup
    )

# Xabarlarni qayta ishlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "ℹ️ Biz haqimizda":
        await update.message.reply_text(
            "ℹ️ **Biz haqimizda:**\n\n"
            "Bu bot foydalanuvchilar bilan interaktiv muloqotni o‘rganish va ko‘rsatish maqsadida yaratilgan.\n"
            "Dasturlash tili: Python 🐍\nKutubxona: python-telegram-bot\n\n"
            "Biz innovatsion ta’lim, sun’iy intellekt va raqamli texnologiyalarni targ‘ib qilamiz."
        )

    elif text == "💬 Savol va murojaatlar uchun":
        await update.message.reply_text(
            "💬 **Savol va murojaatlar uchun:**\n\n"
            "Agar sizda savol, taklif yoki muammo bo‘lsa, shu yerda yozishingiz mumkin.\n"
            "Biz imkon qadar tezda javob beramiz 😊"
        )

    elif text == "📞 Biz bilan aloqa":
        await update.message.reply_text(
            "📞 **Biz bilan aloqa:**\n\n"
            "✉️ Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: @cosmopinf"
        )

    elif text == "🤝 Hamkorlik uchun":
        await update.message.reply_text(
            "🤝 **Hamkorlik uchun:**\n\n"
            "Agar siz hamkorlik yoki qo‘shma loyihalarda ishtirok etmoqchi bo‘lsangiz,\n"
            "quyidagi manzillar orqali bog‘laning:\n\n"
            "📧 Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: @cosmopinf"
        )

    else:
        await update.message.reply_text(
            "❓ Iltimos, quyidagi menyudan tanlang yoki /start buyrug‘ini kiriting."
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlerlar
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
