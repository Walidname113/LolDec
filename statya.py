# meta developer: @LolDecMods
# scope: hikka_min 1.6.2

import json
import random
import requests
from typing import Dict

from hikkatl.types import Message

from .. import loader, utils  # type: ignore


@loader.tds
class RandomValueModule(loader.Module):
    """Выводит твою статью УКРФ."""

    strings = {"name": "    Your C.C.F.R. Article", "example": "example"}
    strings_ru = {"name": "Your C.C.F.R. Article"}

    @loader.command(alias="rs", ru_doc="Выводит твою статью УКРФ.\n\nСпасибо @tvoya_statya_bot за их предоставление.")
    async def rscmd(self, m: Message):
        """Brings up your F.C.C. article.\n\nThanks to @tvoya_statya_bot for providing them."""
        values = self._load_values() 
        if values:
            random_key = random.choice(list(values.keys()))
            random_value = values[random_key]
            message = f"📕<u>Твоя статья УК РФ</u>: {random_key} - <tg-spoiler>{random_value}.</tg-spoiler>"
            await utils.answer(m, message)

    def _load_values(self) -> Dict[str, str]:
        url = "https://raw.githubusercontent.com/Walidname113/LolDec/main/works.json"
        try:
            response = requests.get(url)
            if response.ok:
                data = json.loads(response.text)
                return data
        except (requests.RequestException, json.JSONDecodeError):
            pass

        return {}
