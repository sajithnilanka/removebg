from rembg import remove
import easygui
from PIL import image

input = easygui.fileopenbox(title="select image file..")
outputpath =easygui.fileopenbox(title="save file to...")

input = image.open(inputpath)
output =remove(input)
output.save(outputpath)
