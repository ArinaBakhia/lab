from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def watermark_text(input_img, text, pos, text_font):

    drawing = ImageDraw.Draw(input_img)

    black = (3, 8, 12)
    font = ImageFont.truetype(text_font, 40)
    drawing.text(pos, text, fill=black, font=font)
    return input_img


HOLIDAYS = {
    "8 марта": "holiday.jpg",
    "23 февраля": "fed23.jpg",
    "день рождения": "hb.jpg",
    "новый год": "newyear.jpg"
}


position_input = input("Введите координаты текста:")
position = 50, 50
if position_input:
    position = tuple(map(int, position_input.split()))


text_hol = input("Введите текст поздравления:")
name_hol = input("Введите название праздника:")

text_font = r"C:\Users\arina\Downloads\Baskerville Bold Italic\Baskerville Bold Italic.ttf"
if text_font_input := input("Введите путь до файла шрифта (стандарт - Baskerville Bold Italic.ttf):"):
    text_font = text_font_input

img_path = Path(HOLIDAYS.get(name_hol))

with Image.open(img_path) as img:
     img.load()

p = Path(img.filename).name + "_filter"
img_and_text = watermark_text(img, text_font=text_font, text=text_hol, pos=position,)
img_and_text.show()