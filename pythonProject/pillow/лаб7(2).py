from PIL import Image
filename = "cat.jpg"
with Image.open(filename) as img:
     img.load()

low_res_img = img.resize((img.width // 3, img.height // 3))
# low_res_img.show()
low_res_img.save("low_res_img.jpg")
flip_left_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flip_left_img.save("flip_left_img.jpg")
flip_top_img = img.transpose(Image.FLIP_TOP_BOTTOM)
flip_top_img.show()
flip_top_img.save("flip_top_img.jpg")
