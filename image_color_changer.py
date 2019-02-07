from PIL import ImageColor, Image
import os

os.chdir("images/changeTransparency/")
os.makedirs('edited', exist_ok=True)
for file in os.listdir("."):
    file=file.lower()
    if not (file.endswith('.png') or file.endswith('.jpg')):
        continue
    image = Image.open(file)

    width, height = image.size
    name = image.filename

    pix_arr = []
    for x in range(width):
        for y in range(height):
            print(x, y)
            pix_arr.append(image.getpixel((x, y)))

    px_temp = []
    px_holder = {}
    for px in pix_arr:
        print(px)
        if px not in px_temp:
            px_temp.append(px)
            px_holder[pix_arr.count(px)] = px

    a = list(px_holder.keys())
    a.sort()
    print("sort gives %s " % a)

    for x in range(width):
        for y in range(height):
            px = image.getpixel((x, y))
            if px == px_holder.get(a[-1]):
                print("Changing Pixel Color..%d,%d" % (x, y))
                image.putpixel((x, y), (0, 0, 0,0))

    image.save(os.path.join("edited",file))
    print("Finished!")




