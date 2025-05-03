# 🤖 Headsquare Bot - Telegram

Este é um bot simples para o Telegram, desenvolvido em Python usando a biblioteca [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) e Chatgpt. Ele responde a comandos e mensagens de texto, servindo como base para projetos mais complexos de automação e atendimento.

---

## 🚀 Funcionalidades

- Responde ao comando `/start` com uma saudação personalizada.
- Responde  a qualquer mensagem de texto enviada pelo usuário.
- Utiliza `run_polling()` para escutar e responder em tempo real.

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Biblioteca `python-telegram-bot` v20+
- Chatgpt ('https://chatgpt.com/')
---

## 📦 Instalação

1. Clone o projeto:

   ```bash
   git clone git@github.com:seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
````

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

   ```env
   TELEGRAM_BOT_TOKEN=seu_token_aqui
   ```

5. No código Python, carregue o token usando `python-dotenv`:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
   ```

---

## ▶️ Como executar

Execute o script principal:

```bash
python nome_do_arquivo.py
```

(Substitua `nome_do_arquivo.py` pelo nome real do seu arquivo, como `bot.py`)

---

## 📄 Licença

Este projeto é de uso privado e está sob a licença MIT. Consulte o arquivo `LICENSE` se aplicável.

```

