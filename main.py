from PIL import Image, ImageFont, ImageDraw
import uuid


#commenting for testing 
# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"
#font for id
ID_FONT = ImageFont.truetype('font/freeMono.ttf', 60)

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''
    
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    id= str(uuid.uuid4())[:8]

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # placing id at the left top corner of the image
    draw.text((10, 10), id, fill=FONT_COLOR,font=ID_FONT)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    names = ['Tushar Nankani', "Full Name", 'Some Long Ass Name Might Not Work']
    # for name in names:
    make_certificates("joginder")
    print(len(names), "certificates done.")

