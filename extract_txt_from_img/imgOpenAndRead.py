from PIL import Image
import sys
try:
    a= Image.open("image1.png")
    a.show()
except:
    print("Error", sys.exc_info()[1])
