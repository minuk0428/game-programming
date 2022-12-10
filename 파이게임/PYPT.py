import pygame
import PIL
import random as r

ran = (r.randint(0,99))



from PIL import Image, ImageFilter, ImageEnhance, ImageOps
img = Image.open("/Users/imin-ug/Python/PythonGame/OneDrive_2022-10-13/photo/picture"+ran+"jpg")
img.show()
img = img.filter(ImageFilter.FIND_EDGES)
img.show()