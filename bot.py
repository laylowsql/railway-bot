import os
import time
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, ChatMemberHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN") or "8709664393:AAH2Fgjvfi6gqnEUPAtwkzPGkAJtTsiBBSg"
ALISVERIS_TOPIC_ID = 5
last_message_time = 0

def get_welcome_markup():
    keyboard = [
        [InlineKeyboardButton("🍀 TIKLA SİPARİŞ VER 🍀", url="https://t.me/laylowcommercial")],
        [InlineKeyboardButton("🍀 ONAYLI SATICI 🍀", url="https://t.me/feelingrinchy")]
    ]
    return InlineKeyboardMarkup(keyboard)

WELCOME_TEXT = (
    "⭐️ GRUBUMUZA HOŞGELDİNİZ.\n\n"
    "NE LAZIMSA ADMİNLERE YAZIN, ADMİNLERDEN VEYA ONAYLI SATICILARDAN YAPMADIĞINIZ SATIN ALIMLARDAN GRUBUMUZ SORUMLU DEĞİLDİR.\n\n"
    "KEYİFLİ DUMANLAR DİLERİZ\n\n"
    "Admin: @laylowcommercial \n\n"
    "Onaylı satıcı: @feelingrinchy"
)

async def mesaj_kontrol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_message_time
    if update.effective_chat.type not in ["group", "supergroup"]:
        return

    if ALISVERIS_TOPIC_ID != 0 and update.message.message_thread_id != ALISVERIS_TOPIC_ID:
        return

    current_time = time.time()
    if current_time - last_message_time < 10:
        return

    last_message_time = current_time

    await update.message.reply_text(WELCOME_TEXT, reply_markup=get_welcome_markup())

async def yeni_uye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type not in ["group", "supergroup"]:
        return

    if not update.chat_member:
        return

    old_status = update.chat_member.old_chat_member.status
    new_status = update.chat_member.new_chat_member.status

    if old_status != "member" and new_status == "member":
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=WELCOME_TEXT,
            reply_markup=get_welcome_markup()
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj_kontrol))
    app.add_handler(ChatMemberHandler(yeni_uye))
    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()