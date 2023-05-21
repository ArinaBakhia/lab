from PIL import Image, ImageFilter
from pathlib import Path


def img_filter(image_path: Path):
    if image_path.suffix not in (".png",".jpg"):
        return
    with Image.open(image_path) as img:
        img.load()
    em1 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    em1.save(filter_img / Path(img.filename).name)


default_img = Path("default_img")
filter_img = Path("filter_img")
filter_img.mkdir(exist_ok=True)
list(map(img_filter, default_img.iterdir()))


# + выполнено задание 9.1 и 9.2

