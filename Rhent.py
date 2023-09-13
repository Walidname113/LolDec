import random
from telethon.tl import types

from .. import loader, utils

@loader.tds
class HentaiHm(loader.Module):
    "Получает случайное хентай-медиа. СТРОГО 18+."
    strings = {"name": "RandomHentai"}
        
    async def ghentcmd(self, m: types.Message):
        "Получить хентай-медиа."
        channel_username = "@sidjejdi3nfjeoso"
        channel_entity = await self.client.get_entity(channel_username)
        messages = await self.client.get_messages(channel_entity, limit=100)
        random_message = random.choice(messages)
        await utils.answer(m, random_message)
        await m.delete() 