# meta developer: @LolDec

import asyncio
from hikkatl import types
from telethon import functions

from .. import loader, utils


@loader.tds
class SendMessageModule(loader.Module):
    """Модуль для автоматического получения карт каждые 4 часа в боте @Aniversecard_bot"""

    strings = {"name": "AniverseAuto"}

    def __init__(self):
        self.running = False 
        self.success_message = "<b>🏗Успешно запущено<b>"
        self.already_running_message = "❌️Уже запущено"

    @loader.unrestricted
    async def runancmd(self, message: types.Message):
        """Запускает отправку сообщения 'Получить карту' каждые 4 часа"""
        if self.running:
            await utils.answer(message, self.already_running_message)
            return
        self.running = True

        await utils.answer(message, self.success_message)

        while self.running:
            await message.client(functions.messages.SendMessageRequest(
                peer='aniversecard_bot',
                message='Получить карту'
            ))

            await asyncio.sleep(4 * 60 * 60)

    @loader.unrestricted
    async def stopnancmd(self, message: types.Message):
        """Останавливает отправку сообщения 'Получить карту'"""
        if not self.running:
            await utils.answer(message, "❌️Отправка уже остановлена.")
            return
        self.running = False
        await utils.answer(message, "✔️Отправка остановлена.")

    @loader.unrestricted
    async def command(self, message: types.Message):
        """Отправляет сообщение 'Получить карту' пользователю @aniversecard_bot"""
        await message.client(functions.messages.SendMessageRequest(
            peer='aniversecard_bot',
            message='Получить карту'
        ))
