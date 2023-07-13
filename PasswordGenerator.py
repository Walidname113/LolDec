# meta developer: @LolDec
# meta pic: https://www.flickr.com/photos/198729913@N04/53041989591/in/dateposted-public/

import random
import string
from hikkatl import types

from .. import loader, utils


@loader.tds
class PasswordGeneratorModule(loader.Module):
    """Модуль для генерации случайных паролей"""

    strings = {"name": "PasswordGenerator"}

    async def gpcmd(self, message: types.Message):
        """| Генерирует случайный пароль заданной длины. Пример: .gp <длина пароля (не больше 100)>"""
        length = 12
        args = utils.get_args(message)

        if args:
            try:
                length = int(args[0])
                if length < 1:
                    await utils.answer(message, "❌️Неверно указана длина пароля. Использую длину по умолчанию.❌️")
                    length = 12
                elif length > 100:
                    await utils.answer(message, "❗️Максимальная длина пароля - 100 символов. Использую максимальную длину.❗️")
                    length = 100
            except ValueError:
                await utils.answer(message, "❌️Неверно указана длина пароля. Использую длину по умолчанию.❌️")

        password = self.generate_random_password(length)
        await utils.answer(message, f"✔️Сгенерированный пароль:\n<code>{password}</code>✔️")

    def generate_random_password(self, length):
        """Генерирует случайный пароль заданной длины"""
        allowed_characters = string.ascii_letters + string.digits + "*_:@!"
        password = "".join(random.choice(allowed_characters) for _ in range(length))
        return password