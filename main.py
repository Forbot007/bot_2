import os
import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")
GIGACHAT_URL = os.getenv("GIGACHAT_URL", "https://api.gigachat.dev/generate")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я помогу тебе подготовиться к ОГЭ по математике. "
        "Напиши тему, по которой хочешь решать задачи (например, 'квадратные уравнения')."
    )

async def generate_task(topic: str) -> str:
    prompt = f"Сгенерируй задачу по математике для подготовки к ОГЭ на тему: {topic}. Только текст задачи, без решений."
    headers = {"Authorization": f"Bearer {GIGACHAT_API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 100}

    async with httpx.AsyncClient() as client:
        response = await client.post(GIGACHAT_URL, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get("task", "Не удалось сгенерировать задачу.")
        else:
            return "Ошибка при генерации задачи."

@dp.message()
async def task_handler(message: types.Message):
    topic = message.text
    task = await generate_task(topic)
    await message.answer(f"Реши задачу:\n{task}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
