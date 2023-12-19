import PIL
from tkinter.filedialog import *
from PIL import Image
file_loc=askopenfilenames()
img = Image.open(file_loc[0])
img.save("Compressed.jpg", "JPEG", optimize = True, quality = 10)
print("Image is Compressed")
