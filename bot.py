from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8709664393:AAH2Fgjvfi6gqnEUPAtwkzPGkAJtTsiBBSg"

async def her_mesaj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Konsola her gelen mesajı yaz
    print(f"GELEN: chat={update.effective_chat.id} user={update.effective_user.username if update.effective_user else 'yok'} text={update.message.text if update.message else 'yok'}")
    
    # Sadece grupta çalışsın, özel mesajlara cevap vermesin
    if update.effective_chat.type not in ["group", "supergroup"]:
        print("Özel mesaj, grupta değil.")
        return
    
    # Cevap mesajı
    keyboard = [
        [InlineKeyboardButton("🍀 TIKLA SİPARİŞ VER 🍀", url="https://t.me/laylowcommercial")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "⭐️ GRUBUMUZA HOŞGELDİNİZ.\n\n"
        "NE LAZIMSA ADMİNLERE YAZIN.\n\n"
        "Admin: @laylowcommercial",
        reply_markup=reply_markup
    )
    print("CEVAP VERDİ")

def main():
    app = Application.builder().token(TOKEN).build()
    # TÜM mesajları yakala (text, foto, her şey)
    app.add_handler(MessageHandler(filters.ALL, her_mesaj))
    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()