# Creates images of bees by replacing the following values:
# (237, 28, 36)
# (255, 242, 0)
# (63, 72, 204)

from io import BytesIO
from random import randint
from PIL import Image
import os

def generate_random():
    with Image.open("bee.png") as img:
        a = []
        data = img.getdata()

        rand1 = (randint(0, 255), randint(0, 255), randint(0, 255), 255)
        rand2 = (randint(0, 255), randint(0, 255), randint(0, 255), 255)
        rand3 = (randint(0, 255), randint(0, 255), randint(0, 255), 255)

        filename = str(hash(rand1 + rand2 + rand3)) + ".png"

        # In case somehow a bee was already generated
        if os.path.exists(filename):
            return filename

        for item in data:
            if item == (237, 28, 36, 255):
                a.append(rand1)
            elif item == (255, 242, 0, 255):
                a.append(rand2)
            elif item == (63, 72, 204, 255):
                a.append(rand3)
            else:
                a.append(item)

        img.putdata(a)
        with BytesIO() as image_binary:
            img.save(image_binary, "PNG")
            image_binary.seek(0)
            #with open("temp.png", "wb") as t:
            #    t.write(image_binary.read())
            #    return t
            return image_binary.read()