# meta developer: @LolDecMods
# scope: MemMods
# scope: MemMods 0.0.1
from .. import loader


@loader.tds
class MemMods(loader.Module):
    """Много мемов!\nСледите за обновлениями, со временем их будет больше."""

    strings = {"name": "MemMods"}

    async def hihicmd(self, message):
        """Отправляет гс с громким хихихиха"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/43",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
    async def niggacmd(self, message):
        """Отправляет мемное видео"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/42",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
        
        
    async def bagvideocmd(self, message):
        """Отправляет багованное видео"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/44",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
        
        
   
        
