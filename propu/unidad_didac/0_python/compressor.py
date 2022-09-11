# https://www.youtube.com/watch?v=sW4ScHICKtI

from PIL import Image

import os

downloadsFolder = 'C:/Users/Marco/Documents/GitHub/taca/propu/unidad_didac/0_python/'

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in ['.jpg', '.jpeg', '.png']:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed" + filename, optimize = True, quality = 60)
            
        
