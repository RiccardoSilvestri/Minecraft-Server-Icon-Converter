from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image

# Open the file selection dialog
Tk().withdraw()
filename = askopenfilename()

# Upload the image and resize it
image = Image.open(filename)
image = image.resize((64, 64))

# Save the image as a PNG with the name "server-icon.png"
output_filename = "server-icon.png"
image.save(output_filename, "PNG")

print("Conversion complete!")
