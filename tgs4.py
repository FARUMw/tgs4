from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client("session", api_id='21443650', api_hash='e91b8d86f0f79643e0b563f1d291fbe7')


chat_id = "@datinganon_bot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Вам найден собеседник, начинайте диалог." in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.5)
        if "Вам найден собеседник, начинайте диалог." in message.text:
                sleep(2.3)
                await app.send_sticker(chat_id, "CAACAgIAAxkBAAEIVD1kIC9a1CLD19KUU4puwmkHY0AYmgACuysAAhqR-Ejre6RfJX_-BS8E")
                sleep(2.4)

                if "Вам найден собеседник, начинайте диалог." in message.text:  # Меняем это значение если хотим спамить в другом чате
                       await app.send_message(chat_id, "/stop")
                       sleep(2.5)
                       await app.send_message(chat_id, "Найти собеседника 🔍")


app.run()
