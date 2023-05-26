from pathlib import Path
from PIL import Image


HOLIDAYS = {
    "8 марта": "holiday.jpg",
    "23 февраля": "fed23.jpg",
    "день рождения": "hb.jpg",
    "новый год": "newyear.jpg"
}


name_hol = input("Введите название праздника:")
img_path = Path(HOLIDAYS.get(name_hol))

with Image.open(img_path) as img:
     img.load()

img.show()
