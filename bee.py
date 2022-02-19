# Creates images of bees by replacing the following values:
# (237, 28, 36)
# (255, 242, 0)
# (63, 72, 204)

from random import randint
from PIL import Image
import os

def generate_random():
    a = []
    img = Image.open("bee.png")
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
    img.save(filename)
    return filename
