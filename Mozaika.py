# meta developer: @LolDecMods

import io
import os
import zipfile
from typing import List
from hikka.types import Message

from PIL import Image, UnidentifiedImageError

from .. import loader, utils


@loader.tds
class ModuleName(loader.Module):
    """Mozaika разделит ваше фото на несколько ровных частей"""

    strings = {"name": "mozaika"}
    strings_ru = {"name": "mozaika"}

    @loader.command(alias="mz", ru_doc="| Ответьте реплаем на фото, которое хотите разделить. Пример: .mz <на сколько частей разделить (2-4)> <сделать фото в img или file>")
    async def mzcmd(self, m: Message):
        """| Ответьте реплаем на фото, которое хотите разделить. Пример: .mz <на сколько частей разделить (2-4)> <сделать фото в img или file>"""
        args = utils.get_args_raw(m)
        split_count, output_format = self._parse_arguments(args)
        if not split_count:
            await utils.answer(m, "<emoji document_id=5447644880824181073>⚠️</emoji>После команды, укажите сколько частей делать. (От 2 до 4)<emoji document_id=5447644880824181073>⚠️</emoji>")
            return
        if not output_format:
            await utils.answer(m, "<emoji document_id=5440660757194744323>‼️</emoji>Пожалуйста, укажите формат вывода: [img/file]<emoji document_id=5440660757194744323>‼️</emoji>")
            return
        if split_count < 2 or split_count > 4:
            await utils.answer(m, "<emoji document_id=5240241223632954241>🚫</emoji>Нельзя сделать больше 4 частей, и меньше 2-ух частей!<emoji document_id=5240241223632954241>🚫</emoji>")
            return
        reply_message = await m.get_reply_message()
        if reply_message and reply_message.media:
            file = await reply_message.download_media()
            try:
                parts = await self._split_file(file, split_count)
                if output_format == "img":
                    output_files = [io.BytesIO(part) for part in parts]
                    await utils.answer_file(m, output_files)
                elif output_format == "file":
                    zip_file = await self._create_zip_file(parts)
                    zip_file.name = "фото.zip"
                    await utils.answer_file(m, zip_file, force_document=True, caption="Разделенные изображения без потери качества.\n\n"
                                                                                       "Распакуйте архив, фото в виде файла нельзя скинуть одним сообщением по причине того, что Telegram не поддерживает такое.")
            except UnidentifiedImageError:
                await utils.answer(m, "Тип изображения не поддерживается PIL, это не ошибка, это неисправимо по причинам самой библиотеки.")
            except ValueError:
                await utils.answer(m, "Изображение слишком маленькое для разделения.")
        await m.delete()

    def _parse_arguments(self, args: str) -> tuple[int, str]:
        split_count = 0
        output_format = ""
        if args:
            args_list = args.split()
            if args_list[0].isdigit():
                split_count = int(args_list[0])
                if len(args_list) > 1:
                    output_format = args_list[1].lower()
        return split_count, output_format

    async def _split_file(self, file: str, split_count: int) -> List[bytes]:
        parts = []
        with Image.open(os.path.abspath(file)) as img:
            img_width, img_height = img.size
            part_width = img_width // split_count
            if part_width <= 0:
                raise ValueError("Изображение слишком маленькое для разделения.")
            for i in range(split_count):
                left = i * part_width
                right = (i + 1) * part_width if i < split_count - 1 else img_width
                part_img = img.crop((left, 0, right, img_height))
                part_bytes = io.BytesIO()
                part_img.save(part_bytes, format="PNG")
                part_bytes.seek(0)
                parts.append(part_bytes.getvalue())
        return parts

    async def _create_zip_file(self, parts: List[bytes]) -> io.BytesIO:
        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zf:
            for i, part in enumerate(parts):
                zf.writestr(f"Part_{i+1}.png", part)
        zip_file.seek(0)
        return zip_file
