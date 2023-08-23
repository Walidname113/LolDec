#meta developer: @LolDecMods

from hikkatl.types import Message

from .. import loader, utils


@loader.tds
class TextEditorM(loader.Module):
    """Модуль для быстрого доступа к каналам с модулями"""

    strings = {"name": "TextEditorM", "example": "Модуль для личного использования."}
    strings_ru = {"example": "Модуль для быстрого доступа к каналам с модулями"}

    @loader.command(alias="cmd", ru_doc="| Быстрый доступ к каналам с модулями ")
    async def modlist(self, m: Message):
        """quick access to channels with modules"""
        custom_text = "Hikka Modules\n💭 @hikarimods\n🦋 @morisummermods\n❤️‍🔥 @cakestwix_mods\n💚 @nalinormods\n🤩 @AstroModules\n🌚 @vsecoder_m\n☺️ @mm_mods\n😈 @apodiktum_modules\n😉 @shadow_modules\n😇 @wilsonmods\n🤔 @amoremods\n👑 @DorotoroMods\n✌️ @HikkaFTGmods"
        await m.edit(custom_text)

