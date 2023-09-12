from PIL import Image
from PIL import ImageDraw

img = Image.open('photo1.jpg')
img_draw = ImageDraw.Draw(img)
img_draw.text((28, 36), "7learn.com", fill=(255, 0, 0))
img.save('photo1w.jpg')
