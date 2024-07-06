from easygui import *
from rembg import remove
from PIL import Image
import os
from set_dimensions import get_new_size

# array of creature sizes
choices = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]

def set_image_details(pdf, output_path):
    # set input file and remove background
    input_image = fileopenbox(title="Select Image File", default=output_path)
    input = Image.open(input_image) 
    no_bg = remove(input)

    # select image size
    image_size = choicebox(msg='Choose Creature Size', title='Choose Creature Size', choices=choices)

    # select number of creatures, i.e. number of duplicate images
    text = "Enter the number of copies of this creature to generate"
    title = "Enter the number of copies of this creature to generate"
    d_int = 1
    lower = 0
    upper = 100
    image_number = integerbox(text, title, d_int, lower, upper)

    # extract image name and generate PDF name from folder name
    long_name = input_image.split("\\")
    name = long_name[-1].split(".")
    image_name = name[0]

    # set new dimensions and save transparent png file using those dimensions
    new_dimensions = get_new_size(image_size, input)
    output = no_bg.resize(new_dimensions)
    path = os.path.join(output_path, image_name+".png")
    output.save(path)

    #convert pixel dimensions to mm
    mm_width = output.width * 0.265
    mm_height = output.height * 0.265

    # loop through number of images and add to pdf
    for i in range(image_number):
        if int(pdf.get_x()) <= (210-(2*mm_width)):
            pdf.cell(w=mm_width, h=mm_height, link=pdf.image(name=path, x=pdf.get_x(), y=pdf.get_y(), w=mm_width, h=mm_height), border=1, ln=0)
        else:
            pdf.cell(w=mm_width, h=mm_height, link=pdf.image(name=path, x=None, y=pdf.get_y(), w=mm_width, h=mm_height), border=1, ln=1)