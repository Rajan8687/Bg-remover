from rembg import remove

from PIL import Image

input = Image.open("rajan.jpg")
output = remove(input)
output.save("rajancopy.png")