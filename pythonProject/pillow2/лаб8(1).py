from PIL import Image
img = Image.open('holiday.jpg')
cropped = img.crop((70, 80, 500, 600))
cropped.save('holi_crop.jpg')


