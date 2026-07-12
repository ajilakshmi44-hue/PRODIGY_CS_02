from PIL import Image

img = Image.open("image.jpg.jpg")

pixels = img.load()

width, height = img.size

key = 50

for x in range(width):
    for y in range(height):

        r, g, b = pixels[x, y]

        r = (r + key) % 256
        g = (g + key) % 256
        b = (b + key) % 256

        pixels[x, y] = (r, g, b)

img.save("encrypted.png")

print("Image Encrypted")