import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv

# .env fayldan TOKEN ni yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Tugmalar menyusi
main_menu = [
    ["ℹ️ Biz haqimizda", "💬 Savol va murojaatlar uchun"],
    ["📞 Biz bilan aloqa", "🤝 Hamkorlik uchun"],
]

# --- /start komandasi ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Salom! Men oddiy Telegram botman.\nQuyidagi menyudan birini tanlang:",
        reply_markup=reply_markup,
    )

# --- /help komandasi ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Yordam bo‘limi:*\n\n"
        "Quyidagi menyudan birini tanlang yoki shu komandalarni kiriting:\n"
        "• /start — Boshlash\n"
        "• /about — Biz haqimizda\n"
        "• /help — Yordam olish\n\n"
        "Savolingiz bo‘lsa, shunchaki yozing 😊",
        parse_mode="Markdown",
    )

# --- /about komandasi ---
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Biz haqimizda:*\n\n"
        "Bu bot o‘quv maqsadida yaratilgan.\n"
        "📘 Dasturlash tili: Python\n📚 Kutubxona: python-telegram-bot\n\n"
        "Biz innovatsion ta’lim, sun’iy intellekt va raqamli texnologiyalarni rivojlantirish tarafdorimiz.",
        parse_mode="Markdown",
    )

# --- Tugmalardan keladigan xabarlarni qayta ishlash ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "ℹ️ Biz haqimizda":
        await about_command(update, context)

    elif text == "💬 Savol va murojaatlar uchun":
        await update.message.reply_text(
            "💬 *Savol va murojaatlar uchun:*\n\n"
            "Agar sizda savol, taklif yoki muammo bo‘lsa — shu yerda yozishingiz mumkin.\n"
            "Biz imkon qadar tezda javob beramiz 😊",
            parse_mode="Markdown",
        )

    elif text == "📞 Biz bilan aloqa":
        await update.message.reply_text(
            "📞 *Biz bilan aloqa:*\n\n"
            "✉️ Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: [@cosmopinf](https://t.me/cosmopinf)",
            parse_mode="Markdown",
        )

    elif text == "🤝 Hamkorlik uchun":
        await update.message.reply_text(
            "🤝 *Hamkorlik uchun:*\n\n"
            "Agar siz qo‘shma loyihalarda ishtirok etmoqchi bo‘lsangiz,\n"
            "biz bilan bog‘laning:\n\n"
            "📧 Gmail: saodatalimova9@gmail.com\n"
            "💬 Telegram: [@cosmopinf](https://t.me/cosmopinf)",
            parse_mode="Markdown",
        )

    else:
        await update.message.reply_text(
            "❓ Men bu xabarni tushunmadim.\n"
            "Iltimos, menyudagi tugmalardan birini tanlang yoki /help buyrug‘ini yuboring."
        )

# --- Xatoliklarni qayta ishlovchi ---
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"⚠️ Xatolik: {context.error}")
    if isinstance(update, Update) and update.message:
        await update.message.reply_text(
            "⚠️ Kutilmagan xatolik yuz berdi. Iltimos, keyinroq urinib ko‘ring."
        )

# --- Asosiy funksiya ---
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Komanda handlerlari
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))

    # Xabar handleri
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Xatoliklarni tutish
    app.add_error_handler(error_handler)

    print("✅ Bot ishga tushdi...")
    app.run_polling()

# --- Dastur boshlanish nuqtasi ---
if __name__ == "__main__":
    main()
