import os
from dotenv import load_dotenv
from openai import OpenAI
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# .env fayldan ma'lumotlarni yuklaymiz
load_dotenv()

BOT_TOKEN = os.getenv("8358036357:AAFCauZkwF4FiS7sbpOAVIjbYHMk1f5hfLo")
OPENAI_KEY = os.getenv("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")

if not OPENAI_KEY:
    raise ValueError("❌ OPENAI_API_KEY topilmadi. Iltimos .env faylni tekshiring!")

client = OpenAI(api_key=OPENAI_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom Aziz! Men sizning shaxsiy AI yordamchingman 🇺🇿")

async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Siz foydalanuvchiga O'zbek tilida yordam beruvchi AI yordamchisiz."},
            {"role": "user", "content": user_message}
        ]
    )
    await update.message.reply_text(response.choices[0].message["content"])

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat))
    app.run_polling()

if __name__ == "__main__":
    main()
