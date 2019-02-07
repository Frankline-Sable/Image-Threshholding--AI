from functools import reduce
import os
from PIL import Image

env = os.environ["USERNAME"]
path = "C://users//%s//Documents//Sample Image//" % env

os.makedirs(path, exist_ok=True)
os.chdir(path)
input("Place the image in the 'Documents/Sample Image folder' in order to sample it")

status = False
for files in os.listdir(path):
    files = files.lower()
    if files.endswith(".jpg") or files.endswith(".png"):
        print("Sampling Image %s" % files)
        status = True
        image = Image.open(files)
        width, height = image.size

        balanceArr = []
        for x in range(width):
            for y in range(height):
                avg = reduce(lambda x, y: x + y, image.getpixel((x, y))[:3]) / len(image.getpixel((x, y))[:3])
                balanceArr.append(avg)
        balance = reduce(lambda x, y: x + y, balanceArr) / len(balanceArr)
        for x in range(width):
            for y in range(height):
                if reduce(lambda x, y: x + y, image.getpixel((x, y))[:3]) / len(image.getpixel((x, y))[:3]) > balance:
                    image.putpixel((x, y), (255, 255, 255, 255))
                else:
                    image.putpixel((x, y), (0, 0, 0, 255))

        image.save("samp_%s" % files)
        print("Sampling Complete for %s\n" % files)

if not status:
    print("\nYou haven't placed an image in the folder")
