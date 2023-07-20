# meta developer: @LolDecMods
# scope: MemMods
# scope: MemMods 0.0.2
from .. import loader


@loader.tds
class MemMods(loader.Module):
    """Много мемов!\nСледите за обновлениями, со временем их будет больше."""

    strings = {"name": "MemMods"}

    async def hihicmd(self, message):
        """HIHIHIHA"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/43",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def niggacmd(self, message):
        """tyanNOnigga"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/42",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
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
        
    async def oofcmd(self, message):
        """Цьом"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/59",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def naxcmd(self, message):
        """Иди нахуй"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/58",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def uffcmd(self, message):
        """Уфф"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/57",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def idycmd(self, message):
        """Иду"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/56",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def scmd(self, message):
        """Иди нахуй, сука!"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/55",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        
    async def ocmd(self, message):
        """о_0"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/54",
            voice_note=True,
            reply_to=reply.id if reply else None,
    )
