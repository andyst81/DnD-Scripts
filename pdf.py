from easygui import *
from fpdf import FPDF
from set_image_details import set_image_details

def pdf():
    # create a pdf to save images to
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    #set destination for PDF file
    output_path = diropenbox(msg="Select destination folder for PDF", title="Destination") 
    pdf_name = output_path.split("\\")[-1]
    print(output_path)

    #loop to continue adding creatures
    add = True
    while add:
        set_image_details(pdf, output_path)
        add=add_image()

    pdf.output(f'{output_path}\\{pdf_name}.pdf', 'F')

def add_image():
    add_image = ynbox("Would you like to add another creature?")
    return add_image