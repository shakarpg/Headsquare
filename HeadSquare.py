from telegram import Update # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters # type: ignore

# Substitua pelo seu token do BotFather
TOKEN = '7976061331:AAGRGBuoYFiKoWDnpnIgySIZ-7Ys4p91164'

# Função que responde ao comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou Headsquare. Como posso ajudar?')

# Função que responde a qualquer mensagem
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá, mundo!')

def main():
    # Cria a aplicação do bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Comando /start
    app.add_handler(CommandHandler("start", start))
    # Responde a qualquer mensagem
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Inicia o bot
    app.run_polling()

if __name__ == '__main__':
    main()