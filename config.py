import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Токен вашего Telegram-бота
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")  # Ключ API GigaChat
GIGACHAT_URL = os.getenv("GIGACHAT_URL", "https://api.gigachat.dev/generate")  # URL API GigaChat
