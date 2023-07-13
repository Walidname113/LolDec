# meta developer: @LolDecMods

from .. import loader


@loader.tds
class sssrv(loader.Module):
    """Отправляет различные видео/гс."""

    strings = {"name": "ssrv"}

    async def ssrvacmd(self, message):
        """| Отправляет гс с ссср-эдит звуком"""
        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/filechannelscp/29",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )

    async def ssrvbcmd(self, message):
        """| Отправляет гс с БАС-БУСТ ссср-эдит звуком."""
        reply = await message.get_reply_message()
        await message.delete()
        audio_link = "https://t.me/filechannelscp/14"
        await message.client.send_file(
            message.to_id,
            audio_link,
            voice_note=True,
            reply_to=reply.id if reply else None,
        )

    async def ssrvcmd(self, message):
        """| Отправляет видео-сообщение с эдитом про политиков в виде скелета"""
        reply = await message.get_reply_message()
        await message.delete()
        video_link = "https://t.me/filechannelscp/15"
        await message.client.send_file(
            message.to_id,
            video_link,
            video_note=True,
            reply_to=reply.id if reply else None,
        )

    async def ssrvdcmd(self, message):
        """| Отправляет видео-сообщение с эдитом про немецких войск WW2"""
        reply = await message.get_reply_message()
        await message.delete()
        video_link = "https://t.me/filechannelscp/16"
        await message.client.send_file(
            message.to_id,
            video_link,
            video_note=True,
            reply_to=reply.id if reply else None,
        )

    async def ssrvncmd(self, message):
        """| Отправляет видео-сообщение с эдитом про танк"""
        reply = await message.get_reply_message()
        await message.delete()
        video link = "https://t.me/filechannelscp/31"
        await message.client.send_file(
            message.to_id,
            video_link,
            video_note=True,
            reply_to=reply.id if reply else None,
        )

    async def ssrvrcmd(self, message):
        """| Отправляет видео-сообщение с эдитом про пистолет"""
        reply = await message.get_reply_message()
        await message.delete()
        video_link = "https://t.me/filechannelscp/32"
        await message.client.send_file(
            message.to_id,
            video_link,
            video_note=True,
            reply_to=reply.id if reply else None,
        )
