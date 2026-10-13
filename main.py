import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = "https://shawunahamed899-cmd.github.io/shawun-earn/"

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🚀 Open App - Earn Now", web_app=WebAppInfo(url=APP_URL))],
        [InlineKeyboardButton("💰 Balance"), InlineKeyboardButton("👥 Refer & Earn")],
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/")]
    ]
    text = "🚀 Welcome to Shawun Earn!\n\n🎁 $12.50 Bonus\n🎬 Watch 10 Ads = Income\n👥 Refer = $1 Bonus\n\n👇 Niche Open App e chap dao!"
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
print("Bot Running...")
app.run_polling()
