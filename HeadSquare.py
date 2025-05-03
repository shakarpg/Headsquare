import logging
import os
import openai
from openai.error import AuthenticationError, RateLimitError
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise Exception("As variáveis de ambiente TELEGRAM_TOKEN e OPENAI_API_KEY devem estar configuradas.")

openai.api_key = OPENAI_API_KEY

# Verifica autenticação da API OpenAI
def verificar_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Teste de autenticação"}],
        )
        print("Autenticação bem-sucedida:", response)
    except AuthenticationError:
        raise Exception("Erro de autenticação: Verifique sua chave de API.")
    except RateLimitError:
        raise Exception("Erro de limite de requisições: Tente novamente mais tarde.")
    except Exception as e:
        raise Exception(f"Erro ao verificar a API da OpenAI: {e}")

verificar_openai()

# Configuração de histórico
user_conversations = {}
MAX_HISTORY = 10  # Máximo de interações a manter no histórico

# Configuração de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou um bot com inteligência do ChatGPT. Me pergunte o que quiser!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    message = update.message.text

    # Recupera ou inicia o histórico
    if user_id not in user_conversations:
        user_conversations[user_id] = []

    user_conversations[user_id].append({"role": "user", "content": message})

    # Limita o tamanho do histórico para evitar excesso de tokens
    user_conversations[user_id] = user_conversations[user_id][-MAX_HISTORY:]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=user_conversations[user_id],
        )
        reply = response['choices'][0]['message']['content']
        user_conversations[user_id].append({"role": "assistant", "content": reply})
        await update.message.reply_text(reply)
    except AuthenticationError:
        await update.message.reply_text("Erro de autenticação com a OpenAI. Verifique sua chave de API.")
    except RateLimitError:
        await update.message.reply_text("Atingimos o limite de requisições da OpenAI. Por favor, tente novamente mais tarde.")
    except Exception as e:
        logging.error(f"Erro na OpenAI: {e}")
        await update.message.reply_text("Desculpe, ocorreu um erro ao gerar a resposta. Tente novamente mais tarde.")

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot rodando...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
