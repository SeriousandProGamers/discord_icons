import os
from PIL import Image

print("Enter Directory to convert in:")
fldr = input()
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

for file in os.listdir(fldr):
    if file.endswith(".png"):
        print(f"Processing File: {file}")
        im = Image.open(file)
        newFileName = file.replace(".png", ".ico")
        im.save(newFileName, format='ICO', sizes=icon_sizes)
