from PIL import Image
filename = "cat.jpg"
with Image.open(filename) as img:
     img.load()
print(img)
print(img.format)
img.show()