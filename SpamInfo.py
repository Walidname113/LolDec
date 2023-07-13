# meta developer: @LoldecMods

from .. import loader, utils


@loader.tds
class SpamModule(loader.Module):
    """Модуль для получения информации о статусе аккаунта от - @SpamBot"""

    strings = {"name": "SpamInfo"}

    async def cscmd(self, message):
        """Отправляет команду /start боту @SpamBot и пересылает вам статус аккаунта."""
        await message.client.send_message("@SpamBot", "/start")
        response = await message.client.get_messages("@SpamBot", limit=1)

        if response and response[0].message:
            user_tag = ""

            if message.sender and message.sender.username:
                user_tag = f"@{message.sender.username}"

            forwarded_msg = await message.client.forward_messages(
                message.to_id, response[0], from_peer="@SpamBot"
            )

            await message.delete()

            if user_tag:
                await forwarded_msg.reply(f"{user_tag}: {response[0].message}", no_webpage=True)
            else:
                await forwarded_msg.reply(response[0].message, no_webpage=True)
        else:
            await utils.answer(message, "Не удалось получить ответ от бота @SpamBot.")
