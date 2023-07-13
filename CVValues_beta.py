# meta developer: @LolDecMods

from .. import loader, utils
import re


@loader.tds
class CurrencyModule(loader.Module):
    """Модуль для отображения текущего курса валют с бота @exchange_rates_vsk_bot\n\n(Советуем нажать в нём /start)"""

    strings = {"name": "CVValues"}

    async def cvcmd(self, message):
        """| Получение курса валют с бота.\n+Вырезанная реклама."""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "Не указаны аргументы. Укажите сумму и тип валюты (UAH, USD, EUR, RUB, GBP, ETH, BTC).")
            return

        await message.client.send_message("@exchange_rates_vsk_bot", args)

        response = await message.client.get_messages("@exchange_rates_vsk_bot", limit=1)

        if response and response[0].message:
            cleaned_message = re.sub(r"(http://|https://)\S+", "", response[0].message)
            await message.delete()
            if message.is_reply:
                replied_to_msg = await message.get_reply_message()
                await message.client.send_message(replied_to_msg.to_id, cleaned_message, reply_to=replied_to_msg.id)
            else:
                await message.client.send_message(message.to_id, cleaned_message)
        else:
            await utils.answer(message, "Не удалось получить ответ от бота.")