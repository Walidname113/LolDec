import os
import aiohttp
import random
from urllib.parse import urlparse

from hikkatl.types import Message

from .. import loader, utils

@loader.tds
class ModuleName(loader.Module):
    """Позволяет получить HTML-код с сайта либо страницы сайта."""

    strings = {"name": "WebHtml", "example": "example"}

    async def webhtmlcmd(self, m: Message):
        """| Пример: .webhtml <сайт> <расширение> (расширение либо .html либо .txt)"""
        args = utils.get_args_raw(m)
        if not args:
            await utils.answer(m, self.strings["example"])
            return

        site, extension = args.split(' ')
        if not site.startswith('http'):
            site = 'https://' + site
       
        if not extension.startswith('.'):
            extension = '.' + extension

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(site) as response:
                    if response.status == 200:
                        content = await response.text()
                        file_name = "".join([str(random.randint(1, 9)) for _ in range(9)]) + extension

                        with open(file_name, "w", encoding="utf-8") as file:
                            file.write(content)

                        parsed_url = urlparse(site)
                        domain = parsed_url.netloc
                        message = await m.edit("<emoji document_id=5363972999433166941>😐</emoji>Получаю код...")

                        await m.client.send_file(m.to_id, file=file_name, caption=f"<emoji document_id=5447410659077661506>🌐</emoji>Код-HTML страницы {domain}:")
                        os.remove(file_name)
                        await message.delete()
                    else:
                        await utils.answer(m, "<emoji document_id=5210952531676504517>❌</emoji>Не удалось получить содержимое страницы")
        except Exception as e:
            await utils.answer(m, f"<emoji document_id=5240241223632954241>🚫</emoji>Произошла ошибка: {str(e)}")
