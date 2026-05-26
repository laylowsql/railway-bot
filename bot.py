import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Proxy - sadece lokalde Tor varsa aktif
PROXY = os.environ.get("PROXY")
if PROXY:
    os.environ["HTTP_PROXY"] = PROXY
    os.environ["HTTPS_PROXY"] = PROXY

TOKEN = os.environ.get("TOKEN") or "8709664393:AAH2Fgjvfi6gqnEUPAtwkzPGkAJtTsiBBSg"

async def her_mesaj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type not in ["group", "supergroup"]:
        return
    
    keyboard = [
        [InlineKeyboardButton("🍀 TIKLA SİPARİŞ VER 🍀", url="https://t.me/laylowcommercial")],
        [InlineKeyboardButton("🍀 ONAYLI SATICI 🍀", url="https://t.me/muko1998")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "⭐️ GRUBUMUZA HOŞGELDİNİZ.\n\n"
        "NE LAZIMSA ADMİNLERE YAZIN, ADMİNLERDEN VEYA ONAYLI SATICILARDAN YAPMADIĞINIZ SATIN ALIMLARDAN GRUBUMUZ SORUMLU DEĞİLDİR.\n\n"
        "Admin: @laylowcommercial \n\n"
        "Onaylı satıcı: @muko1998",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, her_mesaj))
    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()