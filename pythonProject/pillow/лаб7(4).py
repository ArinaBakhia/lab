from PIL import Image, ImageDraw, ImageFont


def watermark_text(input_img, output_img, text, pos):
    photo = Image.open(input_img)

    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype(r"C:\Users\arina\Downloads\Baskerville Bold Italic\Baskerville Bold Italic.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_img)


img = 'cat.jpg'
watermark_text(img, 'watercat.jpg', text='wake up', pos=(0, 0))
