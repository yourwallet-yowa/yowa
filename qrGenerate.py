import qrcode
import sys

def generateQR(data):
    img = qrcode.make(str(data))
    img.show()

generateQR(sys.argv[1])
