# meta developer: @LolDecMods
# scope: hikka_min 1.6.2

import base64
from hikkatl.types import Message

from .. import loader, utils  # type: ignore


@loader.tds
class bssh(loader.Module):
    """Зашифровать текст в шифр bs64 и наоборот"""

    strings = {"name": "bs64 coder"}
    strings_ru = {"name": "bs64 шифратор"}

    @loader.command(alias="code", ru_doc="| Зашифровать текст в Base64")
    async def codecmd(self, m: Message):
        """| Зашифровать текст Base64"""
        text_to_encode = m.text.split(" ", 1)[1]
        encoded_text = base64.b64encode(text_to_encode.encode()).decode()
        await utils.answer(m, f"| <emoji document_id=5352784961814405440>⚡️</emoji> | Зашифрованный текст: <code>{encoded_text}</code> | <emoji document_id=5352784961814405440>⚡️</emoji> |")

    @loader.command(alias="decode", ru_doc="| Расшифровать текст Base64")
    async def decodecmd(self, m: Message):
        """| Расшифровать текст Base64"""
        text_to_decode = m.text.split(" ", 1)[1]
        try:
            decoded_text = base64.b64decode(text_to_decode).decode()
            await utils.answer(m, f"| <emoji document_id=5242365016241352434>🔱</emoji> | Расшифрованный текст: <code>{decoded_text}</code> | <emoji document_id=5242365016241352434>🔱</emoji> |")
        except Exception as e:
            await utils.answer(m, f"| <emoji document_id=5440409175190415592>❌️</emoji> | Ошибка при декодировании: {str(e)} | <emoji document_id=5440409175190415592>❌️</emoji> |")