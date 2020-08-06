import os
import cairosvg

def convert_files():
    for filename in os.listdir(os.path.dirname(__file__) + "./images"):
        if filename.endswith(".svg"):
            file_path = os.path.dirname(__file__) + "./images/" + filename
            cairosvg.svg2png(url=file_path, write_to="./target/" + filename[:-4] + ".png")

convert_files()

