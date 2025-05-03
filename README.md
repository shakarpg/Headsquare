# 🤖 Headsquare Bot - Telegram

Este é um bot simples para o Telegram, desenvolvido em Python usando a biblioteca `python-telegram-bot`. Ele responde a comandos e mensagens de texto, servindo como base para projetos mais complexos de automação e atendimento.

## 🚀 Funcionalidades

- Responde ao comando `/start` com uma saudação personalizada.
- Responde com `"Olá, mundo!"` a qualquer mensagem de texto enviada pelo usuário.
- Utiliza `run_polling()` para escutar e responder em tempo real.

## 🔒 Projeto Privado

Este repositório está em modo **privado**, garantindo que o token do bot e outras informações sensíveis não sejam acessíveis publicamente. Mesmo assim, recomendamos:

- **Não versionar diretamente tokens ou senhas.**
- **Usar variáveis de ambiente** com um arquivo `.env` para segurança adicional.

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Biblioteca [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) v20+

## 📦 Instalação

1. Clone o projeto:
   ```bash
   git clone git@github.com:seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   
2.Crie um ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3.Instale as dependências:
   pip install -r requirements.txt

4.Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
   TELEGRAM_BOT_TOKEN=seu_token_aqui

5.No código Python, carregue o token usando python-dotenv:
   from dotenv import load_dotenv
   import os

   load_dotenv()
   TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

▶️ Como executar
   python nome_do_arquivo.py

📄 Licença
   Este projeto é de uso privado e está sob a licença MIT. Consulte LICENSE se aplicável.
