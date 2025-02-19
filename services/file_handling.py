import os
import sys
import re
import time

from aiohttp.web_fileresponse import content_type

# BOOK_PATH = 'book/Goncharov-Oblomov.txt'
# PAGE_SIZE = 1050
BOOK_PATH = 'Goncharov-Oblomov.txt'
PAGE_SIZE = 100

book: dict[int, str] = {}

# Функуция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    if len(text[start:]) < size:
        text_for_prepare = text[start:]
    elif text[start + size] in f'[.,!?;:)>-]':
        text_for_prepare = text[start:(start + size - 2)]
    else:
        text_for_prepare = text[start:start + size]
    matches = [m.start() for m in re.finditer(f'[.,!?;:)>]', text_for_prepare)]
    if not matches:
        matches = [m.start() for m in re.finditer(f'\\s', text_for_prepare)]
    text_for_prepare = text_for_prepare[:matches[-1] + 1]
    return text_for_prepare, len(text_for_prepare)

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

        size_text = len(content)
        position_in_text, count_page = 0, 1

        while size_text > position_in_text:
            next_block = _get_part_text(content, position_in_text, PAGE_SIZE)
            book[count_page] = next_block[0].lstrip()

            position_in_text += next_block[1]
            count_page += 1

# Вызов функции prepare_book для подготовки книги из тестового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
