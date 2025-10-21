# Azizasist Telegram Bot - Render 24/7

## Qadam 1: GitHub Repository
Repository-ga barcha fayllarni yuklang: bot.py, requirements.txt, .env.example, .render.yaml, README_UZ.txt

## Qadam 2: Render Web Service yaratish
- New Web Service → GitHub repository tanlang
- Environment: Python 3
- Build Command: pip install -r requirements.txt
- Start Command: python bot.py
- Environment Variables:
  BOT_TOKEN
  OPENAI_API_KEY
  OWNER_ID

## Qadam 3: Deploy
- Manual Deploy tugmasini bosing
- Telegram’da `/start` yozib, bot javob berishini tekshiring

## Qadam 4: Qo‘shimcha
- Auto-Deploy yoqish tavsiya etiladi
- Faqat OWNER_ID foydalanuvchi foydalanadi
